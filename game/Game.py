import pygame, random

from Person import *
from FireBalls import *
from constants import *
from make import *
from Board import *
from Messages import *

class Game():
	def __init__(self):
		self.player_lives = 3
		self.cur_val = 3
		self.score = 0
		self.ball_speed = 1
		self.ball_frequency = 100 #reduce the value to increase the frequency 
		self.player_speed = 4
		self.fl = 1

	def gameLoop(self, screen, font):
		
		m = Messages(screen, font)
		board = Board()
		
		gamePause = False
		gameExit = False
		gameOver = False
		freq = 1000
		
		#BEGIN BELOW
		if self.fl == 1:
			self.fl = 0
			begin = False
			while not begin:
				m.Start_Message()
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_e:
							begin = True
						if event.key == pygame.K_q:
							begin = True
							gameExit = True
		else:
			cont = False
			while not cont:
				m.level_up_Message()
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_c:
							cont = True
						if event.key == pygame.K_q:
							cont = True
							gameExit = True
		##BEGIN ABOVE
		
		player = Player('mario.png', 20, 30, self.score, self.player_speed)
		player.board = board

		donkey = Donkey('don_1.png', 50, 50)

		player.rect.x = 50
		player.rect.y = SC_HEIGHT - player.rect.height - 50
		
		donkey.rect.x = 50
		donkey.rect.y = 150

		queen = Make('queen.png', 30, 40, 250, 70)

		player_sprite_list = pygame.sprite.Group()
		balls_sprite_list = pygame.sprite.Group()
		donkey_sprite_list = pygame.sprite.Group()
		queen_sprite_list = pygame.sprite.Group()
		all_sprites_list = pygame.sprite.Group()

		all_sprites_list.add(player)
		all_sprites_list.add(donkey)
		all_sprites_list.add(queen)
		player_sprite_list.add(player)
		donkey_sprite_list.add(donkey)
		queen_sprite_list.add(queen)

		while not gameExit:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
					if event.key == pygame.K_p:
						gamePause = True
					if event.key == pygame.K_a:
						player.go_left()
					if event.key == pygame.K_d:
						player.go_right()
					if event.key == pygame.K_w:
						player.go_up()
					if event.key == pygame.K_s:
						player.go_down()
					if event.key == pygame.K_SPACE:
						player.jump()
				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_a or event.key == pygame.K_d:
						player.stop()
					if event.key == pygame.K_w or event.key == pygame.K_s:
						player.stop()
			#MAKE FIREBALLS
			flag = random.randrange(2)
			if freq > self.ball_frequency and flag:
			#if freq > 10: FOR TESTING RANDOMNESS
				freq = 0
				ball = Fireball(donkey, board, self.ball_speed)
				balls_sprite_list.add(ball)
				all_sprites_list.add(ball)
			else:
				freq += 1
			
			#DRAWINGS BELOW
			all_sprites_list.update()

			#board.update()
			balls_sprite_list.update()
			board.door.vanish(balls_sprite_list)

			board.draw(screen)
			all_sprites_list.draw(screen)
			balls_sprite_list.draw(screen)
			##DRAWINGS ABOVE
			
			#LOGIC BELOW
			self.player_lives = player.show_attributes(screen, font, balls_sprite_list)
			if self.player_lives == 0:
				gameOver = True

			if self.cur_val != self.player_lives:
				
				player.rect.x = 30
				player.rect.y = SC_HEIGHT - player.rect.height - 50
		
				donkey.rect.x = 50
				donkey.rect.y = 150
				self.cur_val = self.player_lives
			#queen hit
			queen_hit = pygame.sprite.spritecollide(player, queen_sprite_list, False)
			if len(queen_hit) > 0:
				self.score = player.score + 50
				self.ball_speed += 2
				self.player_speed += 2
				if self.ball_frequency > 50:
					self.ball_frequency -= 50
				else:
					self.ball_frequency -= 5
				self.gameLoop(screen, font)
			##LOGIC ABOVE

			clock.tick(60)
			pygame.display.update()
		
			while gameOver == True:
				m.End_Message(self.score)
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							gameExit = True
							gameOver = False
						if event.key == pygame.K_r:
							gameOver = False
							self.score = 0
							self.fl = 1
							self.gameLoop(screen, font)

			while gamePause == True:
				m.Pause_Message()
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							gameExit = True
							gamePause = False
						if event.key == pygame.K_r:
							gamePause = False
							self.score = 0
							self.fl = 1
							self.gameLoop(screen, font)
						if event.key == pygame.K_c:
							gamePause = False
				
		pygame.quit()
		quit()
