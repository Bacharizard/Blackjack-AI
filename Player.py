from Card import Card
from Deck import Deck
from Hand import Hand
from Dealer import Dealer

class Player:
    def __init__(self, deck):
        self.pointer = 0
        self.deck = deck
        self.hands = [Hand()]  # Initialize with one hand
        self.bets = [0]  # List to store bets corresponding to each hand
        self.money = 1000
        self.insurance = False

    def getHand(self):
        return self.hands[self.pointer]
    
    def reset_bets(self):
        self.bets = [0]
        self.pointer = 0
        self.insurance = False

    
    def get_bet(self):
        return self.bets[self.pointer]
    
    def set_bet(self, bet):
        self.bets[self.pointer] = bet
    
    def draw_card(self):
        card = self.getHand().draw_card(self.deck)

    def draw_hand(self):
        # Draw a new hand for the player
        self.hands = [Hand()]
        self.getHand().draw_card(self.deck)
        self.getHand().draw_card(self.deck)
        self.pointer = 0

    def show(self, screen):
        # Render player's cards on the screen
        if len(self.hands) != 0:
            numHands = len(self.hands)
            screenWidth = 1920
            screenHeight = 1080
            cardWidth = 500
            cardHeight = 726
            screenGap = 2 * cardWidth
            handWidth = 0.7 * cardWidth
            handGap = 0.05 * handWidth
            handScale = screenWidth / (2 * screenGap + numHands * handWidth + (numHands - 1) * handGap)
            for i in range(numHands):
                scale = (handWidth * handScale) / (cardWidth * (1 + (3 / 4) * (len(self.hands[i].cards) - 1)))
                for j in range(len(self.hands[i].cards)):
                    self.hands[i].cards[j].show(screen, handScale * (screenGap + i * (handWidth + handGap)) + (3 / 4) * j * cardWidth * scale, 
                                                screenHeight - cardHeight * (1 + (3 / 4) * j) * scale, scale)