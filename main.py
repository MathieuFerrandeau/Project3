#!/usr/bin/python3
# coding: utf-8
"""Main game file"""

# pylint: disable=W0401, E0602, E1101, R0912, W0614

import pygame
from pygame.locals import * # import pygame constants

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
    game = lvl.Maze(load.map_from_file("maze.xsb"), config["items"])
    mac_gyver = lvl.Hero(game, config["items"])


    display.draw(game, mac_gyver, images, window)

    in_game = True
    stop_game = False

# pylint: disable=W0401, E0602

    # Infinite loop
    print(config["start_msg"])
    while in_game:
        for event in pygame.event.get():	# Waiting for events
            if event.type == QUIT:
                in_game = False
            if event.type == KEYDOWN:
                if not stop_game:
                    if event.key == K_LEFT:
                        mac_gyver.move(LEFT)
                    elif event.key == K_RIGHT:
                        mac_gyver.move(RIGHT)
                    elif event.key == K_UP:
                        mac_gyver.move(UP)
                    elif event.key == K_DOWN:
                        mac_gyver.move(DOWN)

                    if mac_gyver.state == WIN:
                        print(config["win_msg"])
                    elif mac_gyver.state == LOST:
                        print(config["lost_msg"])

                    if mac_gyver.state != IN_MAZE:
                        print("\nAn other party (y/n) ?")
                        stop_game = True
                else:
                    if event.key == K_y:
                        print("\nThis time it's the right one !")
                        mac_gyver.beginning()
                        game.start()
                        stop_game = False
                    elif event.key == K_n:
                        in_game = False



            display.draw(game, mac_gyver, images, window)

if __name__ == "__main__":
    main()
