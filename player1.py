import pygame as pg
from settings import *
from basic_player import Player

vec = pg.math.Vector2

class Player1(Player):
    def __init__(self, WINSIZE):
        super().__init__()
        self.image.fill('red')
        self.pos = vec(WINSIZE[0]/4, WINSIZE[1]/2)
        
    def update(self):
        self.move()
        self.dontGetOffScreen()
        
    def move(self):
        self.acc = vec(0,0)
        keyspressed = pg.key.get_pressed()
        if keyspressed[pg.K_RIGHT]:
            self.acc.x = playerAcc
        if keyspressed[pg.K_LEFT]:
            self.acc.x = -playerAcc
        if keyspressed[pg.K_DOWN]:
            self.acc.y = playerAcc
        if keyspressed[pg.K_UP]:
            self.acc.y = -playerAcc
        
        if self.vel.x > playerMaxSpeed:
            self.vel.x = playerMaxSpeed
        if self.vel.x < -playerMaxSpeed:
            self.vel.x = -playerMaxSpeed
        if self.vel.y > playerMaxSpeed:
            self.vel.y = playerMaxSpeed
        if self.vel.y < -playerMaxSpeed:
            self.vel.y = -playerMaxSpeed
            
        self.vel += self.acc
        self.pos.x += self.vel.x + self.acc.x/2
        self.pos.y += self.vel.y + self.acc.y/2
        self.rect.center = self.pos
        
    def dontGetOffScreen(self):
        if self.rect.left < 0:
            self.pos.x = self.rect.width//2
            self.vel.x = bouncePower
        if self.rect.right > WINW/2:
            self.pos.x = WINW/2 - self.rect.width//2
            self.vel.x = -bouncePower
        if self.rect.top < 0:
            self.pos.y = self.rect.height//2
            self.vel.y = bouncePower
        if self.rect.bottom > WINH:
            self.pos.y = WINH - self.rect.height//2
            self.vel.y = -bouncePower