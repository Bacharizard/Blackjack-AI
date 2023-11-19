import random
from Card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.count = 0
        self.build()
        self.shuffle()

    def build(self):
        self.cards.clear()
        self.count = 0
        # Build a deck with four sets of cards (suits and ranks)
        for times in range(6):
            for s in ["Clubs", "Diamonds", "Hearts", "Spades"]:
                for v in {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack","Queen", "King", "Ace"}:
                    self.cards.append(Card(s, v))

    def shuffle(self):
        # Shuffle the deck
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        card = self.cards.pop()
        if card.get_value() in {"10", "Jack", "Queen", "King", "Ace"}:
            self.count -= 1
        elif card.get_value() in {"2", "3", "4", "5", "6"}:
            self.count += 1
        return card

    def get_true_count(self):
        return self.count / (len(self.cards) / 52)
