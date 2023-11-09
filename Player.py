from Card import Card
from Deck import Deck
from Hand import Hand

class Player:
    def __init__(self, name,deck):
        self.name = name
        self.hand = Hand()
        self.deck = deck
        self.score = 0
        self.wins = 0

    def drawHand(self):
        self.hand.add_card(self.deck.drawCard())
        self.hand.add_card(self.deck.drawCard())