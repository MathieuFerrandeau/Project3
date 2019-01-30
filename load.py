"""Load json file configurations, map and images"""
import json
import pygame


class Images:
    """Load images from given configurations parameters"""
    def __init__(self, config):
        self.mac_gyver = self.load_image(config["mac_gyver"])
        self.guardian = self.load_image(config["guardian"])
        self.wall = self.load_image(config["wall"])
        self.floor = self.load_image(config["floor"])
        self.items = {}
        for item in config["items"]:
            try:
                self.items[item] = self.load_image(config["items"][item]["img"])
            except KeyError:
                print("Image not found from: \"" + item + "\"")
                exit()

    @classmethod
    def load_image(cls, filename):
        """Manages the transparency of images"""
        try:
            return pygame.image.load(filename).convert_alpha()
        except FileNotFoundError:
            print("Couldn't open the image: \"" + filename + "\"")
            exit()

def map_from_file(filename):
    """Load the labyrinth from the given file"""
    try:
        with open(filename, "r") as map_file:
            maze_map = [list(line) for line in map_file]
        return maze_map
    except FileNotFoundError:
        print("Couldn't open map file: \"" + filename + "\"")
        exit()

def config_from_file(filename):
    """Load the config of the given json file"""
    try:
        with open(filename) as data:
            return json.load(data)
    except FileNotFoundError:
        print("Couldn't open config file: \"" + filename + "\"")
        exit()
