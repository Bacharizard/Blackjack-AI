from Player import Player
import NeuralNetwork as NN
import GameLogic as gl
import numpy as np

class Agent (Player):
    def __init__(name,deck,dealer,nn):
        self.dealer = dealer
        self.nn = nn
        super().__init__(name,deck)

    def set_bet(self):
        X = np.array([0, 0, 0, self.deck.get_true_count()])
        bet = self.nn.forward(X)[5]
        super().set_bet(bet)

    def should_insure(self):
        X = np.array([0, 0, 0, self.deck.get_true_count()])
        res = self.nn.forward(X)[4]
        if res > 0.5:
            gl.insurance(self)

        
    
    def action(self):
        X = np.array([self.getHand()[0].get_value(), self.getHand()[1].get_value() , self.dealer.hand.cards[1].get_value(), self.deck.get_true_count()])
        action = np.argmax(nn.forward(X)[0:4])
        if action == 0:
            gl.hit(self)
        elif action == 1:
            gl.stand(self)
        elif action == 2:
            gl.double_down(self)
        elif action == 3:
            gl.split(self)
    