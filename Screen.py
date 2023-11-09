import pygame
from Card import Card
from Deck import Deck
from Hand import Hand
from Dealer import Dealer
from Player import Player

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080))  # Adjust the size as needed
pygame.display.set_caption("Blackjack Game")

# Create game objects
deck = Deck()
dealer = Dealer(deck)
player = Player("Player", deck)

# Create buttons
font = pygame.font.Font(None, 36)
button_width, button_height = 170, 40
button_spacing = 10  # Vertical spacing between buttons

# Adjusted button positions to move them up
hit_button = pygame.Rect(1700, 1000 - 3 * (button_height + button_spacing), button_width, button_height)
stand_button = pygame.Rect(1700, 1000 - 2 * (button_height + button_spacing), button_width, button_height)
double_down_button = pygame.Rect(1700, 1000 - (button_height + button_spacing), button_width, button_height)
split_button = pygame.Rect(1700, 1000, button_width, button_height)  

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green_cloth = (0, 153, 76)
yellow = (255, 255, 0)

# Drawing the dealer's hand
dealer.drawCard()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    screen.fill(green_cloth)

    # Render dealer's cards
    dealer.show(screen)

    # Draw buttons
    pygame.draw.rect(screen, white, hit_button)
    pygame.draw.rect(screen, white, stand_button)
    pygame.draw.rect(screen, white, double_down_button)
    pygame.draw.rect(screen, white, split_button)  

    # Button labels
    hit_text = font.render("Hit", True, black)
    stand_text = font.render("Stand", True, black)
    double_down_text = font.render("Double Down", True, black)
    split_text = font.render("Split", True, black)

    screen.blit(hit_text, (hit_button.x + 10, hit_button.y + 10))
    screen.blit(stand_text, (stand_button.x + 10, stand_button.y + 10))
    screen.blit(double_down_text, (double_down_button.x + 10, double_down_button.y + 10))
    screen.blit(split_text, (split_button.x + 10, split_button.y + 10))  # Display Split button label

    pygame.display.flip()
    pygame.time.delay(1000)
    dealer.drawCard()
