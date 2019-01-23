from constants import *

class Maze:
	"""Définition du labyrinthe"""
	def __init__(self, maze_map):
		self.maze_map = maze_map

	def free_way(self):
		"""teste si le chemin est libre"""
		pass


class Hero:
	"""Définition du hero"""
	def __init__(self, game):
		self.game = game
		self.beginning()

	def move(self, direction):
		"""Deplace mac gyver dans la direction choisie"""
		if direction == LEFT:
			self.pos_x -= 1
		elif direction == RIGHT:
			self.pos_x += 1
		elif direction == UP:
			self.pos_y -= 1
		elif direction == DOWN:
			self.pos_y += 1

	def beginning(self):
		"""Place Mac Guyver dans sa position initiale"""
		self.pos_y, self.pos_x = self.start_position(self.game)

	@classmethod
	def start_position(cls, game):
		"""initialise la position de Mac Gyver"""
		num_line = 0
		for line in game.maze_map:
			num_column = 0
			for case in line:
				if case == "m":
					return (num_line, num_column)
				num_column += 1
			num_line += 1

	@property
	def pixel_position(self):
		"""La position en pixel de Mac Gyver"""
		return [self.pos_x * TILE_SIZE, self.pos_y * TILE_SIZE]

