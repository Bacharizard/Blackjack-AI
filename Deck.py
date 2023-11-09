import random
from Card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()

    def build(self):
        for s in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for v in {"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
                      "Queen", "King", "Ace"}:
                self.cards.append(Card(s, v))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()
