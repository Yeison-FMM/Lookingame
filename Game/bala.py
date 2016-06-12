import pygame

class Bala(pygame.sprite.Sprite):
    def __init__(self,imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(imagen).convert_alpha()
        self.rect = self.image.get_rect()
        self.jugador=0
        #self.velocidad=5

    def update(self):
        if self.jugador==2:
            self.rect.y+=5
        if self.jugador==0:
            self.rect.x+=5
        elif self.jugador==1:
            self.rect.x-=5