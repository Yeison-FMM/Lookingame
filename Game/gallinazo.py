#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import math
import random
import constants

from spritesheet_functions import SpriteSheet

class Gallinazo(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0

    centrar_x = 0
    centrar_y = 0
 
    # Ángulo actual en radianes
    angulo = 0
     
    #Cuán lejos orbitamos desde el centro, en píxeles
    radio = 0

    # Cuán rápido orbitamos, en radianes por fotograma
    velocidad = 0.05

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        self.image =pygame.image.load('minigalli.png')

        self.rect = self.image.get_rect()

    def update(self):

        # Calculamos un nuevo x, y
        self.rect.x = self.radio * math.sin(self.angulo) + self.centrar_x
        #self.rect.x = (-1)*math.sqrt(1+math.pow(2,2))
        self.rect.y = self.radio * math.cos(self.angulo) + self.centrar_y
         
        # Incrementamos el ángulo para la siguiente ronda.
        self.angulo += self.velocidad