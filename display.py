import pygame
from constants import *

def draw(lvl, images, window):
	num_line = 0
	for line in lvl.maze_map:
		num_column = 0 
		for case in line:
			img_pos = [num_column * TILE_SIZE, num_line * TILE_SIZE]

			if case == "#":
				window.blit(images.wall, img_pos)
			else:
				window.blit(images.floor, img_pos)

			num_column += 1
		num_line += 1

	pygame.display.flip()
