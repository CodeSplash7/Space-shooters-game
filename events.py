import pygame as pg

def events(running):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
    return True