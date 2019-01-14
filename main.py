#! /usr/bin/env python3
# coding: utf-8
"""Main game file"""

import pygame
from pygame.locals import *
from constants import *


def main():
	"""Main Function"""
	pygame.init()
	window = pygame.display.set_mode((MAP_LENGHT * TILE_SIZE, MAP_HEIGHT * TILE_SIZE))
	
	

if __name__ == "__main__":
	main()