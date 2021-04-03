import pygame
import sys
import player
import variables


def run_game():
    p3 = player.Player(x=200, y=200, color=variables.RED)
    p3.draw_player()
    p3.set_location(1, 1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # print(event.key)
                if event.key == pygame.K_w:
                    p3.set_location(0, -10)
                if event.key == pygame.K_s:
                    p3.set_location(0, 10)
                if event.key == pygame.K_d:
                    p3.set_location(10, 0)
                if event.key == pygame.K_a:
                    p3.set_location(-10, 0)
        variables.DISPLAYSURF.fill(variables.BGCOLOR)
        p3.draw_player()
        pygame.display.update()
