import game_framework
from pico2d import *


import main_state

name = "loseendState"
image = None
logo_time = 0.0


def enter():
    global image, Sound
    image = load_image('end.png')
    Sound = load_music('ending.mp3')
    Sound.set_volume(64)
    Sound.repeat_play()


def exit():
    global image

    del (image)

    Sound.stop()



def update():
    global logo_time
    pass


def draw():
    global image
    clear_canvas()
    image.clip_draw(0, 0, 600, 1000, 600//2, 1000//2, 600, 1000)      #(self, left, bottom, width, height, x, y, w=None, h=None):
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




