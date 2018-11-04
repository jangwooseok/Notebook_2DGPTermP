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
}


# States
class Pattern1:

    @staticmethod
    def enter(Pattern, event):
        global bullet
        global a, start_time
        Pattern.add_time = 0
        Pattern.current_time = get_time()

        a = 0
        start_time = get_time()
        pass

    @staticmethod
    def exit(Pattern, event):
        pass

    @staticmethod
    def do(Pattern):
        global bullet
        global start_time, a
        Pattern.add_time += get_time() - Pattern.current_time
        Pattern.current_time = get_time()
        if Pattern.add_time >= 0.5:
            Pattern.add_time = 0
            if a < 50:
                Pattern.fire(300, 400, 0, -0.5 * PI, 1, 0.01)
                Pattern.fire(300, 400, 0, 0.5 * PI, 1, 0.01)
                Pattern.fire(100, 600, 0, -0.5 * PI, 1, 0.01)
                Pattern.fire(100, 600, 0, 0.5 * PI, 1, 0.01)
                Pattern.fire(100, 600, 0, -1.0 * PI, 1, 0.01)
                Pattern.fire(100, 600, 0, 0.0 * PI, 1, 0.01)
                Pattern.fire(500, 600, 0, -0.5 * PI, 1, -0.01)
                Pattern.fire(500, 600, 0, 0.5 * PI, 1, -0.01)
                Pattern.fire(500, 600, 0, -1.0 * PI, 1, -0.01)
                Pattern.fire(500, 600, 0, 0.0 * PI, 1, -0.01)
                Pattern.fire(100, 1000 + 25, 0, -0.5 * PI, 3, 0.00)
                Pattern.fire(200, 1000 + 25, 0, -0.5 * PI, 3, 0.00)
                Pattern.fire(300, 1000 + 25, 0, -0.5 * PI, 3, 0.00)
                Pattern.fire(400, 1000 + 25, 0, -0.5 * PI, 3, 0.00)
                Pattern.fire(500, 1000 + 25, 0, -0.5 * PI, 3, 0.00)
                #Pattern.fire(0 - 25, 500 - 30 * a, 0, 0 * PI, 3, 0.00)
                a += 1
        pass

    @staticmethod
    def draw(Pattern):
        pass


class Pattern2:

    @staticmethod
    def enter(Pattern, event):
        global bullet
        global a, start_time
        Pattern.add_time = 0
        Pattern.current_time = get_time()

        a = 0
        start_time = get_time()
        pass

    @staticmethod
    def exit(Pattern, event):
        pass

    @staticmethod
    def do(Pattern):
        global bullet
        global start_time, a
        Pattern.add_time += get_time() - Pattern.current_time
        Pattern.current_time = get_time()
        if Pattern.add_time >= 0.5:
            Pattern.add_time = 0
            if a < 50:
                Pattern.fire(300, 800, 0, -0.5 * PI, 1, 0.01)
                a += 1
        pass

    @staticmethod
    def draw(Pattern):
        pass




next_state_table = {
    Pattern1: {},
    Pattern2: {}
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

        self.add_time = 0
        self.current_time = get_time()


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
        # fill here

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def add_bullet(self):
        game_world.add_object(bullet, 1)

    def fire(self, x = 300, y = 500, radius = 0, radian = 0.0, delta_radius = 0.0, delta_radian = 0.0):
        bullet = Bullet(x, y, radius, radian, delta_radius, delta_radian)
        game_world.add_object(bullet, 1)

