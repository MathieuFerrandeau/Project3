#! /usr/bin/env python3
# coding: utf-8
"""Main game file"""

import pygame
from pygame.locals import *
from constants import *


def main():
	"""Main Function"""
	pygame.init()
	window = pygame.display.set_mode((MAP_LENGHT * TILE_SIZE, MAP HEIGHT * TILE_SIZE))
	
	"""config = load.config_from_file("config.json")
				images= load.Images(config)
				lvl = game.Lvl(load.map_from_file("maze.xsb"), config["items"])
				mac_gyver =game.character"""

if __name__ == "__main__":
	main()