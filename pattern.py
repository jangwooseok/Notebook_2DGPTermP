import game_framework
from pico2d import *
from bullet import Bullet
import math
import random

import game_world

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# 내가 추가함
PI = 3.141592
PATTERN1_TIME_PER_RADIAN = 1 * PI /60

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)
PATTERN1_LEFT, PATTERN1_RIGHT = range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# States
class Pattern1:

    @staticmethod
    def enter(Pattern, event):
        global bullet
        bullet = [Bullet() for i in range(200)]
        for i in range(200):
            bullet[i].x = 300
            bullet[i].y = 800
            bullet[i].radian =  PI * 0.3 * i
            bullet[i].radius = i
        pass

    @staticmethod
    def exit(Pattern, event):
        pass

    @staticmethod
    def do(Pattern):
        for i in range(200):
            bullet[i].radian += PATTERN1_TIME_PER_RADIAN * game_framework.frame_time
            bullet[i].radius += 1
        pass

    @staticmethod
    def draw(Pattern):
        for i in range(200):
            bullet[i].image.draw(bullet[i].x + + bullet[i].radius * math.cos(bullet[i].radian), bullet[i].y + bullet[i].radius * math.sin(bullet[i].radian))








next_state_table = {
    Pattern1: {}
}

class Pattern:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.radius = 0
        self.radian = -1 * PI
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('WhiteBloodCell_50x50.png')
        self.font = load_font('ENCR10B.TTF',16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = Pattern1
        self.cur_state.enter(self, None)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        # fill here

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def add_bullet(self):
        game_world.add_object(bullet, 1)
