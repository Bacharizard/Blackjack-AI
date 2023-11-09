from Card import Card
from Deck import Deck
from Hand import Hand

cardBack = Card("Card","Back")

class Dealer:
    def __init__(self,deck):
        self.deck = deck
        self.hand = Hand()
        self.bust = False
        self.blackjack = False
        self.stand = False
    
    def drawCard(self):
        self.hand.add_card(self.deck.drawCard())
        if self.hand.get_value() == 21:
            self.blackjack = True
        if self.hand.get_value() > 21:
            self.bust = True
        
    def drawHand(self):
        self.hand.clear()
        self.bust = False
        self.blackjack = False
        self.stand = False
        self.drawCard()
        self.drawCard()

    def show(self,screen):
        numCards = len(self.hand.cards)
        screenWidth = 1920
        cardWidth = 500
        screenGap = 1000
        cardGap=100
        scale = screenWidth/(2*screenGap+numCards*cardWidth+(numCards-1)*cardGap)
        for i in range(numCards):
            if numCards==2 and i ==1 and not self.stand:
                cardBack.show(screen,screenGap*scale+i*(cardWidth+cardGap)*scale,0,scale)
            else:    
                self.hand.cards[i].show(screen,screenGap*scale+i*(cardWidth+cardGap)*scale,0,scale)

        