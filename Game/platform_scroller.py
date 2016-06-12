#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys
import math, random
import constants

import levels, time
from bala import Bala
from pygame.locals import * 
from player import Player
from buho import Buho
from aguila import Aguila
from gallinazo import Gallinazo
from halcon import Halcon

import levels
from pygame.locals import * 
from player import Player
from buho import Buho

from menu import Menu
import pygame, os 

class Game:

	def __init__(self):
		os.environ['SDL_VIDEO_CENTERED'] = '1'
		self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
		self.background_image = self.load_image("images/background_initial.png").convert()
		self.gameover = self.load_image("game-over.jpg").convert()
		self.gana = self.load_image("win.png").convert()
		self.pause = True
		self.active = True

	def text_objects(self, text, font):
		textSurface = font.render(text, True, (0,0,0))
		return textSurface, textSurface.get_rect()

	def load_image(self,filename, transparent=False):
			try: image = pygame.image.load(filename)
			except pygame.error, message:
					raise SystemExit, message
			image = image.convert()
			if transparent:
					color = image.get_at((0,0))
					image.set_colorkey(color, RLEACCEL)
			return image

	def button(self,msg,x,y,w,h,ic,ac,action=None):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(self.screen, ac,(x,y,w,h))

			if click[0] == 1 and action != None:
				action()         
		else:
			pygame.draw.rect(self.screen, ic,(x,y,w,h))

		smallText = pygame.font.Font("fonts/FEASFBI_.TTF",20)
		textSurf, textRect = self.text_objects(msg, smallText)
		textRect.center = ( (x+(w/2)), (y+(h/2)) )
		self.screen.blit(textSurf, textRect)

	def dispararEnem(self,ls_balaenemie,enemies_list,active_sprite_list):
		for i in ls_balaenemie:
			self.active_sprite_list.add(i)

	def recargarEnem(self, enemies_list,ls_balaenemie,active_sprite_list):
		for i in enemies_list:
			balaenemie = Bala('yoga-ball.png')
			balaenemie.jugador = 2
			balaenemie.rect.x = i.rect.x
			balaenemie.rect.y = i.rect.y
			ls_balaenemie.append(balaenemie)
			active_sprite_list.add(balaenemie)

	def unpause(self):
		self.pause = False
		self.active = False
		pygame.mixer.music.unpause()

	def paused(self):
		clock = pygame.time.Clock()
		largeText = pygame.font.Font("fonts/FEASFBI_.TTF",115)
		TextSurf, TextRect = self.text_objects("Paused", largeText)
		TextRect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/2))
		self.active = True
		while self.pause:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
					
			#self.screen.fill(constants.WHITE)
			self.screen.blit(TextSurf, TextRect)
			self.button("Continue",150,450,100,50,constants.green,constants.bright_green,self.unpause)
			self.button("Quit",550,450,100,50,constants.red,constants.bright_red,self.salir_del_programa)

			pygame.display.update()
			clock.tick(15) 

	def salir_del_programa(self):
		sys.exit(0)

	def comenzar_nuevo_juego(self):
		pygame.init()
		puntuacion = 0
		enemie_dead = True
		enemie_dead2 = True
		entrar = False
		muertohalcon = False
		#Loop until the user clicks the close button.
		done = False
		count = 0
		# Used to manage how fast the screen updates
		clock = pygame.time.Clock()
		crears = True
		# Set the height and width of the screen
		size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
		screen = pygame.display.set_mode(size)

		pygame.display.set_caption("Looking for my Son")

		# Set the sound for intro game
		pygame.mixer.music.load("sounds/birdgame.mp3")
		jump = pygame.mixer.Sound("sounds/jump.wav")
		pygame.mixer.music.play()    
		kill = False
		kill2 = False
		# Create the player
		player = Player()
		buho = Buho()
		enemies_list = []
		enemies_list2 = []
		ls_balaenemie = []
		#  Esto representa un aguila
		aguila = Aguila()
		halcon = Halcon()
		# Create all the levels
		level_list = []
		level_list.append(levels.Level_01(player,buho,aguila))
		level_list.append(levels.Level_02(player,buho,aguila))
		# Set the current level
		current_level_no = 0
		current_level = level_list[current_level_no]

		self.active_sprite_list = pygame.sprite.Group()
		player.level = current_level
		player.rect.x = 340
		player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
		self.active_sprite_list.add(player)

	  
		# Establece una ubicación aleatoria para el aguila
		aguila.rect.x = random.randrange(160)
		aguila.rect.y = random.randrange(10)
		aguila.cambio_x = random.randrange(-3,4)
		aguila.cambio_y = random.randrange(-3,4)
		aguila.limite_izquierdo = 0
		aguila.limite_superior = 0
		aguila.limite_derecho = constants.SCREEN_WIDTH
		aguila.limite_inferior = constants.SCREEN_HEIGHT


		halcon.rect.x = random.randrange(160)
		halcon.rect.y = random.randrange(10)
		halcon.cambio_x = random.randrange(-3,4)
		halcon.cambio_y = random.randrange(-3,4)
		halcon.limite_izquierdo = 0
		halcon.limite_superior = 0
		halcon.limite_derecho = constants.SCREEN_WIDTH
		halcon.limite_inferior = constants.SCREEN_HEIGHT

		"""# Establece una ubicación aleatoria superman
		superman.rect.x = random.randrange(160)
		superman.rect.y = random.randrange(40,600)
		superman.cambio_x = random.randrange(-3,4)
		superman.cambio_y = random.randrange(-3,4)
		superman.limite_izquierdo = 0
		superman.limite_superior = 0
		superman.limite_derecho = constants.SCREEN_WIDTH
		superman.limite_inferior = constants.SCREEN_HEIGHT
		""" 

		for i in range(1):
			buho = Buho()
			balaenemie = Bala('yoga-ball.png')
			balaenemie.jugador = 2
			#Establecemos una ubicación central aleatoria para que orbite el buho.
			buho.centrar_x = random.randrange(200,constants.SCREEN_WIDTH/2)
			buho.centrar_y = random.randrange(100,constants.SCREEN_HEIGHT/2)
			# Radio aleatorio, desde a to b
			buho.radio = random.randrange(0, 300)
			# Ángulo de inicio aleatorio, desde 0 a 2pi
			buho.angulo = random.random() * 2 * math.pi
			# radianes por fotograma.
			buho.velocidad = 0.008
			balaenemie.rect.x = buho.centrar_x
			balaenemie.rect.y = buho.centrar_y
			# Añadimos el buho a la lista de objetos.
			enemies_list.append(buho)
			buho.level = current_level
			ls_balaenemie.append(balaenemie)
		
		for i in range(5):
			gallinazo = Gallinazo()
			balaenemie = Bala('yoga-ball.png')
			balaenemie.jugador = 2
			#Establecemos una ubicación central aleatoria para que orbite el buho.
			gallinazo.centrar_x = random.randrange(300,constants.SCREEN_WIDTH/2)
			gallinazo.centrar_y = random.randrange(100,constants.SCREEN_HEIGHT/2)
			# Radio aleatorio, desde a to b
			gallinazo.radio = random.randrange(0, 280)
			# Ángulo de inicio aleatorio, desde 0 a 2pi
			gallinazo.angulo = random.random() * 2 * math.pi
			# radianes por fotograma.
			gallinazo.velocidad = 0.058
			balaenemie.rect.x = gallinazo.centrar_x
			balaenemie.rect.y = gallinazo.centrar_y
			# Añadimos el buho a la lista de objetos.
			enemies_list2.append(gallinazo)
			gallinazo.level = current_level
			ls_balaenemie.append(balaenemie)

		for i in enemies_list:
			self.active_sprite_list.add(i)

		ls_bala = []
		self.active = False
		fuente = pygame.font.Font(None, 30)
		 
		while not done:
			for event in pygame.event.get(): # User did something
				if event.type == pygame.QUIT: # If user clicked close
					done = True # Flag that we are done so we exit this loop
					pygame.mixer.music.stop()
					self.main()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT and self.active == False:
						player.go_left()
					if event.key == pygame.K_RIGHT and self.active == False:
						player.go_right()
					if event.key == pygame.K_UP and self.active == False:
						player.jump()
						jump.play() 
					if (event.key == pygame.K_p):
						pygame.mixer.music.pause()
						self.active = True
						self.pause = True
						self.paused()   
					if event.key == pygame.K_x:
						if player.direction == 'L':
							bala = Bala('corn_l.png')
							bala.jugador = 1
						else:
							bala=Bala('corn_r.png')

						bala.rect.x=player.rect.x+10
						bala.rect.y=player.rect.y
						self.active_sprite_list.add(bala)
						ls_bala.append(bala)
						for j in ls_bala:
							if current_level_no == 0:								
								for i in enemies_list:
									if i == aguila:
										if pygame.sprite.collide_rect(i,j):
											aguila.vida -= 10
											self.active_sprite_list.remove(j)
											ls_bala.remove(j)
											puntuacion += 50 
									else:
										if pygame.sprite.collide_rect(i,j):
											self.active_sprite_list.remove(i)
											enemies_list.remove(i)
											self.active_sprite_list.remove(j)
											ls_bala.remove(j)
											puntuacion += 50 
							else:
								for i in enemies_list2:
									if i == halcon:
										if pygame.sprite.collide_rect(i,j):
											halcon.vida -= 10
											self.active_sprite_list.remove(j)
											ls_bala.remove(j)
											puntuacion += 50 
									else:
										if pygame.sprite.collide_rect(i,j):
											self.active_sprite_list.remove(i)
											enemies_list2.remove(i)
											self.active_sprite_list.remove(j)
											ls_bala.remove(j)
											puntuacion += 50

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT and player.change_x < 0:
						player.stop()
					if event.key == pygame.K_RIGHT and player.change_x > 0:
						player.stop()

			disparar = random.randint(1,60)
			if disparar == 1 and current_level_no == 0:
				self.recargarEnem(enemies_list,ls_balaenemie,self.active_sprite_list)
			if disparar == 1 and current_level_no == 1:
				self.recargarEnem(enemies_list2,ls_balaenemie,self.active_sprite_list)

			# Update the player and enemies
			self.active_sprite_list.update()

			# Update items in the level
			current_level.update()
			# GameOver

			"""if player.vida < 400:
				self.active_sprite_list.add(superman)

			if pygame.sprite.collide_rect(player,superman):
				self.active_sprite_list.remove(superman)
				for sprite in self.active_sprite_list:
					if sprite == superman:
						sprite.kill()
						active_sprite_list.remove(sprite)
				player.vida += 300
			"""

			if player.vida<=0:
				screen.blit(self.gameover,(0,0))
				pygame.display.flip()
				pygame.mixer.music.stop()
				time.sleep(2)
				done = True
				self.main()
				puntuacion = 0
				player.vida = 1000
		
			if aguila.vida <=0:
				self.active_sprite_list.remove(aguila)
				for i in enemies_list[:]:
					enemies_list.remove(i)
				enemie_dead = False
				entrar = True
				aguila.vida = 0

			if halcon.vida <=0:
				self.active_sprite_list.remove(halcon)
				for i in enemies_list2[:]:
					enemies_list2.remove(i)
				enemie_dead2 = False
				entrar = False
				halcon.vida = 0
				muertohalcon = True

			for j in ls_bala:
				for i in ls_balaenemie:
					if pygame.sprite.collide_rect(i,j):
						self.active_sprite_list.remove(i)
						ls_balaenemie.remove(i)
						self.active_sprite_list.remove(j)
						ls_bala.remove(j) 

			if current_level_no == 0:			
				for i in enemies_list:
					if pygame.sprite.collide_rect(i,player) and puntuacion>0 and player.vida>0:
						player.vida -= 10
			else:
				for i in enemies_list2:
					if pygame.sprite.collide_rect(i,player) and puntuacion>0 and player.vida>0:
						player.vida -= 10

			for i in ls_balaenemie:
				if pygame.sprite.collide_rect(i,player) and puntuacion>=0 and player.vida>=0:
					player.vida -= 10
					self.active_sprite_list.remove(i)
					ls_balaenemie.remove(i)

			# If the player gets near the right side, shift the world left (-x)
			if player.rect.x >= 500:
				diff = player.rect.x - 500
				player.rect.x = 500
				current_level.shift_world(-diff)

			# If the player gets near the left side, shift the world right (+x)
			if player.rect.x <= 120:
				diff = 120 - player.rect.x
				player.rect.x = 120
				current_level.shift_world(diff)

			if not enemies_list:
				if enemie_dead: 
					kill = True
				else:
					kill = False

			if not enemies_list2:
				if enemie_dead2: 
					kill2 = True
				else:
					kill2 = False

			# If the player gets to the end of the level, go to the next level
			current_position = player.rect.x + current_level.world_shift

			#if current_position < -1000 and enemies_list[1] == aguila and entrar:
			#   del enemies_list[0]
			#   enemie_dead = False

			if current_position < -760 and kill and current_level_no == 0:
				#Añade el aguila a la lista de objetos
				pygame.mixer.music.load("battle.mp3")
				pygame.mixer.music.play()
				enemies_list.append(aguila)
				current_level.draw(screen,puntuacion,player.vida,aguila.vida)
				self.active_sprite_list.add(aguila)
				kill = False
				enemie_dead = False

			elif current_position < -760 and kill2 and current_level_no == 1:
				pygame.mixer.music.load("battle.mp3")
				pygame.mixer.music.play()
				enemies_list2.append(halcon)
				current_level.draw(screen,puntuacion,player.vida,halcon.vida)
				self.active_sprite_list.add(halcon)
				kill2 = False
				enemie_dead2 = False


			if current_level_no == 1 and not enemies_list2 and muertohalcon:
				time.sleep(2)
				screen.blit(self.gana,(0,0))
				pygame.display.flip()
				pygame.mixer.music.stop()
				time.sleep(2)
				done = True
				self.main()
				puntuacion = 0
				player.vida = 1000

			if current_position < current_level.level_limit and entrar:
				#player.rect.x = 120
				for i in enemies_list2:
					self.active_sprite_list.add(i)
				if current_level_no < len(level_list)-1:
					current_level_no += 1
					current_level = level_list[current_level_no]
					player.level = current_level

			# ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
			if current_level_no == 0:
				current_level.draw(screen,puntuacion,player.vida,aguila.vida)
			else:
				current_level.draw(screen,puntuacion,player.vida,halcon.vida)

			self.active_sprite_list.draw(screen)

			# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

			# Limit to 60 frames per second
			clock.tick(60)
			
			# Go ahead and update the screen with what we've drawn.
			pygame.display.flip()
		
	def mostrar_opciones(self):
		pass        

	def main(self):
		""" Main Program """
		pygame.init()

		# Set the height and width of the screen
		size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
		self.screen = pygame.display.set_mode(size)

		pygame.display.set_caption("Looking for my Son")

		# Set the sound for intro game
		pygame.mixer.music.load("sounds/intro.mp3")
		pygame.mixer.music.play(10)

		#Loop until the user clicks the close button.
		done = False

		# Used to manage how fast the screen updates
		clock = pygame.time.Clock()

		# import menu
		menu = Menu(constants.opciones)

		# -------- Main Program Loop -----------
		while not done:
			clock.tick(60)
			for eventos in pygame.event.get():
				if (eventos.type == QUIT):
					sys.exit(0)
					done = True
			self.screen.blit(self.background_image, (0, 0))
			menu.actualizar()
			menu.imprimir(self.screen)
			pygame.display.flip()
			pygame.time.delay(10)
		return 0

if __name__ == "__main__":
	Game().main()