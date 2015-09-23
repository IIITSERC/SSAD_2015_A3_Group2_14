import pygame

from constants import *
from make import *
from Messages import *

class Person(pygame.sprite.Sprite):
	def __init__(self, file_name, w, h):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(file_name)
		self.image = pygame.transform.scale(self.image,(w, h))
		self.rect = self.image.get_rect()
		self.change_x = 0
		self.change_y = 0

class Donkey(Person):
	def __init__(self, file_name, w, h):
		Person.__init__(self, file_name, w, h)
		self.change_x = 3
		self.val = 1
	
	def update(self):
		if self.rect.x > 750 or self.rect.x < 15:
			self.change_x *= -1
		self.rect.x += self.change_x

class Player(Person):
	def __init__(self, file_name, w, h, score, speed):
		Person.__init__(self, file_name, w, h)
		self.board = None
		self.score = score
		self.lives = 3
		self.lad = 0
		self.speed = speed

	#JUMP
	def jump(self):
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self, self.board.platform_list, False)
		self.rect.y -= 2

		if len(platform_hit_list) > 0 or self.lad:
			self.change_y = -7
			

	def go_left(self):
		self.change_x = -self.speed
	def go_right(self):
		self.change_x = self.speed
	
	def go_up(self):
		self.rect.y -= 2
		lad_list = pygame.sprite.spritecollide(self,self.board.ladders_list, False)
		self.rect.y += 2
		
		if len(lad_list) > 0:
			self.change_y = -self.speed
	
	def go_down(self):
		self.rect.y += 10
		lad_list = pygame.sprite.spritecollide(self,self.board.ladders_list, False)
		self.rect.y -= 10
		
		if len(lad_list) > 0:
			self.change_y = self.speed+0.1
	
	def stop(self):
		self.change_x = 0
		self.change_y = 0

	def update(self):
		(posx,posy) = self.getPosition() 
		# LADDERS
		self.rect.y += 2
		lad_hit_list_down = pygame.sprite.spritecollide(self,self.board.ladders_list, False)
		self.rect.y -= 2
		self.rect.y -= 2
		lad_hit_list_up = pygame.sprite.spritecollide(self,self.board.ladders_list, False)
		self.rect.y += 2

		if len(lad_hit_list_down) > 0 or len(lad_hit_list_up) > 0:
			self.lad = 1
		else:
			self.lad = 0
		
		#Gravity
		self.calc_grav()

		# Move <->
		self.rect.x += self.change_x
		block_hit_list = pygame.sprite.spritecollide(self, self.board.platform_list, False)
		for block in block_hit_list:
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				self.rect.left = block.rect.right

		# Move |
		#print (self.change_y)
		self.rect.y += self.change_y
		block_hit_list = pygame.sprite.spritecollide(self, self.board.platform_list, False)
		for block in block_hit_list:
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom
			self.change_y = 0

	def calc_grav(self):
		if self.lad:
			if self.change_y == self.speed+0.1:
				self.change_y = self.speed+0.1
			elif self.change_y > 0:
				self.change_y = 0 
		else:
			self.change_y += 0.5

	def show_attributes(self, screen, font, balls_list):
		#COINS
		self.collectCoin()
		# FIRE BALLS
		lives =  self.checkCollision(balls_list)
		#SHOWING
		text = font.render('P', True, RED)
		screen.blit(text, [SC_WIDTH - 110, 15])
		text = font.render(' to Pause', True, WHITE)
		screen.blit(text, [SC_WIDTH - 90, 15])

		text = font.render('SCORE  :  '+str(self.score), True, WHITE)
		screen.blit(text, [20, SC_HEIGHT - 30])
		text = font.render('LIVES  :  ', True, WHITE)
		screen.blit(text, [SC_WIDTH - 250, SC_HEIGHT - 30])
		for i in range(self.lives):
			img = pygame.image.load('life.png')
			img = pygame.transform.scale(img, (20, 20))
			screen.blit(img, [SC_WIDTH - 170 + (i*25),SC_HEIGHT - 30])
		return lives

	def getPosition(self):
		return (self.rect.x, self.rect.y)

	def collectCoin(self):
		coin_hit_list = pygame.sprite.spritecollide(self,self.board.coins_list, True)
		for coin in coin_hit_list:
			self.score += 5

	def checkCollision(self, balls_list):
		ball_hit_list = pygame.sprite.spritecollide(self,balls_list, True)
		#ball_hit_list.extend(pygame.sprite.spritecollide(self,donkey_list, False))
		if len(ball_hit_list) > 0:
			if self.score > 25:
				self.score -= 25
			else:
				self.score = 0
			self.lives -= 1
			return self.lives

