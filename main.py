import pygame
from constants import *
pygame.init()

def main():
    print("Starting asteroids!")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    game_status = True
    
    
    while game_status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_status = False
        
        #Refeshes Background color       
        screen.fill(BACKGROUND_COLOR)
        pygame.display.update()
        #sets fps to 60
        dt = clock.tick(60) / 1000    

    
    
    
    
if __name__ == "__main__":
    main()