import pygame, random

class Fireball(pygame.sprite.Sprite):
	def __init__(self, donkey, board, speed):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('ball.png')
		self.image = pygame.transform.scale(self.image,(20, 25))
		
		self.rect = self.image.get_rect()

		self.rect.x = 0
		self.rect.y = 0
		self.change_x = speed
		self.change_y = 0
		#flags
		self.lad_down = 0
		self.lad_up = 0
		self.platform = 0
	
		self.board = board
		
		self.speed = speed
		self.getPosition(donkey)

	def update(self):
		#set the flags
		self.set_flags()
		#gravity
		self.calc_grav()
		self.cases()
		#move
		self.move()
	
	def calc_grav(self):
		self.change_y += 0.5
	
	def set_flags(self):
		self.rect.y += 20
		lad_down_list = pygame.sprite.spritecollide(self, self.board.ladders_list, False)
		lad_down_list.extend(pygame.sprite.spritecollide(self, self.board.broken_ladders_list, False))
		self.rect.y -= 20
		if len(lad_down_list):
			self.lad_down = 1
		else:
			self.lad_down = 0	
		
		self.rect.y -= 20		
		lad_up_list = pygame.sprite.spritecollide(self, self.board.ladders_list, False)
		self.rect.y += 20
		if len(lad_up_list):
			self.lad_up = 1
		else:
			self.lad_up = 0

		self.rect.y += 5
		self.rect.x += 10
		block_hit_list = self.checkWall()
		self.rect.y -= 5
		self.rect.x -= 10
		if len(block_hit_list):
			self.platform = 1
		else:
			self.platform = 0
	
	def cases(self):
		go_down = random.randrange(10)
		#go_down = 1
		rand_horizontal = random.randrange(2)
		#Choose Ladder
		if go_down == 0:
			self.stay_up()
		#change direction
		if self.change_y > 7:
			if rand_horizontal:
				self.change_x = -self.speed
			else:
				self.change_x = self.speed

	def stay_up(self):
		#print ('stay_up')
		if not self.lad_up:
			self.rect.y += 2
			lad_hit_list = pygame.sprite.spritecollide(self, self.board.ladders_list, False)
			lad_hit_list.extend(pygame.sprite.spritecollide(self, self.board.broken_ladders_list, False))
			self.rect.y -= 2
			
			self.rect.x += 40
			self.rect.y += 30
			block_hit_list = self.checkWall()
			self.rect.x -= 40
			self.rect.y -= 30
			if len(block_hit_list) == 0:
				for lad in lad_hit_list:
					if self.change_y > 0:
						self.rect.bottom = lad.rect.top-1
					self.change_y = 0

	def move(self):
		#print (self.change_y)
		# Move <->
		self.rect.x += self.change_x
		block_hit_list = self.checkWall()
		for block in block_hit_list:
			if self.change_x > 0 and not self.lad_down:
				self.rect.right = block.rect.left
				self.change_x *= -1
			elif self.change_x < 0 and not self.lad_down:
				self.rect.left = block.rect.right
				self.change_x *= -1

		# Move |
		self.rect.y += self.change_y
		block_hit_list = self.checkWall()
		for block in block_hit_list:
			if self.change_y > 0:
				self.rect.bottom = block.rect.top-4
			self.change_y = 1

	def getPosition(self, donkey):
		self.rect.x = donkey.rect.x
		self.rect.y = donkey.rect.y

	def checkWall(self):
		block_hit_list = pygame.sprite.spritecollide(self, self.board.platform_list, False)
		return block_hit_list
