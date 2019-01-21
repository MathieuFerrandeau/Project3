import json
import pygame


class Images:

	def __init__(self, config):
		self.mac_gyver = self.load_image(config["mac_gyver"])
		self.guardian = self.load_image(config["guardian"])
		self.wall = self.load_image(config["wall"])
		self.floor = self.load_image(config["floor"])

	@classmethod
	def load_image(cls, filename):
		return pygame.image.load(filename).convert_alpha()

def config_from_file(filename):
	with open(filename) as data:
		return json.load(data)

def map_from_file(filename):
	with open(filename, "r") as map_file:
		maze_map = [list(line) for line in map_file]
	return maze_map


class Maze:

	def __init__(self, maze_map):
		self.maze_map = maze_map