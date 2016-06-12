#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import math
import random
import constants

from spritesheet_functions import SpriteSheet

class Gallinazo(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []
    # Este es el "centro" que el sprite orbitará
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

        image = self.walking_frames_r.append(pygame.image.load('minigalli.png'))


        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    def update(self):

        # Calculamos un nuevo x, y
        self.rect.x = self.radio * math.sin(self.angulo) + self.centrar_x
        #self.rect.x = (-1)*math.sqrt(1+math.pow(2,2))
        self.rect.y = self.radio * math.cos(self.angulo) + self.centrar_y
         
        # Incrementamos el ángulo para la siguiente ronda.
        self.angulo += self.velocidad