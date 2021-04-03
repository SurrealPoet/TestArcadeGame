import variables
import pygame


class Player:
    def __init__(self, x=450, y=450, color=variables.WHITE):
        self.x = x
        self.y = y
        self.color = color
        # self.name = name

    # def set_player(self, x, y, color):
    #     pygame.draw.circle(DISPLAYSURF, color, (x, y), PLAYERSIZE)

    def draw_player(self):
        pygame.draw.circle(variables.DISPLAYSURF, self.color, (self.x, self.y), variables.PLAYERSIZE)

    def set_location(self, x, y):
        self.x += x
        self.y += y
        print(self.x, self.y)
        return self.x, self.y

    def get_location(self):
        pass
        # return self.x, self.y

