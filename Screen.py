import pygame
from Card import Card
from Deck import Deck
from Hand import Hand
from Dealer import Dealer
from Player import Player

TIME = 850  # Time in milliseconds to delay between actions

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
deal_button = pygame.Rect(1650, 1000 - 9 * (button_height + button_spacing), button_width, button_height)
hit_button = pygame.Rect(1650, 1000 - 3 * (button_height + button_spacing), button_width, button_height)
stand_button = pygame.Rect(1650, 1000 - 2 * (button_height + button_spacing), button_width, button_height)
double_down_button = pygame.Rect(1650, 1000 - (button_height + button_spacing), button_width, button_height)
split_button = pygame.Rect(1650, 1000, button_width, button_height)

# Additional buttons for Money, Bet, and Insurance
money_button = pygame.Rect(100, 1000 - 2 * (button_height + button_spacing), button_width, button_height)
bet_button = pygame.Rect(100, 1000 - (button_height + button_spacing), button_width, button_height)
insurance_button = pygame.Rect(100, 1000, button_width, button_height)

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
                    dealer.hidden = True
                    # Draw the dealer's hand
                    dealer.draw_hand()

                    # Draw the player's hand
                    player.draw_hand()

                    # Update the flag to indicate that cards have been dealt
                    cards_dealt = True

            # Check if the Hit button is clicked
            if hit_button.collidepoint(mouse_x, mouse_y):
                # Draw a card only if cards have been dealt
                if cards_dealt:
                    player.draw_card()
                    # If the player busts or has a blackjack, move to the next hand
                    if player.getHand().bust or player.getHand().blackjack:
                        player.pointer -= 1

            # Check if the Stand button is clicked
            if stand_button.collidepoint(mouse_x, mouse_y):
                # Move to the next hand only if cards have been dealt
                if cards_dealt:
                    player.pointer -= 1

            # Check if the Double Down button is clicked
            if double_down_button.collidepoint(mouse_x, mouse_y):
                # Double the bet and draw a card only if cards have been dealt and the player has enough money
                if cards_dealt and len(player.getHand().cards) == 2 and player.money >= player.getBet():
                    player.money -= player.getBet()
                    player.setBet(2 * player.getBet())
                    player.draw_card()
                    dd = True
                    player.pointer -= 1

            # Check if the Split button is clicked
            if split_button.collidepoint(mouse_x, mouse_y):
                # Split the hand only if cards have been dealt and the player has enough money
                if cards_dealt and len(player.getHand().cards) == 2 and player.getHand().cards[0].rank == player.getHand().cards[1].rank:
                    player.split()


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

    # Draw additional buttons for Money, Bet, and Insurance
    pygame.draw.rect(screen, white, money_button)
    pygame.draw.rect(screen, white, bet_button)
    pygame.draw.rect(screen, white, insurance_button)

    # Right Button labels
    deal_text = font.render("Deal", True, black)
    hit_text = font.render("Hit", True, black)
    stand_text = font.render("Stand", True, black)
    double_down_text = font.render("Double Down", True, black)
    split_text = font.render("Split", True, black)

    # Left Button labels
    money_text = font.render(f"Money: {player.money}", True, black)
    bet_text = font.render(f"Bet: {player.bets}", True, black)
    insurance_text = font.render("Insurance", True, black)

    # Draw right button labels
    screen.blit(deal_text, (deal_button.x + 10, deal_button.y + 10))
    screen.blit(hit_text, (hit_button.x + 10, hit_button.y + 10))
    screen.blit(stand_text, (stand_button.x + 10, stand_button.y + 10))
    screen.blit(double_down_text, (double_down_button.x + 10, double_down_button.y + 10))
    screen.blit(split_text, (split_button.x + 10, split_button.y + 10))

    # Draw left button labels
    screen.blit(money_text, (money_button.x + 10, money_button.y + 10))
    screen.blit(bet_text, (bet_button.x + 10, bet_button.y + 10))
    screen.blit(insurance_text, (insurance_button.x + 10, insurance_button.y + 10))

    pygame.display.flip()
            
    # If has one card in his hand, draw another card (happens after split)        
    if cards_dealt and len(player.getHand().cards) == 1:
        player.draw_card()
        pygame.time.delay(TIME)

    # If the player has no more hands, move to the dealer
    if cards_dealt and player.pointer==-1:
        # Reveal the dealer's hidden card
        if dealer.hidden:
            dealer.hidden = False
        else:
            # Dealer draws cards until he has 17 or more
            if dealer.hand.get_value() < 17 :
                dealer.draw_card()
                pygame.time.delay(TIME)
            # When the dealer has 17 or more, the balance is updated 
            else:
                player.update_balance(dealer)
                cards_dealt = False
