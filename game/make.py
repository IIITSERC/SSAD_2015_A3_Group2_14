import pygame

class Make(pygame.sprite.Sprite):
	def __init__(self, file_name, w, h, x, y):
		
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.image.load(file_name)
		self.image = pygame.transform.scale(self.image,(w, h))
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	
	def fall(self, platform_list):
		fl = 1
		while fl:
			hit_list = pygame.sprite.spritecollide(self, platform_list, False)
			if len(hit_list) == 0:	
				fl = 0
			else:
				self.rect.y -= 10

		fl = 1
		while fl:
			self.rect.y += 1
			hit_list = pygame.sprite.spritecollide(self, platform_list, False)
			self.rect.y -= 1
			if not len(hit_list):
				self.rect.y += 1
			else:
				fl = 0
	
	def vanish(self, balls_sprite_list):
		temp_list = pygame.sprite.spritecollide(self, balls_sprite_list, True)
