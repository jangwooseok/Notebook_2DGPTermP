import game_framework
from pico2d import *


import main_state

name = "TitleState"
image = None
logo_time = 0.0

KEY_DOWN = range(1)

key_event_table = {
    (SDL_KEYDOWN) : KEY_DOWN
}


def enter():
    global image, titleSound
    global running

    running = True
    image = load_image('title.png')

    titleSound = load_music('title_BGM.mp3')
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
    global running


    if (logo_time > 2.0):
        logo_time = 0
        game_framework.quit()
    delay(0.01)
    logo_time += 0.01


    pass


def draw():
    global image
    clear_canvas()
    image.clip_draw(0, 0, 1690, 1122, 600//2, 1000//2, 600, 1000)      #(self, left, bottom, width, height, x, y, w=None, h=None):
    update_canvas()
    pass

next_state_table = {
   KEY_DOWN: main_state
}


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            game_framework.change_state(main_state)

    pass


def pause(): pass


def resume(): pass




