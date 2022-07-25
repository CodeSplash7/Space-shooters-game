import pygame as pg
from settings import *

class Bullet(pg.sprite.Sprite):
    def __init__(self, color, way, pos):
        self.color = color
        self.way = way
        super().__init__()
        self.image = pg.Surface((bulletLen, bulletThickness))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = pos)
        self.speed = bulletSpeed
    
    def update(self, ALL_BULLETS=None):
        self.rect.x += self.way * self.speed
        self.checkOutOfWindow()
        
    def checkOutOfWindow(self):
        if self.rect.centerx + bulletLen/2*self.way > WINW or self.rect.centerx + bulletLen/2*self.way < 0:
            self.kill()