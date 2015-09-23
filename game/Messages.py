import pygame

from constants import *

class Messages():
	def __init__(self, screen, font):
		self.font = font
		self.screen = screen

	def Start_Message(self):
		self.screen.fill(WHITE)
		local_font = pygame.font.Font(None, 50)
		text = local_font.render('DONKEY KONG', True, BLACK)
		self.screen.blit(text, [SC_WIDTH/2 - 120,100])
		#KEYS BELOW
		local_font = pygame.font.Font(None, 45)
		pygame.draw.rect(self.screen, BLACK, [145 , 240, 50, 50])
		text = local_font.render('W', True, WHITE)
		self.screen.blit(text, [155, 250])
		pygame.draw.rect(self.screen, BLACK, [100 , 300, 50, 50])
		text = local_font.render('A', True, WHITE)
		self.screen.blit(text, [110, 310])
		pygame.draw.rect(self.screen, BLACK, [160 , 300, 50, 50])
		text = local_font.render('S', True, WHITE)
		self.screen.blit(text, [170, 310])
		pygame.draw.rect(self.screen, BLACK, [220 , 300, 50, 50])
		text = local_font.render('D', True, WHITE)
		self.screen.blit(text, [230, 310])

		text = local_font.render('to', True, BLACK)
		self.screen.blit(text, [300, 290])
		text = local_font.render('MOVE', True, RED)
		self.screen.blit(text, [340, 290])


		pygame.draw.rect(self.screen, BLACK, [220 , 380, 400, 50])
		text = local_font.render('Space Bar', True, WHITE)
		self.screen.blit(text, [340, 387])
		text = local_font.render('to', True, BLACK)
		self.screen.blit(text, [655, 390])
		text = local_font.render(' JUMP', True, RED)
		self.screen.blit(text, [690, 390])
		local_font = pygame.font.Font(None, 20)
		text = local_font.render('*ladders boost the jump', True, RED)
		self.screen.blit(text, [220, 440])
		##KEYS ABOVE
		local_font = pygame.font.Font(None, 45)
		text = local_font.render('Press ', True, BLACK)
		self.screen.blit(text, [100,550])
		text = local_font.render(' Q ', True, RED)
		self.screen.blit(text, [190,550])
		text = local_font.render('to Quit', True, BLACK)
		self.screen.blit(text, [240,550])

		text = local_font.render('Press ', True, BLACK)
		self.screen.blit(text, [100,500])
		text = local_font.render(' E ', True, RED)
		self.screen.blit(text, [190,500])
		text = local_font.render('to Start', True, BLACK)
		self.screen.blit(text, [240,500])

		pygame.display.update()

	def End_Message(self, score):
		self.screen.fill(WHITE)
		local_font = pygame.font.Font(None, 50)
		text = local_font.render('GAME OVER', True, RED)
		self.screen.blit(text, [SC_WIDTH/2 - 120,150])

		local_font = pygame.font.Font(None, 40)
		text = local_font.render('Score is ', True, BLACK)
		self.screen.blit(text, [SC_WIDTH/2 - 250,250])
		text = local_font.render(str(score), True, RED)
		self.screen.blit(text, [SC_WIDTH/2 - 100,250])

		text = local_font.render('Press ', True, BLACK)
		self.screen.blit(text, [SC_WIDTH/2 - 300,350])
		text = local_font.render(' Q ', True, RED)
		self.screen.blit(text, [SC_WIDTH/2 - 220,350])
		text = local_font.render('to Quit', True, BLACK)
		self.screen.blit(text, [SC_WIDTH/2 - 170,350])

		text = local_font.render('Press ', True, BLACK)
		self.screen.blit(text, [SC_WIDTH/2 - 300,400])
		text = local_font.render(' R ', True, RED)
		self.screen.blit(text, [SC_WIDTH/2 - 220,400])
		text = local_font.render('to Restart', True, BLACK)
		self.screen.blit(text, [SC_WIDTH/2 - 170,400])

		pygame.display.update()

	def Pause_Message(self):
		w = 300
		h = 150
		pygame.draw.rect(self.screen, WHITE, [(SC_WIDTH-w)/2 , (SC_HEIGHT-h)/2, w, h])
		text = self.font.render('PAUSED', True, RED)
		self.screen.blit(text, [(SC_WIDTH-w)/2 + 120, (SC_HEIGHT-h)/2 + 10])
		text = self.font.render('C', True, RED)
		self.screen.blit(text, [(SC_WIDTH-w)/2 + 15, (SC_HEIGHT-h)/2 + 45])
		text = self.font.render(' to continue', True, BLACK)
		self.screen.blit(text, [(SC_WIDTH-w)/2 + 25, (SC_HEIGHT-h)/2 + 45])

		text = self.font.render('Q', True, RED)
		self.screen.blit(text, [(SC_WIDTH-w)/2 + 15, (SC_HEIGHT-h)/2 + 75])
		text = self.font.render(' to quit', True, BLACK)
		self.screen.blit(text, [(SC_WIDTH-w)/2 + 25, (SC_HEIGHT-h)/2 + 75])

		text = self.font.render('R', True, RED)
		self.screen.blit(text, [(SC_WIDTH-w)/2 + 15, (SC_HEIGHT-h)/2 + 105])
		text = self.font.render(' to restart', True, BLACK)
		self.screen.blit(text, [(SC_WIDTH-w)/2 + 25, (SC_HEIGHT-h)/2 + 105])
		pygame.display.update()

	def level_up_Message(self):
		self.screen.fill(WHITE)
		local_font = pygame.font.Font(None, 50)
		text = local_font.render('LEVEL UP', True, RED)
		self.screen.blit(text, [SC_WIDTH/2 - 120,150])
		local_font = pygame.font.Font(None, 40)
		text = local_font.render('Press ', True, BLACK)
		self.screen.blit(text, [SC_WIDTH/2 - 300,250])
		text = local_font.render(' C ', True, RED)
		self.screen.blit(text, [SC_WIDTH/2 - 220,250])
		text = local_font.render('to continue', True, BLACK)
		self.screen.blit(text, [SC_WIDTH/2 - 170,250])

		text = local_font.render('Press ', True, BLACK)
		self.screen.blit(text, [SC_WIDTH/2 - 300,300])
		text = local_font.render(' Q ', True, RED)
		self.screen.blit(text, [SC_WIDTH/2 - 220,300])
		text = local_font.render('to quit', True, BLACK)
		self.screen.blit(text, [SC_WIDTH/2 - 170,300])

		local_font = pygame.font.Font(None, 20)
		text = local_font.render('*ladders are safe', True, RED)
		self.screen.blit(text, [SC_WIDTH/2 - 300,340])

		pygame.display.update()

