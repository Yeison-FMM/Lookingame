#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Global constants
"""
from lookingame import Game

# Colors
BLACK    = (   0,   0,   0) 
WHITE    = ( 255, 255, 255) 
BLUE     = (   0,   0, 255)

# Screen dimensions
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

# Options
opciones = [
			("Jugar", Game().comenzar_nuevo_juego),
			("Instruc", Game().mostrar_opciones),
			("Salir", Game().salir_del_programa)
		]


red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

