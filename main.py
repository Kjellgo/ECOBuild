import random as r
import os
import time as t
import pygame as pg

#Formalia

if not pg.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

#Konstanten

TAXES_XSMALL = 20 #XSmall house taxes
TAXES_SMALL = 35 #Small house taxes
TAXES_MEDIUM = 50 #Medium house taxes
TAXES_LARGE = 75 #Large house taxes
TAXES_XLARGE = 100 #XLarge house taxes

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit(f'Could not load image "{file}" {pg.get_error()}')
    return surface.convert()


def load_sound(file):
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print(f"Warning, unable to load, {file}")
    return None

class House(pg.sprite.Sprite):
    def __init__(self, size: int = 1, *groups):


