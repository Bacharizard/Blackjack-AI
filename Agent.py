from Player import Player
from Deck import Deck
from NeuralNetwork import NeuralNetwork
from Card import Card
from Hand import Hand
from Dealer import Dealer
from GameLogic import GameLogic
import numpy as np
import math

class Agent (Player):
    def __init__(self,name,deck,dealer,nn):
        self.dealer = dealer
        self.nn = nn
        super().__init__(name,deck)
    
    def decide_bet(self):
        X = np.array([0, 0, 0, self.deck.get_true_count()])
        bet = self.nn.forward(X)[5]
        super().set_bet(math.ceil(bet*self.money))

    def should_insure(self,gl):
        X = np.array([0, 0, 0, self.deck.get_true_count()])
        res = self.nn.forward(X)[4]
        if res > 0.5:
           gl.insurance()

        
    
    def action(self,gl):
        X = np.array([self.getHand().cards[0].get_value(), self.getHand().cards[1].get_value() , self.dealer.hand.cards[0].get_value(), self.deck.get_true_count()])
        outputs = self.nn.forward(X)
        if not gl.can_double_down():
            outputs[2] = -1
        if not gl.can_split():
            outputs[3] = -1

        action = np.argmax(outputs[:4])
        if action == 0:
            gl.hit()
            print("AI hits")
        elif action == 1:
            gl.stand()
            print("AI stands")
        elif action == 2:
            gl.double_down()
            print("AI doubles down")
        elif action == 3:
            gl.split()
            print("AI splits")

    def play_round(self,gl):
        self.decide_bet()
        gl.deal()
        self.should_insure(gl)
        print("--------------------")
        print("AI's money: " + str(self.money) + " AI's bet: " + str(self.get_bet()))
        print("AI's hand: " + str(self.getHand().cards[0]) + " " + str(self.getHand().cards[1]))
        print("Dealer's card: " + str(self.dealer.hand.cards[0]))
        print("XXXXXXXXXXXXXXXXXXXXXXXXX")
        while not gl.ended:
            if gl.can_play():
                self.action(gl)
            gl.check_for_action()
        print("Action Done")
        print("AI's money: " + str(self.money))
        s = "["
        for hand in self.hands:
            s += str(hand) + ", "
        s += "]"
        print("AI's hand: " +  s)
        print("Dealer's hand: " + str(dealer.hand))
        print("---------------------------")
        
        

deck = Deck()
dealer = Dealer(deck)
nn = NeuralNetwork(4,5,6)
agent = Agent("AI",deck,dealer,nn)
gl = GameLogic(deck,dealer,agent)

for i in range(100):
    if(agent.money >= 1):
        agent.play_round(gl)


