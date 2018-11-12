import game_framework
from pico2d import *
#from math import *
import random

import game_world

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

GHOST_ASSENTION_SPEED_CMPS = 30.0
GHOST_TIME_PER_RADIAN = 4 * 3.141592 * 60
# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_DOWN, DOWN_DOWN, UP_UP, DOWN_UP = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP
}


# Boy States

class IdleState:

    @staticmethod
    def enter(bacteria, event):
        if event == RIGHT_DOWN:
            bacteria.x_velocity = RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            bacteria.x_velocity = -RUN_SPEED_PPS
        elif event == RIGHT_UP:
            bacteria.x_velocity = 0
        elif event == LEFT_UP:
            bacteria.x_velocity = 0

        elif event == UP_DOWN:
            bacteria.y_velocity = RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            bacteria.y_velocity = -RUN_SPEED_PPS
        elif event == UP_UP:
            bacteria.y_velocity = 0
        elif event == DOWN_UP:
            bacteria.y_velocity = 0
        bacteria.timer = get_time()

    @staticmethod
    def exit(bacteria, event):
        pass

    @staticmethod
    def do(bacteria):
        bacteria.frame = (bacteria.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    @staticmethod
    def draw(bacteria):
        bacteria.image.clip_draw(int(bacteria.frame) * 100, 0, 100, 100, bacteria.x, bacteria.y)


class RunState:

    @staticmethod
    def enter(bacteria, event):
        if event == RIGHT_DOWN:
            bacteria.x_velocity = RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            bacteria.x_velocity = -RUN_SPEED_PPS
        elif event == RIGHT_UP:
            bacteria.x_velocity = 0
        elif event == LEFT_UP:
            bacteria.x_velocity = 0

        elif event == UP_DOWN:
            bacteria.y_velocity = RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            bacteria.y_velocity = -RUN_SPEED_PPS
        elif event == UP_UP:
            bacteria.y_velocity = 0
        elif event == DOWN_UP:
            bacteria.y_velocity = 0
        bacteria.dir = clamp(-1, bacteria.x_velocity, 1)
        bacteria.dir = clamp(-1, bacteria.y_velocity, 1)
        # fill here
        pass

    @staticmethod
    def exit(bacteria, event):
        pass

    @staticmethod
    def do(bacteria):
        bacteria.frame = (bacteria.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        bacteria.x += bacteria.x_velocity * game_framework.frame_time
        bacteria.y += bacteria.y_velocity * game_framework.frame_time

        #bacteria.x = clamp(25, bacteria.x, 1600 - 25)


    def draw(bacteria):
        bacteria.image.clip_draw(int(bacteria.frame) * 100, 0, 100, 100, bacteria.x, bacteria.y)
        pass


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                UP_UP: RunState, DOWN_UP: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState},
    RunState: {RIGHT_UP: RunState, LEFT_UP: RunState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
               UP_UP: RunState, DOWN_UP: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState}
}

class Bacteria:

    def __init__(self):
        self.x, self.y = 300, 100
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('Bacteria_100x500.png')
        self.font = load_font('ENCR10B.TTF',16)
        self.dir = 1
        self.x_velocity = 0
        self.y_velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
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
        #draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        # fill here

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

