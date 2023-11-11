import pygame

# Dictionary mapping card names to image file names
images = {
    "2 of Clubs": "2_of_clubs",
    "2 of Diamonds": "2_of_diamonds",
    "2 of Hearts": "2_of_hearts",
    "2 of Spades": "2_of_spades",
    "3 of Clubs": "3_of_clubs",
    "3 of Diamonds": "3_of_diamonds",
    "3 of Hearts": "3_of_hearts",
    "3 of Spades": "3_of_spades",
    "4 of Clubs": "4_of_clubs",
    "4 of Diamonds": "4_of_diamonds",
    "4 of Hearts": "4_of_hearts",
    "4 of Spades": "4_of_spades",
    "5 of Clubs": "5_of_clubs",
    "5 of Diamonds": "5_of_diamonds",
    "5 of Hearts": "5_of_hearts",
    "5 of Spades": "5_of_spades",
    "6 of Clubs": "6_of_clubs",
    "6 of Diamonds": "6_of_diamonds",
    "6 of Hearts": "6_of_hearts",
    "6 of Spades": "6_of_spades",
    "7 of Clubs": "7_of_clubs",
    "7 of Diamonds": "7_of_diamonds",
    "7 of Hearts": "7_of_hearts",
    "7 of Spades": "7_of_spades",
    "8 of Clubs": "8_of_clubs",
    "8 of Diamonds": "8_of_diamonds",
    "8 of Hearts": "8_of_hearts",
    "8 of Spades": "8_of_spades",
    "9 of Clubs": "9_of_clubs",
    "9 of Diamonds": "9_of_diamonds",
    "9 of Hearts": "9_of_hearts",
    "9 of Spades": "9_of_spades",
    "10 of Clubs": "10_of_clubs",
    "10 of Diamonds": "10_of_diamonds",
    "10 of Hearts": "10_of_hearts",
    "10 of Spades": "10_of_spades",
    "Jack of Clubs": "jack_of_clubs",
    "Jack of Diamonds": "jack_of_diamonds",
    "Jack of Hearts": "jack_of_hearts",
    "Jack of Spades": "jack_of_spades",
    "Queen of Clubs": "queen_of_clubs",
    "Queen of Diamonds": "queen_of_diamonds",
    "Queen of Hearts": "queen_of_hearts",
    "Queen of Spades": "queen_of_spades",
    "King of Clubs": "king_of_clubs",
    "King of Diamonds": "king_of_diamonds",
    "King of Hearts": "king_of_hearts",
    "King of Spades": "king_of_spades",
    "Ace of Clubs": "ace_of_clubs",
    "Ace of Diamonds": "ace_of_diamonds",
    "Ace of Hearts": "ace_of_hearts",
    "Ace of Spades": "ace_of_spades",
    "Back of Card": "card_back"
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def show(self, screen, x, y, scale):
        # Load and scale the card image
        image = pygame.image.load("card_images/" + images[self.rank + " of " + self.suit] + ".png")
        image = pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))
        # Draw the card on the screen
        screen.blit(image, (x, y))

    def get_value(self):
        # Return the value of the card (for blackjack)
        if self.rank in {"Jack", "Queen", "King"}:
            return 10
        elif self.rank == "Ace":
            return 11
        else:
            return int(self.rank)
