import pygame
import pygame_menu
import sys

pygame.init()

# Screen and Configuration

screen = pygame.display.set_mode((720,720))
width = screen.get_width()
height = screen.get_height()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.SysFont("Ariel", 40)
main_menu = False



class Button:
    def __init__(self, text_input, pos):
        self.pos = pos
        self.text_input = text_input
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))
        
    def draw(self):
        pygame.draw.rect(screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark gray', self.button, 5, 5)
        txt = font.render(self.text_input, True, "Black")
        screen.blit(txt, (self.pos[0] + 60, self.pos[1] + 7))
        
    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False


def draw_game():
    play_button = Button("Play", (230, 250))
    play_button.draw()
    return play_button.check_clicked()

def options():
    options_button = Button("Options", (230, 300))
    options_button.draw()
    return options_button.check_clicked()
    

def draw_menu():
    pygame.draw.rect(screen, "black", [100, 100, 300, 300])
    
    menu_btn = Button("Main Menu", (120, 350))
    menu_btn.draw()
    return not menu_btn.check_clicked()

while True:
    background = pygame.image.load("images/background.jpeg")
    screen.blit(background, (0,0))
    
    
    if main_menu:
        main_menu = draw_menu()
    else:
        main_menu = draw_game()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        
        
    pygame.display.update()
    timer.tick(fps)