import random

from pico2d import *


class InfiniteBackground:


    def __init__(self):
        self.image = load_image('ground_600x3000.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()

        self.y = 0
        self.h1 = 1000
        self.h2 = 0

        self.bgm = load_music('Undertale OST_ 072 - Song That Might Play When You Fight Sans.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()


    def draw(self):
        self.image.clip_draw(0, 0, 600, 3000, 0, 0, 600, 1000)                        # quadrant 3

        #self.image.clip_draw(0, self.y, 600, self.y + self.h1, 0, self.y, 600, self.y + self.h1)                        # quadrant 3
        #self.image.clip_draw(0, 1000 - self.y, 600, self.h2, 0, 0, 1200, self.h2)                        # quadrant 3



    def update(self):
        self.y += 1
        if self.y + 1000 > 3000:
            self.h2 = self.y + 1000 - 3000
            self.h1 -= self.h2
        if self.y >= 3000:
            self.h2 = 0
            self.h1 = 1000



    def handle_event(self, event):
        pass





