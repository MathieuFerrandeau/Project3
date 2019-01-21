#!/usr/bin/python3
# coding: utf-8

import pygame
from pygame.locals import * # import all pygame constants

import load
import display
from constants import *

def main():
    """Main function"""
    pygame.init()
    window = pygame.display.set_mode((MAP_LENGTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE))

    config = load.config_from_file("config.json")
    images = load.Images(config)
    lvl = load.Maze(load.map_from_file("maze.xsb"))

    display.draw(lvl, images, window)



#BOUCLE INFINIE
    continuer = 1
    while continuer:
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT:
                continuer = 0

                display.draw(lvl, images, window)

if __name__ == "__main__":
	main()