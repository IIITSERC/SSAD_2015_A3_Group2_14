import pygame, random

from constants import *
from make import *

class Board():
	def __init__(self):
		self.score = 0
		self.platform_list = pygame.sprite.Group()
		self.coins_list = pygame.sprite.Group()
		self.ladders_list = pygame.sprite.Group()
		self.broken_ladders_list = pygame.sprite.Group()
		self.static_list = pygame.sprite.Group()
		#        [  w,  h,   x,   y],
		# pw = platform_width
		pw = 10 
		gap = 40
		const = 80
		sw = SC_WIDTH
		sh = SC_HEIGHT
		base = sh-pw-gap
		layout = [
				 #borders
				 [sw, pw, 0, base],
				 [sw, pw, 0, gap],
				 [pw, sh-(2*gap)-(2*pw), 0, gap+pw],
				 [pw, sh-(2*gap)-(2*pw), sw-pw, gap+pw],
                 
				 [250, pw, 0, base-(1*(pw+const))],
				 [380, pw, 290, base-(1*(pw+const))],
				 [90, pw, 710, base-(1*(pw+const))],

				 [300, pw, sw-800, base-(2*(pw+const))],
				 [460, pw, sw-460, base-(2*(pw+const))],
		
				 [300, pw, 0, base-(3*(pw+const))],
				 [410, pw, 340, base-(3*(pw+const))],
				 [110, pw, 790, base-(3*(pw+const))],
	
				 [30, pw, sw-900, base-(4*(pw+const))],
				 [830, pw, sw-835, base-(4*(pw+const))],

				 [550, pw, 0, base-(5*(pw+const))],
				 [210, pw, 590, base-(5*(pw+const))],
				 #cage
				 [150, pw, 200, base-(6*(pw+const))],
				 [20, pw, 390, base-(6*(pw+const))],
				 [pw, 60, 200, base-(6*(pw+const))-60],
				 [pw, 60, 400, base-(6*(pw+const))-60],
                 ]
		for dimension in layout:
			block = Make('wall_1.png',dimension[0], dimension[1], dimension[2], dimension[3])
			self.platform_list.add(block)
		
		#make ladders
		#diff = base-pw-const
		h = 90
		w = 40
		extra = 2
		layout = [
				 [w, h, 250, base-(1*(pw+const))-extra],
				 [w, h, 670, base-(1*(pw+const))-extra],

				 [w, h, sw-500, base-(2*(pw+const))-extra],

				 [w, h, 750, base-(3*(pw+const))-extra],
 
				 [w, h, 150, base-(4*(pw+const))-extra],
				
				 [w, h, 550, base-(5*(pw+const))-extra],

				 [w, h, 350, base-(6*(pw+const))-extra],
				 ]
		for lad in layout:
			block = Make('lad.png', lad[0], lad[1], lad[2], lad[3])
			self.ladders_list.add(block)

		layout = [
				 [w, h/3, 300, base-(3*(pw+const))-extra],
				 [w, h/3, 300, base-(3*(pw+const))-extra+2*(h/3)],
				 ]
		fl = 1
		for lad in layout:
			block = Make('lad.png', lad[0], lad[1], lad[2], lad[3])
			if fl:
				self.broken_ladders_list.add(block)
				fl = 0
			else:
				self.ladders_list.add(block)
				fl = 0
		
		#make coins
		all_coins = []
		for j in range(random.randrange(20,30)):
			x = random.randrange(25, sw-25)
			y = random.randrange(150, base-50)
			coin = Make('coin.png', 20, 20, x, y)
			self.coins_list.add(coin)
			coin.fall(self.platform_list)
		
		#make door
		self.door = Make('door.png', 55, 55, 20, sh-105)
		self.static_list.add(self.door)

	#flip
	
	def draw(self, screen):
		screen.fill(BLACK)
		self.platform_list.draw(screen)
		self.ladders_list.draw(screen)
		self.broken_ladders_list.draw(screen)
		self.static_list.draw(screen)
		self.coins_list.draw(screen)

