import pygame as pg

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((40,40))
        self.rect = self.image.get_rect()
        self.acc = vec()
        self.vel = vec()
        
    def checkIfHit(self, ALL_BULLETS):
        hits = pg.sprite.spritecollide(self, ALL_BULLETS, False)
        for hit in hits:
            if self.color != hit.color:
                print('shot')
                hit.kill()