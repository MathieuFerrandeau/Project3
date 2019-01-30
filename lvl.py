"""Defined maze classes, MG and items"""
from random import randint
from constants import * #import all constants


class Maze:
    """Definition of labyrinth and items"""
    def __init__(self, maze_map, items):
        self.maze_map = maze_map
        self.items = {}
        for item in items:
            self.items[item] = Item(self.random_position())

    def free_way(self, pos_x, pos_y, direction):
        """Test if the path is free"""
        return (direction == LEFT and pos_x > 0 and
                self.maze_map[pos_y][pos_x-1] != "#" or
                direction == RIGHT and pos_x < (MAP_LENGTH - 1) and
                self.maze_map[pos_y][pos_x+1] != "#" or
                direction == UP and pos_y > 0 and
                self.maze_map[pos_y-1][pos_x] != "#" or
                direction == DOWN and pos_y < (MAP_HEIGHT - 1) and
                self.maze_map[pos_y+1][pos_x] != "#")

    def start(self):
        """Place all the items randomly in the labyrinth"""
        for item in self.items:
            self.maze_map[self.items[item].pos_y][self.items[item].pos_x] = " "
            self.items[item] = Item(self.random_position())

    def random_position(self):
        """Choose a random position to place an item"""
        pos_x = 0
        pos_y = 0
        while self.maze_map[pos_y][pos_x] != " ":
            pos_x = randint(0, (MAP_LENGTH - 1))
            pos_y = randint(0, (MAP_HEIGHT - 1))
        self.maze_map[pos_y][pos_x] = "i"
        return (pos_x, pos_y)


class Item:
    """Describes an item"""
    def __init__(self, position):
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.show = True

    @property
    def pixel_position(self):
        """The pixel position of the items"""
        return [self.pos_x * TILE_SIZE, self.pos_y * TILE_SIZE]


class Hero:
    """Definition of MG"""
    def __init__(self, game, items):
        self.game = game
        self.beginning()
        self.item_msg = {}
        for item in items:
            self.item_msg[item] = items[item].get("msg")

    def move(self, direction):
        """Move MG in the chosen direction and call the method to pick up objects"""
        if self.game.free_way(self.pos_x, self.pos_y, direction):
            if direction == LEFT:
                self.pos_x -= 1
            elif direction == RIGHT:
                self.pos_x += 1
            elif direction == UP:
                self.pos_y -= 1
            elif direction == DOWN:
                self.pos_y += 1
            self.gather()

    def beginning(self):
        """Place Mac Guyver in its initial position and put the item counter at 0"""
        self.pos_y, self.pos_x = self.start_position(self.game)
        self.items_count = 0

    @classmethod
    def start_position(cls, game):
        """Initializes the position of MG"""
        num_line = 0
        for line in game.maze_map:
            num_column = 0
            for case in line:
                if case == "m":
                    return (num_line, num_column)
                num_column += 1
            num_line += 1

    def gather(self):
        """Collect objects"""
        for item in self.game.items:
            if (self.game.items[item].pos_x == self.pos_x and
                    self.game.items[item].pos_y == self.pos_y and
                    self.game.items[item].show):
                self.items_count += 1
                self.game.items[item].show = False
                if self.item_msg[item] is not None:
                    print(self.item_msg[item])
                if self.items_count == 3:
                    print("Now I can make a syringe, it's time to get out of here !")

    @property
    def pixel_position(self):
        """The pixel position of MG"""
        return [self.pos_x * TILE_SIZE, self.pos_y * TILE_SIZE]

    @property
    def state(self):
        """State of MG if he has lost, won or is in the labyrinth"""
        if self.game.maze_map[self.pos_y][self.pos_x] == "g":
            if self.items_count == len(self.game.items):
                return WIN
            return LOST
        return IN_MAZE
