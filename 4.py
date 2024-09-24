import pygame
from pygame.locals import *
import pickle
import os

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Game Menu")

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center = self.rect.center)
        screen.blit(text, text_rect)
        
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
class Game:
    def __init__(self, username):
        self.username = username
        self.level = 1
        self.xp = 0
        self.strength = 50
        self.acceleration = 75
        self.endurance = 35
        self.money = 0
        self.energy = 100
        self.food_hay = 0
        self.food_bran = 0
        self.food_hc = 0
        self.is_in_game_menu = False
        self.feeding_button = FeedingButton(75, 300, 300, 125, "Feed", (0, 128, 0))
        self.feeding_state = "default"
        
    def update(self):
        self.xp = min(self.xp, MAX_XP)
        xp_formula = (self.level / 0.08) ** 2
        
    def save_game(self):
        game_state = {
            "username": self.username,
            "level": self.level,
            "xp": self.xp,
            "strength": self.strength,
            "acceleration": self.acceleration,
            "endurance": self.endurance,
            "money": self.money,
            "energy": self.energy,
            "food_hay": self.food_hay,
            "food_bran": self.food_bran,
            "food_hc": self.food_hc
        }
        
        with open("saved_game.pk1", "wb") as file:
            pickle.dump(game_state, file)
        
    def load_game(self):
        try:
            with open("saved_game.pk1", "rb") as file:
                game_state = pickle.load(file)
            self.username = game_state["username"]
            self.level = game_state["level"]
            self.xp = game_state["xp"]
            self.strength = game_state["strength"]
            self.acceleration = game_state["acceleration"]
            self.endurance = game_state["endurance"]
            self.money = game_state["money"]
            self.energy = game_state["energy"]
            self.food_hay = game_state["food_hay"]
            self.food_bran = game_state["food_bran"]
            self.food_hc = game_state["food_hc"]
            
        except FileNotFoundError:
            print("No saved game found.")
    
    def draw(self):
        xp_bar_width = 254
        xp_bar_height = 20
        xp_bar_x = 10
        xp_bar_y = 10
        pygame.draw.rect(screen, (255,255,255), (xp_bar_x, xp_bar_y, xp_bar_width, xp_bar_height))
        
        filled_up_width = xp_bar_width * (self.xp / MAX_XP)
        
        pygame.draw.rect(screen, (0, 128, 255), (xp_bar_x + 2, xp_bar_y + 2, filled_up_width - 4, xp_bar_height - 4))
        
        
        
        # Username & Player Stats
        font = pygame.font.Font(None, 36)
        username_text = font.render(f"Username: {self.username}", True, (255,255,255))
        
        font = pygame.font.Font(None, 26)
        level_text = font.render(f"Level: {self.level}", True, (255, 255, 255))
        money_text = font.render(f"Money: ${self.money}", True, (255, 255, 255))
        
        screen.blit(username_text, (10, 40))
        screen.blit(level_text, (10, 80))
        screen.blit(money_text, (10, 100))
        
        #  Horse Stats Graph
        energy_bar_width = 140
        energy_bar_heigth = 20
        energy_bar_x = 450
        energy_bar_y = 200
        pygame.draw.rect(screen, (255,255,255), (energy_bar_x, energy_bar_y, energy_bar_width, energy_bar_heigth))
        
        filled_up_width = energy_bar_width * (self.energy / MAX_ENERGY)
        
        pygame.draw.rect(screen, (0, 128, 255), (energy_bar_x + 2, energy_bar_y + 2, filled_up_width - 4, energy_bar_heigth - 4))
        
        strength_bar_width = 140
        strength_bar_height = 20
        strength_bar_x = 450
        strength_bar_y = 50
        pygame.draw.rect(screen, (255,255,255), (strength_bar_x, strength_bar_y, strength_bar_width, strength_bar_height))
        filled_up_width = strength_bar_width * (self.strength / MAX_STRENGTH)
        pygame.draw.rect(screen, (0, 255, 0), (strength_bar_x + 2, strength_bar_y + 2, filled_up_width - 4, strength_bar_height - 4))
        
        acceleration_bar_width = 140
        acceleration_bar_height = 20
        acceleration_bar_x = 450
        acceleration_bar_y = 100
        pygame.draw.rect(screen, (255,255,255), (acceleration_bar_x, acceleration_bar_y, acceleration_bar_width, acceleration_bar_height))
        filled_up_width = acceleration_bar_width * (self.acceleration / MAX_ACCELERATION)
        pygame.draw.rect(screen, (255, 0, 0), (acceleration_bar_x + 2, acceleration_bar_y + 2, filled_up_width - 4, acceleration_bar_height - 4))
        
        endurance_bar_width = 140
        endurance_bar_height = 20
        endurance_bar_x = 450
        endurance_bar_y = 150
        pygame.draw.rect(screen, (255,255,255), (endurance_bar_x, endurance_bar_y, endurance_bar_width, endurance_bar_height))
        filled_up_width = endurance_bar_width * (self.endurance / MAX_ENDURANCE)
        pygame.draw.rect(screen, (0, 0, 255), (endurance_bar_x + 2, endurance_bar_y + 2, filled_up_width - 4, endurance_bar_height - 4))
        
        
        
        # Horse Stats Text
        font = pygame.font.Font(None, 36)
        strength_text = font.render(f"Strength: {game.strength}", True, (255, 255, 255))
        acceleration_text = font.render(f"Acceleration: {game.acceleration}", True, (255, 255, 255))
        endurance_text = font.render(f"Endurance: {game.endurance}", True, (255, 255, 255))
        energy_text = font.render(f"Energy: {self.energy}%", True, (255, 255, 255))
        
        
        screen.blit(strength_text, (600, 50))
        screen.blit(acceleration_text, (600, 100))
        screen.blit(endurance_text, (600, 150))
        screen.blit(energy_text, (600, 200))
        
        
        # Food Text
        font = pygame.font.Font(None, 26)
        hay_text = font.render(f"Hay: {game.food_hay}", True, (255, 255, 255))
        bran_text = font.render(f"Bran: {game.food_bran}", True, (255, 255, 255))
        hc_text = font.render(f"High Calorie: {game.food_hc}", True, (255, 255, 255))
        
        screen.blit(hay_text, (10, 150))
        screen.blit(bran_text, (100, 150))
        screen.blit(hc_text, (190, 150))
        
        # Draw Game Buttons
        self.feeding_button.draw()
        training_button.draw()
        resting_button.draw()
        racing_button.draw()
        
        # Feeding Options
        if self.feeding_button.state == "default":
            self.feeding_button.draw()
        elif self.feeding_button.state == "options":
            feed_hay_button.draw()
            feed_bran_button.draw()
            feed_hc_button.draw()
            
    def feeding_button_is_clicked(self, pos):
        return self.feeding_button_is_clicked(pos)
    
    def change_feeding_state(self, new_state):
        self.feeding_state = new_state
        
        
class InGameMenu:
    def __init__(self):
        self.save_button = Button(300, 200, 200, 50, "Save Game", (0, 128, 255))
        self.quit_button = Button(300, 300, 200, 50, "Quit Game", (128, 0, 0))
        
    def draw(self):
        self.save_button.draw()
        self.quit_button.draw()
    

class FeedingButton:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.state = "default"
        
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255,255,255))
        text_rect = text.get_rect(center = self.rect.center)
        screen.blit(text, text_rect)
    
            
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
    
    

    
play_button = Button(300, 175, 200, 50, "New Game", (0, 128, 0))
load_button = Button(300, 250, 200, 50, "Load Game", (128, 128, 0))
quit_button = Button(300, 325, 200, 50, "Quit", (128, 0, 0))

# Game Buttons
# Food Buttons
feed_hay_button = Button(75, 300, 90, 50, "Hay", (128, 128, 128))
feed_bran_button = Button(175, 300, 90, 50, "Bran", (128, 128, 128))
feed_hc_button = Button(275, 300, 90, 50, "High Calorie", (128, 128, 128))

training_button = Button(425, 300, 300, 125, "Training", (0, 128, 0))
resting_button = Button(75, 450, 300, 125, "Rest", (0, 128, 0))
racing_button = Button(425, 450, 300, 125, "Race", (0, 128, 0))

MAIN_MENU = 0
USER_INPUT = 1
MAIN_GAME = 2
IN_GAME_MENU = 3
FEEDING_BUTTONS = 4
current_state = MAIN_MENU

MAX_XP = 250
MAX_ENERGY = 100
MAX_STRENGTH = 100
MAX_ACCELERATION = 100
MAX_ENDURANCE = 100


running = True
username = ""
game = Game(username)
menu = InGameMenu()

if os.path.exists("saved_game.pk1"):
    load_saved_game = Button(300, 150, 200, 50, "Load Saved Game", (128, 128, 0))
    screen.fill((0, 0, 0))
    load_saved_game.draw()
    pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == MOUSEBUTTONDOWN:
            if load_saved_game.is_clicked(event.pos):
                game.load_game()
                current_state = MAIN_GAME
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game.is_in_game_menu = not game.is_in_game_menu
            
            
        if current_state == MAIN_MENU:
            if event.type == MOUSEBUTTONDOWN:
                if play_button.is_clicked(event.pos):
                    current_state = USER_INPUT
                elif quit_button.is_clicked(event.pos):
                    running = False
                elif load_button.is_clicked(event.pos):
                    game.load_game()
                    current_state =  MAIN_GAME
        elif current_state == USER_INPUT:
            if event.type == KEYDOWN:
                if event.key == K_RETURN:  
                    game = Game(username)
                    current_state = MAIN_GAME
                elif event.key == K_BACKSPACE:
                    username = username[:-1]
                else:
                    if event.unicode:  # Check if the event has a Unicode representation
                        username += event.unicode
        
        if event.type == MOUSEBUTTONDOWN:
            if game.is_in_game_menu:
                if menu.save_button.is_clicked(event.pos):
                    game.save_game()
                    game.is_in_game_menu = False
                if menu.quit_button.is_clicked(event.pos):
                    running = False
                    
            
                    
        
        if not running:
            break

        
    screen.fill((0, 0, 0))
    
    if current_state == MAIN_MENU:
        play_button.draw()
        load_button.draw()
        quit_button.draw()
    elif current_state == USER_INPUT:
        font = pygame.font.Font(None, 36)
        text = font.render("Enter your username: ", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 100))
        screen.blit(text, text_rect)
        
        user_text = font.render(username, True, (255, 255, 255))
        user_rect = user_text.get_rect(center=(400, 200))
        screen.blit(user_text, user_rect)
    elif current_state == MAIN_GAME:
        game.update()
        game.draw()
        
        if game.is_in_game_menu:
            overlay = pygame.Surface((600, 400), SRCALPHA)
            overlay.fill((0, 0, 0, 128))
            screen.blit(overlay, (100, 100))
            menu.draw()
            
        
    pygame.display.flip()
    
pygame.quit()
        