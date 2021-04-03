# shoot-em type game

import pygame
import sys

# from player.py import *

FPS = 60
WINDOWWIDTH = 900
WINDOWHEIGHT = 900
PLAYERSIZE = 20
NAVYBLUE = 60, 60, 100
BGCOLOR = NAVYBLUE
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)


class Player:
    def __init__(self, x=450, y=450, color=WHITE):
        self.x = x
        self.y = y
        self.color = color
        # self.name = name

    # def set_player(self, x, y, color):
    #     pygame.draw.circle(DISPLAYSURF, color, (x, y), PLAYERSIZE)

    def draw_player(self):
        pygame.draw.circle(DISPLAYSURF, self.color, (self.x, self.y), PLAYERSIZE)

    def set_location(self, x, y):
        self.x += x
        self.y += y
        print(self.x, self.y)
        return self.x, self.y

    def get_location(self):
        pass
        # return self.x, self.y


def run_game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_w:
                    p3.set_location(0, 1)
                # if event.type == pygame.KEYUP:
                #     if event.key == pygame.K_w:
                #         p1.y += -1
                #         print(p1.y)

        pygame.display.update()


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    pygame.key.set_repeat(100)
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    DISPLAYSURF.fill(BGCOLOR)
    pygame.display.set_caption('Shoot\'em Game')
    mousex = 0
    mousey = 0
    # p1 = Player()
    # p1.set_player(450, 450, RED)
    # p2 = Player()
    # p2.set_player(200, 200, GREEN)
    # p1.get_location()
    p3 = Player(x=200, y=200, color=RED)
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
        DISPLAYSURF.fill(BGCOLOR)
        p3.draw_player()
        pygame.display.update()

    # run_game()


main()

# how to do font
# font = pygame.font.SysFont('', 28)
# message1 = pygame.font.Font.render(font, 'Player1', True, GREEN)
# DISPLAYSURF.blit(message1, (500, 500))
