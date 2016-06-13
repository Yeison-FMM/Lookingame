#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import math
import random
import constants

from spritesheet_functions import SpriteSheet

class Aguila(pygame.sprite.Sprite):

	# -- Attributes
	limite_izquierdo = 0
	limite_derecho = 0
	limite_superior = 0
	limite_inferior = 0
	cambio_x = 0
	cambio_y = 0

	# -- Methods
	def __init__(self):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("aguila.png")
		self.rect = self.image.get_rect()
		self.vida = 150

	# Actualiza la posicion del aguila en x y en y
	def update(self):
		self.rect.x += self.cambio_x
		self.rect.y += self.cambio_y
		 
		if self.rect.right >= self.limite_derecho or self.rect.left <= self.limite_izquierdo:
			self.cambio_x *= -1

		if self.rect.bottom >= self.limite_inferior or self.rect.top <= self.limite_superior:
			self.cambio_y *= -1