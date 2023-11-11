from Card import Card
from Deck import Deck
from Hand import Hand

cardBack = Card("Card", "Back")

class Dealer:
    def __init__(self, deck):
        self.deck = deck
        self.hand = Hand()
        self.hidden = True  # Flag to determine if the second card is hidden

    def draw_card(self):
        # Draw a card for the dealer
        self.hand.draw_card(self.deck)

    def draw_hand(self):
        # Draw the initial two cards for the dealer
        self.hand.clear()
        self.hand.draw_card(self.deck)
        self.hand.draw_card(self.deck)

    def show(self, screen):
        # Render dealer's cards on the screen
        numCards = len(self.hand.cards)
        screenWidth = 1920
        cardWidth = 500
        screenGap = 2 * cardWidth
        cardGap = 0.2 * cardWidth
        scale = screenWidth / (2 * screenGap + numCards * cardWidth + (numCards - 1) * cardGap)
        for i in range(numCards):
            if numCards == 2 and i == 0 and self.hidden:
                # Render the back of the second card if it is hidden
                cardBack.show(screen,screenWidth - scale* (screenGap + cardWidth + i * (cardWidth+cardGap)), 0, scale)
            else:
                # Render the visible cards
                self.hand.cards[i].show(screen, screenWidth - scale* (screenGap + cardWidth + i * (cardWidth+cardGap)), 0, scale)
