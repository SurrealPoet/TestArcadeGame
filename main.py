# shoot-em type game

import pygame
import sys
import update_screen
import variables


def main():
    pygame.init()
    pygame.display.set_caption('Shoot\'em Game')
    update_screen.run_game()


main()

# how to do font
# font = pygame.font.SysFont('', 28)
# message1 = pygame.font.Font.render(font, 'Player1', True, GREEN)
# DISPLAYSURF.blit(message1, (500, 500))
