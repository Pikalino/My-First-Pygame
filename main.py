import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()  # 1) log each frame

        # 2) allow window close button to work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 3) draw (clear screen)
        screen.fill("black")

        # 4) flip last
        pygame.display.flip()

if __name__ == "__main__":
    main()
import json
import math