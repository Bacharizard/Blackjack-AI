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
deal_button = pygame.Rect(1700, 1000 - 9 * (button_height + button_spacing), button_width, button_height)
hit_button = pygame.Rect(1700, 1000 - 3 * (button_height + button_spacing), button_width, button_height)
stand_button = pygame.Rect(1700, 1000 - 2 * (button_height + button_spacing), button_width, button_height)
double_down_button = pygame.Rect(1700, 1000 - (button_height + button_spacing), button_width, button_height)
split_button = pygame.Rect(1700, 1000, button_width, button_height)

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green_cloth = (0, 153, 76)
yellow = (255, 255, 0)

# Boolean to track whether the cards have been dealt
cards_dealt = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Check for button press events
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the Deal button is clicked
            if deal_button.collidepoint(mouse_x, mouse_y):
                # Deal cards only if not already dealt
                if not cards_dealt:
                    # Draw the dealer's hand
                    dealer.drawHand()

                    if dealer.blackjack:
                        cards_dealt = False
                        player.bet = 0
                        player.money -= player.bet

                    # Draw the player's hand
                    player.drawHand()

                    # Update the flag to indicate that cards have been dealt
                    cards_dealt = True

            if hit_button.collidepoint(mouse_x, mouse_y):
                if cards_dealt:
                    player.drawCard()
                    if player.bust:
                        cards_dealt = False
                        player.bet = 0
                        player.money -= player.bet

            if stand_button.collidepoint(mouse_x, mouse_y):
                if cards_dealt:
                    dealer.stand = True
                    dealer.show(screen)
                    pygame.display.flip()
                    pygame.time.delay(1000)    

    if dealer.stand:
        if dealer.hand.get_value() < 17:
            dealer.drawCard()
        else:
            if dealer.bust or player.hand.get_value() > dealer.hand.get_value():
                player.money += 2*player.bet
            elif player.hand.get_value() == dealer.hand.get_value():
                player.money += player.bet
            else:
                player.money -= player.bet
                
            cards_dealt = False
            player.bet = 0


    # Clear the screen
    screen.fill(green_cloth)

    # Render dealer's cards
    dealer.show(screen)

    # Render player's cards
    player.show(screen)

    # Draw buttons
    pygame.draw.rect(screen, white, deal_button)
    pygame.draw.rect(screen, white, hit_button)
    pygame.draw.rect(screen, white, stand_button)
    pygame.draw.rect(screen, white, double_down_button)
    pygame.draw.rect(screen, white, split_button)

    # Button labels
    deal_text = font.render("Deal", True, black)
    hit_text = font.render("Hit", True, black)
    stand_text = font.render("Stand", True, black)
    double_down_text = font.render("Double Down", True, black)
    split_text = font.render("Split", True, black)

    screen.blit(deal_text, (deal_button.x + 10, deal_button.y + 10))
    screen.blit(hit_text, (hit_button.x + 10, hit_button.y + 10))
    screen.blit(stand_text, (stand_button.x + 10, stand_button.y + 10))
    screen.blit(double_down_text, (double_down_button.x + 10, double_down_button.y + 10))
    screen.blit(split_text, (split_button.x + 10, split_button.y + 10))

    pygame.display.flip()
    pygame.time.delay(1000)
