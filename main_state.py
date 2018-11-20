import random
import json
import os

from pico2d import *
import game_framework
import game_world

from pattern import Pattern
from bacteria import Bacteria
from bullet import Bullet


name = "MainState"

boy = None

def enter():
    global pattern, bacteria
    global bullet
    pattern = Pattern()
    bacteria = Bacteria()
    game_world.add_object(pattern, 0)
    game_world.add_object(bacteria, 1)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass

def collide(a, b):
    radius_a, xPosition_a, yPosition_a = a.get_bb()
    radius_b, xPosition_b, yPosition_b = b.get_bb()

    isCollide = (xPosition_a - xPosition_b)**2 + (yPosition_a - yPosition_b)**2 - (radius_a + radius_b)**2

    if isCollide <= 0:
        return True
    return False



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            bacteria.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


    if collide(bacteria, pattern):
        print("COLLISION")

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






