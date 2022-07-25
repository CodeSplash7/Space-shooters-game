from turtle import back
import pygame as pg
from settings import *
from player1 import Player1
from player2 import Player2
from bullet import Bullet

SCREEN = pg.display.set_mode(WINSIZE)
CLOCK = pg.time.Clock()
pg.init()
pg.mixer.init()

def update(ALL_BULLETS):
    ALL_SPRITES.update(ALL_BULLETS)
    
def render(background):
    SCREEN.fill("white")
    SCREEN.blit(background[0], background[1])
    ALL_SPRITES.draw(SCREEN)
    pg.display.flip()

background = pg.image.load(background_image)
background = pg.transform.scale(background, WINSIZE)
backgroundRect = background.get_rect()
background = [background, backgroundRect]

ALL_SPRITES = pg.sprite.Group()
ALL_BULLETS = pg.sprite.Group()
player1 = Player1(WINSIZE)
ALL_SPRITES.add(player1)
player2 = Player2(WINSIZE)
ALL_SPRITES.add(player2)

running = True
while running:
    CLOCK.tick(FPS)
    # events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RSHIFT:
                bullet = Bullet('red', 1, player1.rect.midright)
                ALL_BULLETS.add(bullet)
                ALL_SPRITES.add(bullet)
            if event.key == pg.K_LSHIFT:
                bullet = Bullet('yellow', -1, player2.rect.midleft)
                ALL_BULLETS.add(bullet)
                ALL_SPRITES.add(bullet)
    update(ALL_BULLETS)
    render(background)