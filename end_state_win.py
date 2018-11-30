import game_framework
from pico2d import *


import main_state

name = "winendState"
image_background = None
image_bacteria = None
logo_time = 0.0

radian = 0
size = 520



def enter():
    global image_background, image_bacteria, Sound
    image_background = load_image('win.PNG')
    image_bacteria = load_image('win_bacteria.PNG')
    Sound = load_music('ending.mp3')
    Sound.set_volume(64)
    Sound.repeat_play()
    print('이김')



def exit():
    global image_win
    global image_lose

    del (image_win)
    del (image_lose)
    Sound.stop()
    pass


def update():
    global logo_time
    global radian, size
    radian += 0.01
    size -= 5
    if size <= 400:
        size = 520
    pass


def draw():
    global image_background, image_bacteria
    global radian, size
    #def clip_composite_draw(self, left, bottom, width, height, rad, flip, x, y, w = None, h = None):

    clear_canvas()
    image_background.clip_draw(0, 0, 600, 1000, 600//2, 1000//2, 600, 1000)      #(self, left, bottom, width, height, x, y, w=None, h=None):
    image_bacteria.clip_composite_draw(0, 0, 520, 520, radian, 'None', 600//2, 740, size, size)      #(self, left, bottom, width, height, x, y, w=None, h=None):
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




