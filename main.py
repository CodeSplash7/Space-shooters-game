from turtle import back
import pygame as pg
from settings import *
from events import *
from player1 import Player1
from player2 import Player2

SCREEN = pg.display.set_mode(WINSIZE)
CLOCK = pg.time.Clock()
pg.init()
pg.mixer.init()

def update():
    ALL_SPRITES.update()
    
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
player1 = Player1(WINSIZE)
ALL_SPRITES.add(player1)
player2 = Player2(WINSIZE)
ALL_SPRITES.add(player2)

running = True
while running:
    CLOCK.tick(FPS)
    running = events(running)
    update()
    render(background)