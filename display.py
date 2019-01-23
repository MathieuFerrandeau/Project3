import pygame
from constants import *

def draw(game, mac_gyver, images, window):
	"""Dessine le jeu"""
	num_line = 0
	for line in game.maze_map:
		num_column = 0 
		for case in line:
			img_pos = [num_column * TILE_SIZE, num_line * TILE_SIZE]

			if case == "#":
				window.blit(images.wall, img_pos)
			else:
				window.blit(images.floor, img_pos)
			if case == "g":
				window.blit(images.guardian, img_pos)
			
			window.blit(images.mac_gyver, mac_gyver.pixel_position)
			num_column += 1
		num_line += 1

	pygame.display.flip()
