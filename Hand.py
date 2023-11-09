from Card import Card
from Deck import Deck
import pygame


class Hand:
    def __init__(self):
        self.cards = []  # A list to store the cards in the hand

    def add_card(self, card):
        """Add a card to the hand."""
        self.cards.append(card)

    def clear(self):
        """Remove all cards from the hand."""
        self.cards = []

    def get_value(self):
        """Calculate and return the value of the hand."""
        value = 0
        num_aces = 0

        for card in self.cards:
            value += card.get_value()

            # Check for aces and count them separately
            if card.get_rank() == 'Ace':
                num_aces += 1

        # Handle aces to minimize busting
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value
    
    def PlayerShow(self,screen,x,y):
        self.cards[0].show(screen,x,y)
        self.cards[1].show(screen,x+300,y)

