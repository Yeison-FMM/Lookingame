import pygame

import constants
import platforms

class Level():
	# Atributos
	platform_list = None
	enemy_list = None

	# Background image
	background = None

	# Sirve para hacer "scroll y mover el mundo cuando movemos el jugador"
	world_shift = 0
	level_limit = -1000


	def __init__(self, player,buho,enemigo):

		self.platform_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.player = player
		self.buho = buho

		self.enemigo = enemigo

	# 
	def update(self):
		self.platform_list.update()
		self.enemy_list.update()

	def draw(self, screen,puntaje,vida_personaje,vida_jefe):

		font = pygame.font.Font("fonts/FEASFBI_.TTF",20)
		screen.blit(self.background,(self.world_shift // 3,0))
		label_1 = font.render("Puntaje: ",True,(255,255,255))
		label_2 = font.render("Vida: ",True,(255,255,255))
		label_3 = font.render("Enemigo Jefe: ",True,(255,255,255))
		textSurface_1 = font.render(str(puntaje), True, (244,67,54))
		textSurface_2 = font.render(str(vida_personaje), True, (0,150,136))
		textSurface_3 = font.render(str(vida_jefe), True, (0,150,136))
		screen.blit(label_1,(0,0))
		screen.blit(label_2,(140,0))
		screen.blit(label_3,(600,0))
		screen.blit(textSurface_1,(90,0))
		screen.blit(textSurface_2,(204,0))
		screen.blit(textSurface_3,(740,0))

		self.platform_list.draw(screen)
		self.enemy_list.draw(screen)

	def shift_world(self, shift_x):
		# Corremos el mundo lo indicado por shift_x mas la posicion del mundo
		self.world_shift += shift_x

		# Desplazamos las plataformas y los enemigos cuando corremos el mundo
		for platform in self.platform_list:
			platform.rect.x += shift_x

		for enemy in self.enemy_list:
			enemy.rect.x += shift_x

# Creamos el nivel 1
class Level_01(Level):

	def __init__(self, player, buho, enemigo):
		
		# Call the parent constructor
		Level.__init__(self, player, buho, enemigo)

		self.background = pygame.image.load("background_01.png").convert()
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = -2500

		# Aqui tenemos las plataformas del background
		level = [ [platforms.GRASS_LEFT, 500, 500],
				  [platforms.GRASS_MIDDLE, 570, 500],
				  [platforms.GRASS_RIGHT, 640, 500],
				  [platforms.GRASS_LEFT, 800, 400],
				  [platforms.GRASS_MIDDLE, 870, 400],
				  [platforms.GRASS_RIGHT, 940, 400],
				  [platforms.GRASS_LEFT, 1000, 500],
				  [platforms.GRASS_MIDDLE, 1070, 500],
				  [platforms.GRASS_RIGHT, 1140, 500],
				  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
				  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
				  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
				  ]

		
		for platform in level:
			block = platforms.Platform(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			block.buho   = self.buho
			block.enemigo = self.enemigo

			self.platform_list.add(block)

		# Se agrega el bloque pequeño que se mueve
		block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
		block.rect.x = 1350
		block.rect.y = 280
		block.boundary_left = 1350
		block.boundary_right = 1600
		block.change_x = 1
		block.player = self.player
		block.level = self
		self.platform_list.add(block)


# Creamos el nivel 2 de la misma forma que el nivel 1, con diferente background
class Level_02(Level):

	def __init__(self, player,buho,enemigo):
		
		Level.__init__(self, player,buho,enemigo)

		self.background = pygame.image.load("background_02.png").convert()
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = -1000

		# Array with type of platform, and x, y location of the platform.
		level = [ [platforms.STONE_PLATFORM_LEFT, 500, 550],
				  [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
				  [platforms.STONE_PLATFORM_RIGHT, 640, 550],
				  [platforms.GRASS_LEFT, 800, 400],
				  [platforms.GRASS_MIDDLE, 870, 400],
				  [platforms.GRASS_RIGHT, 940, 400],
				  [platforms.GRASS_LEFT, 1000, 500],
				  [platforms.GRASS_MIDDLE, 1070, 500],
				  [platforms.GRASS_RIGHT, 1140, 500],
				  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
				  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
				  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
				  ]

		for platform in level:
			block = platforms.Platform(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			block.buho  = self.buho
			block.enemigo = self.enemigo
			self.platform_list.add(block)

		block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
		block.rect.x = 1500
		block.rect.y = 300
		block.boundary_top = 100
		block.boundary_bottom = 550
		block.change_y = -1
		block.player = self.player
		block.level = self
		self.platform_list.add(block)
