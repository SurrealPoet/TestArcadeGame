# shoot-em type game

import pygame
import sys
import update_screen
import variables


def main():
    pygame.init()
    pygame.key.set_repeat(100)

    variables.DISPLAYSURF.fill(variables.BGCOLOR)
    pygame.display.set_caption('Shoot\'em Game')
    mousex = 0
    mousey = 0
    # p1 = Player()
    # p1.set_player(450, 450, RED)
    # p2 = Player()
    # p2.set_player(200, 200, GREEN)
    # p1.get_location()
    update_screen.run_game()


main()

# how to do font
# font = pygame.font.SysFont('', 28)
# message1 = pygame.font.Font.render(font, 'Player1', True, GREEN)
# DISPLAYSURF.blit(message1, (500, 500))
