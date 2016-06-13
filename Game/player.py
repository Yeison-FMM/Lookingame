import pygame

import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
	change_x = 0
	change_y = 0

	# Listas para almacenar los movimientos del sprite
	walking_frames_l = []
	walking_frames_r = []

	# Nos indicara hacia donde mira el jugador
	direction = "R"

	level = None

	# -- Methods
	def __init__(self):
	
		pygame.sprite.Sprite.__init__(self)

		sprite_sheet = SpriteSheet("chicken.png")

		self.vida = 1000

		# Cargamos la imagen de la gallina mirando a la izquierda
		image = self.walking_frames_r.append(pygame.image.load('uno.png'))
		image = self.walking_frames_r.append(pygame.image.load('dos.png'))
		image = self.walking_frames_r.append(pygame.image.load('tres.png'))

		# Cargamos las imagenes de la gallina mirando a la derecha
		image = sprite_sheet.get_image(0, 47, 50, 20)
		image = pygame.transform.flip(image, True, False)
		image = self.walking_frames_l.append(pygame.image.load('cuatro.png'))
		image = self.walking_frames_l.append(pygame.image.load('cinco.png'))
		image = self.walking_frames_l.append(pygame.image.load('seis.png'))


		# La gallina inicia mirando a la derecha
		self.image = self.walking_frames_l[0]

		# Obtenemos una refecian del rectangulo que cubre a la imagen
		self.rect = self.image.get_rect()

	def update(self):
		""" Move the player. """
		# Gravity
		self.calc_grav()

		# Move left/right
		self.rect.x += self.change_x
		pos = self.rect.x + self.level.world_shift
		if self.direction == "R":
			frame = (pos // 30) % len(self.walking_frames_r)
			self.image = self.walking_frames_r[frame]
		else:
			frame = (pos // 30) % len(self.walking_frames_l)
			self.image = self.walking_frames_l[frame]

		# Si colisoniamos con algun elemento de la plataforma
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				self.rect.left = block.rect.right

		# Nos sirve para movernos hacia arriba(saltar)
		self.rect.y += self.change_y

		# Verificamos si chocamos con algo
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:

			# Cambiamos nuestra posicion en caso de chocar
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom
			self.change_y = 0

			if isinstance(block, MovingPlatform):
				self.rect.x += block.change_x

	# Metodo para ponerle efecto de gravedad al jugador
	def calc_grav(self):
		""" Calculate effect of gravity. """
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .35

		if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

	# Metodo para saltar 
	def jump(self):
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2
		if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
			self.change_y = -10

	# Nos movemos a la izquierda
	def go_left(self):
		self.change_x = -6
		self.direction = "L"

	# Nos movemos a la derecha
	def go_right(self):
		self.change_x = 6
		self.direction = "R"

	# Frenamos
	def stop(self):
		self.change_x = 0
