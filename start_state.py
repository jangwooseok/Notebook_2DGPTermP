import game_framework
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image, startSound
    image = load_image('stop.png')

    startSound = load_music('start.mp3')
    startSound.set_volume(64)
    startSound.play(1)

    pass


def exit():
    global image
    del (image)

    pass


def update():

    global logo_time
    if (logo_time > 1.0):
        logo_time = 0
        game_framework.quit()
    delay(0.01)
    logo_time += 0.01

    pass


def draw():
    global image
    clear_canvas()
    image.clip_draw(0, 0, 600, 1000, 600//2, 1000//2, 600, 1000)
    update_canvas()
    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




