import random
from Card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()

    def build(self):
        # Build a deck with four sets of cards (suits and ranks)
        for times in range(4):
            for s in ["Clubs", "Diamonds", "Hearts", "Spades"]:
                for v in {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack","Queen", "King", "Ace"}:
                    self.cards.append(Card(s, v))

    def shuffle(self):
        # Shuffle the deck
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        # Draw a card from the deck
        return self.cards.pop()
