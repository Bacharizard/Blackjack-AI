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

# Additional buttons for Money, Bet, Insurance, and Test/Stop
money_button = pygame.Rect(100, 1000 - 2 * (button_height + button_spacing), button_width, button_height)
bet_button = pygame.Rect(100, 1000 - (button_height + button_spacing), button_width, button_height)
insurance_button = pygame.Rect(100, 1000, button_width, button_height)
minus_button = pygame.Rect(40,50,40,40)
plus_button = pygame.Rect(90,50,40,40)
test_stop_button = pygame.Rect(35, 100, 100, 40)  # Test/Stop button position and size

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green_cloth = (0, 153, 76)
red = (255, 0, 0)
green = (0, 255, 0)

# Text input
bet_text = ""
bet_active = True  # Flag to track if the text input for bet is active

# Generation
current_generation = 1

# Test/Stop button state
test_stop_button_active = False

def draw_buttons():
    # Draw buttons
    pygame.draw.rect(screen, white, deal_button)
    pygame.draw.rect(screen, white, hit_button)
    pygame.draw.rect(screen, white, stand_button)
    pygame.draw.rect(screen, white, double_down_button)
    pygame.draw.rect(screen, white, split_button)
    pygame.draw.rect(screen, white, money_button)
    pygame.draw.rect(screen, white, bet_button)
    pygame.draw.rect(screen, white, insurance_button)
    pygame.draw.rect(screen, black, minus_button)
    pygame.draw.rect(screen, black, plus_button)
    pygame.draw.rect(screen, black, test_stop_button)

    # Button labels
    deal_text = font.render("Deal", True, black)
    hit_text = font.render("Hit", True, black)
    stand_text = font.render("Stand", True, black)
    double_down_text = font.render("Double Down", True, black)
    split_text = font.render("Split", True, black)
    money_text = font.render(f"Money: {tester.money if test_stop_button_active else player.money}", True, black)
    bet_label_text = font.render(f"Bets: {tester.bets if test_stop_button_active else bet_text}", True, black)
    insurance_text = font.render("Insurance", True, black)
    generation_label_text = font.render(f"Generation: {current_generation}", True, black)
    minus_label_text = font.render("-", True, red)
    plus_label_text = font.render("+", True, green)

    if test_stop_button_active:
        test_stop_text = font.render("Stop", True, red)
    else:
        test_stop_text = font.render("Test", True, green)

    # Draw button labels
    screen.blit(deal_text, (deal_button.x + 10, deal_button.y + 10))
    screen.blit(hit_text, (hit_button.x + 10, hit_button.y + 10))
    screen.blit(stand_text, (stand_button.x + 10, stand_button.y + 10))
    screen.blit(double_down_text, (double_down_button.x + 10, double_down_button.y + 10))
    screen.blit(split_text, (split_button.x + 10, split_button.y + 10))
    screen.blit(money_text, (money_button.x + 10, money_button.y + 10))
    screen.blit(bet_label_text, (bet_button.x + 10, bet_button.y + 10))
    screen.blit(insurance_text, (insurance_button.x + 10, insurance_button.y + 10))
    screen.blit(generation_label_text, (10, 10)) 
    screen.blit(test_stop_text, (test_stop_button.x + 10, test_stop_button.y + 10))
    screen.blit(minus_label_text, (minus_button.x + 16, minus_button.y + 7))
    screen.blit(plus_label_text, (plus_button.x + 12, plus_button.y + 5))


    if bet_active and not test_stop_button_active:
        # Render blinking cursor when text input is active
        if time.time() % 1 < 0.5:
            pygame.draw.rect(screen, black, (bet_button.x + 10 + font.size(f"Bets: {bet_text}")[0], bet_button.y + 10, 2, 20))
        bet_label_text = font.render(f"Bets: {bet_text}", True, black)

# Create game objects
deck = Deck()
dealer = Dealer(deck)
player = Player(deck)
gl = GameLogic(deck, dealer, player)

# Create population
pop = Population()
best_agents = []
pop.calculate_fitness()
best_agents.append(pop.best_agent)


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        # Check for button press events
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the Minus button is clicked
            if minus_button.collidepoint(mouse_x, mouse_y) and not test_stop_button_active:
                 if current_generation > 1:
                    current_generation -= 1
            
            # Check if the Plus button is clicked
            if plus_button.collidepoint(mouse_x, mouse_y) and not test_stop_button_active:
                if current_generation == len(best_agents):
                    pop.next_gen()
                    best_agents.append(pop.best_agent)
                current_generation += 1

            # Check if the Test/Stop button is clicked
            if test_stop_button.collidepoint(mouse_x, mouse_y):
                if test_stop_button_active:
                    deck = Deck()
                    dealer = Dealer(deck)
                    player = Player(deck)
                    gl = GameLogic(deck, dealer, player)
                else:
                    tester = best_agents[current_generation-1]
                    tester.hands_played = 0
                    tester.money = 1000
                    gl = tester.gl
                test_stop_button_active = not test_stop_button_active
                
            else:
                # Check if the Deal button is clicked
                if deal_button.collidepoint(mouse_x, mouse_y) and gl.ended and not bet_active and bet_text != "":
                        gl.deal()

                # Check if the Hit button is clicked
                if hit_button.collidepoint(mouse_x, mouse_y) and not gl.ended:
                        gl.hit()
                    
                # Check if the Stand button is clicked
                if stand_button.collidepoint(mouse_x, mouse_y) and not gl.ended:
                        gl.stand()

                # Check if the Double Down button is clicked
                if double_down_button.collidepoint(mouse_x, mouse_y) and not gl.ended:
                        gl.double_down()

                # Check if the Insurance button is clicked
                if insurance_button.collidepoint(mouse_x, mouse_y) and not gl.ended:
                        gl.insurance()

                # Check if the Split button is clicked
                if split_button.collidepoint(mouse_x, mouse_y) and not gl.ended:
                        gl.split()


        # Check for text input events while the Bet button is active
        if event.type == pygame.KEYDOWN and bet_active and not test_stop_button_active:
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

    if test_stop_button_active:
        if gl.ended:
            if tester.money>= 1:
                tester.decide_bet()
                gl.deal()
                tester.should_insure()
        else:
            if gl.can_play():
                tester.action()

    # Clear the screen
    screen.fill(green_cloth)

    if not gl.ended:
        # Render dealer's cards
        gl.dealer.show(screen)
        # Render player's cards
        gl.player.show(screen)
    
    draw_buttons()
    pygame.display.flip() 
    clock.tick(60)
    pygame.time.delay(TIME)

    # If there was action on the current hand, delay 
    if gl.check_for_action():
        if gl.ended:
            bet_text = ""
            bet_label_text = font.render(f"Bets: ", True, black)
            bet_active = True
