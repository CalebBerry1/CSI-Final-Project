from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes

pygame.init()
surface = pygame.display.set_mode((720, 720))

def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)
    
def start_the_game():
    pass

def level_menu():
    main_menu._open(level)

main_menu = pygame_menu.Menu("Welcome!", 720, 720, theme=themes.THEME_SOLARIZED)
main_menu.add.text_input("Name: ", default="username", maxchar=20)
main_menu.add.button("Play", start_the_game)
main_menu.add.button("Levels", level_menu)
main_menu.add.button("Quit", pygame_menu.events.EXIT)

level = pygame_menu.Menu("Select a difficulty", 720, 720, theme=themes.THEME_BLUE)
level.add.selector("Difficulty", [("Hard", 1), ("Easy", 2)], onchange=set_difficulty)

loading = pygame_menu.Menu("Loading", 720, 720, theme=themes.THEME_DARK)
loading.add.progress_bar("Progress", progressbar_id=1, default=0, width=300)
update_loading = pygame.USEREVENT + 0

arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))




while True:
    events = pygame.event.get()
    for event in events:
        if event.type == update_loading:
            progress = loading.get_widget("1")
            progress.set_value(progress.get_value() + 1)
            if progress.get_value() == 100:
                pygame.time.set_timer(update_loading, 0)
        if event.type == pygame.QUIT:
            exit()
            
        if main_menu.is_enabled():
            main_menu.update(events)
            main_menu.draw(surface)
            if (main_menu.get_current().get_selected_widget()):
                arrow.draw(surface, main_menu.get_current().get_selected_widget())
            
        pygame.display.update()