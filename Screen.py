import pygame
import time
from Card import Card
from Deck import Deck
from Hand import Hand
from Dealer import Dealer
from Player import Player
from NeuralNetwork import NeuralNetwork  
from Population import Population
from GameLogic import GameLogic

TIME = 850  # Time in milliseconds to delay between actions
clock = pygame.time.Clock()

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080))  # Adjust the size as needed
pygame.display.set_caption("Blackjack Game")

# Create game objects
deck = Deck()
dealer = Dealer(deck)
player = Player("Player", deck)
gl = GameLogic(deck, dealer, player)

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

# Additional buttons for Money, Bet, Insurance, and Train
money_button = pygame.Rect(100, 1000 - 2 * (button_height + button_spacing), button_width, button_height)
bet_button = pygame.Rect(100, 1000 - (button_height + button_spacing), button_width, button_height)
insurance_button = pygame.Rect(100, 1000, button_width, button_height)
train_button = pygame.Rect(10, 10, 100, 40)  # Train button position and size

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green_cloth = (0, 153, 76)

# Boolean to track whether the cards have been dealt
cards_dealt = False

# Text input
bet_text = ""
bet_active = True  # Flag to track if the text input for bet is active

# Generation
current_generation = 1

# Train button state
train_button_active = False


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Check for button press events
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the Train button is clicked
            if train_button.collidepoint(mouse_x, mouse_y) and not cards_dealt:
                train_button_active = not train_button_active
                if train_button_active:
                    # Code to start training
                    print("Training started...")
                    # You should implement your training logic here
                    # Update the neural network weights based on the game outcomes
                    # After training, set train_button_active to False
                    train_button_active = False
                    print("Training completed.")


            # Check if the Deal button is clicked
            if deal_button.collidepoint(mouse_x, mouse_y):
                # Deal cards only if not already dealt
                if not cards_dealt and not bet_active and bet_text != "":
                    gl.deal()
                    # Update the flag to indicate that cards have been dealt
                    cards_dealt = True
                    dealer.hidden = True  # Hide the dealer's second card

            # Check if the Hit button is clicked
            if hit_button.collidepoint(mouse_x, mouse_y):
                # Draw a card only if cards have been dealt
                if cards_dealt:
                   gl.hit()
                
            # Check if the Stand button is clicked
            if stand_button.collidepoint(mouse_x, mouse_y):
                # Move to the next hand only if cards have been dealt
                if cards_dealt:
                    gl.stand()

            # Check if the Double Down button is clicked
            if double_down_button.collidepoint(mouse_x, mouse_y):
                # Double the bet and draw a card only if cards have been dealt and the player has enough money
                if cards_dealt:
                    gl.double_down()

            # Check if the Insurance button is clicked
            if insurance_button.collidepoint(mouse_x, mouse_y):
                # Pay insurance only if the dealer reaveled card is an Ace and the player has enough money
                if not player.insurance and cards_dealt and dealer.hand.cards[1].rank == "Ace" and player.money >= player.get_bet() / 2:
                    player.money -= player.get_bet() / 2
                    player.insurance = True

            # Check if the Split button is clicked
            if split_button.collidepoint(mouse_x, mouse_y):
                # Split the hand only if he has two cards of the same rank and the player has enough money
                    gl.split()

        # Check for text input events while the Bet button is active
        if event.type == pygame.KEYDOWN and bet_active:
            if event.key == pygame.K_RETURN:
                bet_amount = int(bet_text)
                if bet_amount > 0 and bet_amount <= player.money:
                    player.set_bet(bet_amount)
                    bet_active = False  # Deactivate text input after pressing Enter
            elif event.key == pygame.K_BACKSPACE:
                bet_text = bet_text[:-1]
            # Only allow numbers to be entered
            elif event.unicode.isdigit():
                bet_text += event.unicode

    # Clear the screen
    screen.fill(green_cloth)

    if cards_dealt:
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

    # Draw additional buttons for Money, Bet,Insurance and Train
    pygame.draw.rect(screen, white, money_button)
    pygame.draw.rect(screen, white, bet_button)
    pygame.draw.rect(screen, white, insurance_button)
    pygame.draw.rect(screen, white, train_button)

    # Button labels
    deal_text = font.render("Deal", True, black)
    hit_text = font.render("Hit", True, black)
    stand_text = font.render("Stand", True, black)
    double_down_text = font.render("Double Down", True, black)
    split_text = font.render("Split", True, black)
    money_text = font.render(f"Money: {player.money}", True, black)
    bet_label_text = font.render(f"Bets: {bet_text}", True, black)
    insurance_text = font.render("Insurance", True, black)

    # Draw button labels
    screen.blit(deal_text, (deal_button.x + 10, deal_button.y + 10))
    screen.blit(hit_text, (hit_button.x + 10, hit_button.y + 10))
    screen.blit(stand_text, (stand_button.x + 10, stand_button.y + 10))
    screen.blit(double_down_text, (double_down_button.x + 10, double_down_button.y + 10))
    screen.blit(split_text, (split_button.x + 10, split_button.y + 10))
    screen.blit(money_text, (money_button.x + 10, money_button.y + 10))
    screen.blit(bet_label_text, (bet_button.x + 10, bet_button.y + 10))
    screen.blit(insurance_text, (insurance_button.x + 10, insurance_button.y + 10))

    if train_button_active:
          generation_label_text = font.render(f"Generation: {current_generation}", True, black)
          screen.blit(generation_label_text, (10, 10)) 
    else:
        train_text = font.render("Train", True, black)
        screen.blit(train_text, (train_button.x + 10, train_button.y + 10))

    if bet_active:
        # Render blinking cursor when text input is active
        if time.time() % 1 < 0.5:
            pygame.draw.rect(screen, black, (bet_button.x + 10 + font.size(f"Bets: {bet_text}")[0], bet_button.y + 10, 2, 20))
        bet_label_text = font.render(f"Bets: {bet_text}", True, black)

    pygame.display.flip()
    clock.tick(60)

    if cards_dealt:
        # Check if the current hand is over
        if gl.ended:
            cards_dealt = False
            bet_text = ""
            bet_label_text = font.render(f"Bets: ", True, black)
            bet_active = True

        elif player.pointer == -1 and dealer.hidden:
            dealer.hidden = False
        # If there was action on the current hand, delay 
        elif gl.check_for_action():
            pygame.time.delay(2*TIME)
