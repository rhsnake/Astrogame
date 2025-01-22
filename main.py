import pygame
from constants import *
pygame.init()

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_status = True
    
    while game_status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_status = False
            screen.fill(BACKGROUND_COLOR)
            pygame.display.update()
            
            
    pygame.quit()
    
    
    
    
    
if __name__ == "__main__":
    main()