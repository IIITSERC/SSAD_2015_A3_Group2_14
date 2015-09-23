import pygame, random

#Importing Modules

from constants import *
from make import *
from Person import *
from FireBalls import *
from Board import *
from Game import *

def main():
	pygame.init()

	size = [SC_WIDTH, SC_HEIGHT]
	screen = pygame.display.set_mode(size)
	font = pygame.font.Font(None, 25)
	pygame.display.set_caption('Donkey Kong')

	game = Game()
	game.gameLoop(screen, font)


if __name__ == "__main__":
	main()
