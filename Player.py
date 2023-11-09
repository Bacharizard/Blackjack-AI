from Card import Card
from Deck import Deck
from Hand import Hand

class Player:
    def __init__(self, name,deck):
        self.name = name
        self.hand = Hand()
        self.deck = deck
        self.bust = False
        self.blackjack = False

    def drawCard(self):
        self.hand.add_card(self.deck.drawCard())
        if self.hand.get_value() > 21:
            self.bust = True
        if self.hand.get_value() == 21:
            self.blackjack = True
        
    def show(self,screen):
        numCards = len(self.hand.cards)
        screenWidth = 1920
        screenHeight = 1080
        cardWidth = 500
        cardHeight = 726
        maxHeight = 500
        startX = (1920-(maxHeight/cardHeight)*cardWidth)/2
        scale = maxHeight/((1+(numCards-1)*3/4)*cardHeight)
        for i in range(numCards):
            self.hand.cards[i].show(screen,startX+i*cardWidth*scale*3/4,screenHeight-cardHeight*scale*(1+i*(3/4)),scale)
            print(startX)

    