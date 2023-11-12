from Card import Card
from Deck import Deck
from Hand import Hand
from Dealer import Dealer

class Player:
    def __init__(self, name, deck):
        self.name = name
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


    def split(self):
        # Split the current hand into two hands
        self.hands.insert(self.pointer+1,Hand())
        self.hands[self.pointer+1].add_card(self.getHand().cards.pop())
        self.bets.append(self.get_bet())  # Set the bet for the new hand
        self.money -= self.get_bet()
        self.pointer += 1

    def update_balance(self, dealer):
        # Update player's balance based on game outcome
        for i in range(len(self.hands)):
            if not self.hands[i].bust:
                if dealer.hand.bust:
                    self.money += 2 * self.bets[i]
                elif self.hands[i].get_value() == dealer.hand.get_value():
                    self.money += self.bets[i]
                elif self.hands[i].blackjack:
                    self.money += 2.5 * self.bets[i]
                elif self.hands[i].get_value() > dealer.hand.get_value():
                    self.money += 2 * self.bets[i]

        # Pay insurance if the dealer has blackjack
        if dealer.hand.blackjack and self.insurance:
            self.money += 2 * self.bets[0]
        self.reset_bets()

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

