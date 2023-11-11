from Card import Card
from Deck import Deck
import pygame


class Hand:
    def __init__(self):
        self.cards = []  # A list to store the cards in the hand
        self.bust = False
        self.blackjack = False

    def add_card(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards.clear()
        self.bust = False
        self.blackjack = False


    def get_value(self):
        value = 0
        num_aces = 0

        for card in self.cards:
            value += card.get_value()

            # Check for aces and count them separately
            if card.rank == 'Ace':
                num_aces += 1

        # Handle aces to minimize busting
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        # Update bust and blackjack attributes
        self.bust = value > 21
        self.blackjack = value == 21 and len(self.cards) == 2

        return value

    def draw_card(self, deck):
        card = deck.draw_card()
        self.add_card(card)
        self.get_value()
        return card

