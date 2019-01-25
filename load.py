"""Charge les configurations du fichier json et 2 fonctions qui permette de traiter des fichiers"""
import json
import pygame


class Images:
    """charge les images a partir des paramètres de config"""
    def __init__(self, config):
        self.mac_gyver = self.load_image(config["mac_gyver"])
        self.guardian = self.load_image(config["guardian"])
        self.wall = self.load_image(config["wall"])
        self.floor = self.load_image(config["floor"])
        self.items = {}
        for item in config["items"]:
            self.items[item] = self.load_image(config["items"][item]["img"])

    @classmethod
    def load_image(cls, filename):
        """Gère la transparence"""
        return pygame.image.load(filename).convert_alpha()


def map_from_file(filename):
    """Charge le labyrinthe a partir du fichier donnée en paramètre"""
    with open(filename, "r") as map_file:
        maze_map = [list(line) for line in map_file]
    return maze_map

def config_from_file(filename):
    """Charge les config du fichier json donné en paramètre"""
    with open(filename) as data:
        return json.load(data)
