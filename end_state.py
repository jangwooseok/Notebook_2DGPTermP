import game_framework
from pico2d import *


import main_state

name = "endState"
image = None
logo_time = 0.0





def enter():
    global image, titleSound
    image = load_image('end.png')
    titleSound = load_music('ending.mp3')
    titleSound.set_volume(64)
    titleSound.repeat_play()
    pass


def exit():
    global image
    del (image)
    titleSound.stop()
    pass


def update():
    global logo_time

    pass


def draw():
    global image
    clear_canvas()
    image.opacify(0.3)
    image.clip_draw(0, 0, 1690, 1122, 600//2, 1000//2, 600, 1000)      #(self, left, bottom, width, height, x, y, w=None, h=None):
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(main_state)

    pass


def pause(): pass


def resume(): pass




