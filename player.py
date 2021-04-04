import variables
import pygame


class Player:
    def __init__(self, x=450, y=450, color=variables.WHITE):
        self.x = x
        self.y = y
        self.color = color
        self.up_is_pressed = False
        self.down_is_pressed = False
        self.left_is_pressed = False
        self.right_is_pressed = False
        # self.name = name

    def draw_player(self):
        pygame.draw.circle(variables.DISPLAYSURF, self.color, (self.x, self.y), variables.PLAYERSIZE)

    def set_location(self, x, y):
        self.x = x
        self.y = y
        print(self.x, self.y)
        return self.x, self.y

    def get_location(self):
        return self.x, self.y

    def move_player(self):
        if self.up_is_pressed:
            self.y += -variables.MOVESPEED
        if self.down_is_pressed:
            self.y += variables.MOVESPEED
        if self.left_is_pressed:
            self.x += -variables.MOVESPEED
        if self.right_is_pressed:
            self.x += variables.MOVESPEED


def create_player_list():
    num_players = int(input('number of players'))
    player_list = list(range(1, (num_players + 1)))
    print(player_list)

    dicts = {}
    keys = range(0, num_players)
    print(keys)
    values = ["Hi", "I", "am", "John"]
    print(values)
    for i in keys:
        dicts[i + 1] = values[i]
    print(dicts)

    # player_names = for num in player_list:
    #                     list()
