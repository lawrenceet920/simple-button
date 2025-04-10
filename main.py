# Ethan Lawrence 
# Apr 10 2025
# Simple Button

import pygame
import sys
import config

# Generic Functions
def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen
def handle_events(button):
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            return False
        if events.type == pygame.K_ESCAPE:
            return False
        if events.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(events.pos):
                return False
            
    return True
def main():
    screen = init_game()
    clock = pygame.time.Clock()
    running = True
    # On Startup
    font = pygame.font.Font('PixelifySans-Bold.ttf', 40)
    surf = font.render('Quit', True, config.GREEN)

    button_quit = {
        'length' : 200,
        'height' : 60,
        'x' : 300,
        'y' : 125
    }
    button = pygame.Rect(button_quit['x'], button_quit['y'], button_quit['length'], button_quit['height'])
    surf_rect = surf.get_rect()
    surf_rect.center = button.center
    while running:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        running = handle_events(button)
        screen.fill(config.WHITE)
        # While Running
        if button.collidepoint(mouse_x, mouse_y):
            button_quit['color'] = (180, 180, 180)
        else:
            button_quit['color'] = (110, 110, 110)
        
        pygame.draw.rect(screen, button_quit['color'], button)
        screen.blit(surf, surf_rect)
        # Limit clock to FPS & Update Screen
        pygame.display.flip()
        clock.tick(config.FPS)
    pygame.quit()
    sys.exit()

# Other Functions
    
# Startup
if __name__ == '__main__':
    main()