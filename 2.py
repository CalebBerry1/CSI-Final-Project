import pygame
import sys

pygame.init()

# Screen and configuration
screen = pygame.display.set_mode((720,720))
width = screen.get_width()
height = screen.get_height()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.SysFont("Ariel", 40)
game = False 

# Button
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
        
def main_menu():
    main = True
    while main:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        Button("Quit", center=(250, 500))
        
        pygame.display.update()
        timer.tick()
        
gameExit = False

while not gameExit:
    background = pygame.image.load("images/background.jpeg")
    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    pygame.display.update()
    timer.tick()
        