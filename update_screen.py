import pygame
import sys
import player
import variables


def run_game():
    p3 = player.Player(x=200, y=200, color=variables.RED)
    p3.draw_player()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    p3.up_is_pressed = True
                if event.key == pygame.K_s:
                    p3.down_is_pressed = True
                if event.key == pygame.K_a:
                    p3.left_is_pressed = True
                if event.key == pygame.K_d:
                    p3.right_is_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    p3.up_is_pressed = False
                if event.key == pygame.K_s:
                    p3.down_is_pressed = False
                if event.key == pygame.K_a:
                    p3.left_is_pressed = False
                if event.key == pygame.K_d:
                    p3.right_is_pressed = False

        p3.move_player()
        draw_screen(p3)
        pygame.time.Clock().tick(variables.FPS)
        # player.create_player_list()


def draw_screen(name):
    variables.DISPLAYSURF.fill(variables.BGCOLOR)
    name.draw_player()
    pygame.display.update()



