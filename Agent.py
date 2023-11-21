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
        self.gl = GameLogic(deck,dealer,self)
        self.hands_played = 0
        self.fitness = 0
        super().__init__(name,deck)
    
    def decide_bet(self):
        X = np.array([0, 0, 0, self.deck.get_true_count()])
        bet_rate = self.nn.forward(X)[5]
        bet = math.ceil(bet_rate * self.money)
        if(abs(self.money - bet) < 1):
            bet = self.money
        self.set_bet(bet)
        
    def should_insure(self):
        X = np.array([0, 0, 0, self.deck.get_true_count()])
        res = self.nn.forward(X)[4]
        if res > 0.5:
           self.gl.insurance()

        
    
    def action(self):
        X = np.array([self.getHand().get_value(), self.getHand().get_soft_value() , self.dealer.hand.cards[0].get_value(), self.deck.get_true_count()])
        outputs = self.nn.forward(X)
        if not self.gl.can_double_down():
            outputs[2] = -1
        if not self.gl.can_split():
            outputs[3] = -1

        action = np.argmax(outputs[:4])
        if action == 0:
            self.gl.hit()
        elif action == 1:
            self.gl.stand()
        elif action == 2:
            self.gl.double_down()
        elif action == 3:
            self.gl.split()

    def play_round(self):
        self.decide_bet()
        self.gl.deal()
        self.should_insure()
        while not self.gl.ended:
            if self.gl.can_play():
                self.action()
            self.gl.check_for_action()
    
    def crossover(self, other):
        new_nn = self.nn.crossover(other.nn)
        new_deck = Deck()
        new_dealer = Dealer(new_deck)
        return Agent("AI",new_deck,new_dealer,new_nn)
    
    def mutate(self):
       self.nn.mutate()
        


