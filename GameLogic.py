from Dealer import Dealer
from Deck import Deck
from Player import Player
from Hand import Hand


class GameLogic:
    def __init__(self, deck, dealer,player):
        self.deck = deck
        self.dealer = dealer
        self.player = player
        self.ended = True

    def deal(self):
        self.ended = False
        self.player.money -= self.player.get_bet()  # Deduct the bet from the self.player's money
        # Draw the dealer's hand
        self.dealer.draw_hand()
        # Draw the self.player's hand
        self.player.draw_hand()
        # Check for blackjack
        if self.player.getHand().blackjack:
            self.player.pointer -= 1
        self.dealer.hidden = True  # Hide the dealer's second card

    def can_play(self):
        return self.player.pointer > -1 and not self.player.getHand().bust and self.player.getHand().get_value() != 21
    
    def hit(self):
        if self.can_play():
            self.player.draw_card()
            # If the self.player busts or has 21, move to the next hand
            if self.player.getHand().bust or self.player.getHand().get_value() == 21:
                self.player.pointer -= 1

    def stand(self):
        # Move to the next hand
        if self.can_play():
            self.player.pointer -= 1

    def can_double_down(self):
        return len(self.player.getHand().cards) == 2 and self.player.money >= self.player.get_bet()
    
    def double_down(self):
        if self.can_double_down():
            self.player.money -= self.player.get_bet()
            self.player.set_bet(2 * self.player.get_bet())
            self.player.draw_card()
            self.player.pointer -= 1

    def can_split(self):
        return self.player.money >= self.player.get_bet() and len(self.player.getHand().cards) == 2 and self.player.getHand().cards[0].get_value() == self.player.getHand().cards[1].get_value()
    
    def split(self):
        if self.can_split():
            self.player.hands.insert(self.player.pointer+1,Hand())
            self.player.hands[self.player.pointer+1].add_card(self.player.getHand().cards.pop())
            self.player.bets.append(self.player.get_bet())  # Set the bet for the new hand
            self.player.money -= self.player.get_bet()
            self.player.pointer += 1


    def insurance(self):
        if not self.player.insurance and self.dealer.hand.cards[1].rank == "Ace" and self.player.money >= self.player.get_bet() / 2:
            self.player.money -= self.player.get_bet() / 2
            self.player.insurance = True
    
    def update_balance(self):
        # Update player's balance based on game outcome
        for i in range(len(self.player.hands)):
            if not self.player.hands[i].bust:
                if self.player.hands[i].get_value() == self.dealer.hand.get_value():
                    self.player.money += self.player.bets[i]
                elif self.player.hands[i].blackjack:
                    self.player.money += 2.5 * self.player.bets[i]
                elif self.dealer.hand.bust:
                    self.player.money += 2 * self.player.bets[i]
                elif self.player.hands[i].get_value() > self.dealer.hand.get_value():
                    self.player.money += 2 * self.player.bets[i]

        # Pay insurance if the dealer has blackjack
        if self.dealer.hand.blackjack and self.player.insurance:
            self.player.money += 2 * self.player.bets[0]
        self.player.reset_bets()

    def check_for_action(self):
        # If the player can't play anymore, move on   
        if self.player.pointer == -1:
            if self.dealer.hidden:
                self.dealer.hidden = False  
            elif self.dealer.hand.get_value() < 17:
                self.dealer.draw_card()
                return True
            else:
                self.update_balance()
                # Check if the deck needs to be rebuilt and shuffled
                if len(self.deck.cards)<104:
                    self.deck.build()
                    self.deck.shuffle()
                self.ended = True
                return True
        # If has one card in his hand, draw another card (happens after split)        
        elif len(self.player.getHand().cards) == 1:
            self.player.draw_card()
            if self.player.getHand().get_value() == 21:
                self.player.pointer -= 1
            return True
        return False