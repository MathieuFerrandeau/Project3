from constants import *
from random import *


class Maze:
	"""Définition du labyrinthe et des items"""
	def __init__(self, maze_map, items):
		self.maze_map = maze_map
		self.items = {}
		for item in items:
			self.items[item] = Item(self.random_position())

	def free_way(self, pos_x, pos_y, direction):
		"""teste si le chemin est libre"""
		return (direction == LEFT and pos_x > 0 and
				self.maze_map[pos_y][pos_x-1] != "#" or
				direction == RIGHT and pos_x < (MAP_LENGTH - 1) and
				self.maze_map[pos_y][pos_x+1] != "#" or
				direction == UP and pos_y > 0 and
				self.maze_map[pos_y-1][pos_x] != "#" or
				direction == DOWN and pos_y < (MAP_HEIGHT - 1) and
				self.maze_map[pos_y+1][pos_x] != "#")

	def start(self):
		"""place tous les items aléatoirement dans le labyrinthe"""
		for item in self.items:
			self.maze_map[self.items[item].pos_y][self.items[item].pos_x] = " "
			self.items[item] = Item(self.random_position())

	def random_position(self):
		"""Choisit une position aléatoire pour placer un item"""
		pos_x = 0
		pos_y = 0
		while self.maze_map[pos_y][pos_x] != " ":
			pos_x = randint(0, (MAP_LENGTH - 1))
			pos_y = randint(0, (MAP_HEIGHT - 1))
		self.maze_map[pos_y][pos_x] = "i"
		return (pos_x, pos_y)

class Item:
	"""decrit un item"""
	def __init__(self, position):
		self.pos_x = position[0]
		self.pos_y = position[1]
		self.show = True

	@property
	def pixel_position(self):
		"""la position en pixel des items"""
		return [self.pos_x * TILE_SIZE, self.pos_y * TILE_SIZE]


class Hero:
	"""Définition du hero"""
	def __init__(self, game, items):
		self.game = game
		self.beginning()

	def move(self, direction):
		"""Deplace mac gyver dans la direction choisie"""
		if self.game.free_way(self.pos_x, self.pos_y, direction):
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

	@property
	def status(self):
		"""Statut de MG si il a perdu, gagné ou dans le labyrinthe"""
		if self.game.maze_map[self.pos_y][self.pos_x] == "g":
			return WIN
		


	