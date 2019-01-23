#!/usr/bin/python3
# coding: utf-8

import pygame
from pygame.locals import * # import all pygame constants

import load
import lvl
import display
from constants import *

def main():
    """Main function"""
    pygame.init()
    window = pygame.display.set_mode((MAP_LENGTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE))

    config = load.config_from_file("config.json")
    images = load.Images(config)
    game = lvl.Maze(load.map_from_file("maze.xsb"))
    mac_gyver = lvl.Hero(game)

    display.draw(game, mac_gyver, images, window)



#BOUCLE INFINIE
    continuer = 1
    while continuer:
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT:
                continuer = 0
            #if event.type == KEYDOWN:
                #if event.key == K_LEFT: 
                    #mac_gyver = 
                #elif event.key == K_RIGHT:
                    #mac_gyver = 
                #elif event.key == K_UP:
                    #mac_gyver = 
                #elif event.key == K_DOWN:
                    #mac_gyver = 

                display.draw(game, mac_gyver, images, window)

if __name__ == "__main__":
	main()