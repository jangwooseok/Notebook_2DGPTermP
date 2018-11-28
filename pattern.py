import game_framework
from pico2d import *
from bullet import Bullet
from bacteria import Bacteria

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


TYPE_BULLET = 0
TYPE_BLOCK = 1
TYPE_WARNNING = 2



# Boy Event
PATTERN1, PATTERN2, PATTERN3, PATTERN4, PATTERN5 = range(5)

key_event_table = {
}


# 이거 쓰면 값을 받아 올 수 있음
#boy = main_state.get_boy()



# States

#엇갈리게
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

        bullet_speed = 2.0
        bullet_ypos = 800
        bullet_xpos = 300

        if Pattern.add_time >= 1.0:
            Pattern.add_time = 0


            if a < 12:
                #bullet = Bullet(x, y, radius, degree, delta_radius, delta_degree)
                if a < 5:
                    for n in range(30):
                        if a % 2 == 0:
                            Pattern.fire(bullet_xpos, bullet_ypos, 0, -6 * n, bullet_speed, 0)
                        else:
                            Pattern.fire(bullet_xpos, bullet_ypos, 0, -6 * n + 3, bullet_speed, 0)
                elif a < 12:
                    for n in range(30):
                        if a % 2 == 0:
                            Pattern.fire(bullet_xpos, bullet_ypos, 0, -6 * n, bullet_speed, 0.1)
                        else:
                            Pattern.fire(bullet_xpos, bullet_ypos, 0, -6 * n + 3, bullet_speed, -0.1)
                a += 1
            else:
                Pattern.add_event(PATTERN2)
                pass
        pass
    def draw(Pattern):
        pass


# 유비트처럼 테두리
class Pattern2:

    @staticmethod
    def enter(Pattern, event):
        global bullet
        global a, start_time
        global safeZoneX, safeZoneY
        Pattern.add_time = 0
        Pattern.current_time = get_time()

        safeZoneX = [0,0,0]
        safeZoneY = [0,0,0]

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
        global safeZoneX, safeZoneY
        Pattern.add_time += get_time() - Pattern.current_time
        Pattern.current_time = get_time()

        bullet_speed = 0.0
        bullet_ypos = 800
        bullet_xpos = 300



        if Pattern.add_time >= 0.8:
            Pattern.add_time = 0
            #bullet = Bullet(x, y, radius, degree, delta_radius, delta_degree)
            if a < 32:
                k = a % 15

                if a == 5 or a == 5 + 8 or a == 5 + 16 :
                    for n in range(3):
                        safeZoneX[n] = random.randint(0, 2)
                        safeZoneY[n] = random.randint(0, 4)

                    for w in range(3):
                        for h in range(5):
                            if not(w == safeZoneX[0] and h == safeZoneY[0]) and not(w == safeZoneX[1] and h == safeZoneY[1]) and not(w == safeZoneX[2] and h == safeZoneY[2]):
                                Pattern.fire_not_collide(w * 200 + 100, h * 200 + 100, 0, 0, 0, 0, TYPE_WARNNING)

                if a == 6 or a == 6 + 8 or a == 6 + 16 :
                    #Pattern.draw_square(bullet_amount, bullet_xpos, bullet_ypos, 0)
                    for h in range(5):
                        for w in range(3):
                            Pattern.draw_empty_square(200 * w + 100, 200 * h +100, bullet_speed)
                        #Pattern.draw_square(bullet_xpos, bullet_ypos, 0)

                elif a == 11 or a == 11 + 8 or a == 11 + 16:
                    game_world.remove_object_in_layer(2)

                    bullet_amount = 5
                    seprate = 35

                    for h in range(5):
                        for w in range(3):
                            if not(w == safeZoneX[0] and h == safeZoneY[0]) and not(w == safeZoneX[1] and h == safeZoneY[1]) and not(w == safeZoneX[2] and h == safeZoneY[2]):
                                bullet_xpos = w * 200 + 100
                                bullet_ypos = h * 200 + 100
                                Pattern.draw_fill_square(bullet_xpos, bullet_ypos, bullet_amount, seprate)

                elif a == 13 or a == 13 + 8 or a == 13 + 16 :
                    game_world.remove_object_in_layer(2)

                a += 1
            else:
                Pattern.add_event(PATTERN3)
        pass

    @staticmethod
    def draw(Pattern):
        pass

#미로
class Pattern3:

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
        global bullet, bacteria
        global start_time, a
        Pattern.add_time += get_time() - Pattern.current_time
        Pattern.current_time = get_time()
        if Pattern.add_time >= 0.6:
            Pattern.add_time = 0
            #bullet = Bullet(x, y, radius, degree, delta_radius, delta_degree)
            seprate = 50

            bullet_amount = 13
            bullet_speed = 1.5
            bullet_ypos = 800
            bullet_move_down = -90


            if a < 30:
                if a < 4:
                    for n in range(bullet_amount):
                        if n != 2 and n != 3 and n != 10 and n != 11:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0, TYPE_BLOCK)

                elif (4 == a ) or a == 14 or (a == 9 ):
                    for n in range(bullet_amount):
                        if n < 2 or n > 11:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0, TYPE_BLOCK)

                elif 5 <= a and a < 9:
                    for n in range(bullet_amount):
                        if n != 6 and n != 7 :
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0, TYPE_BLOCK)

                elif a == 11 or a == 10:
                    for n in range(bullet_amount):
                        if n != 2 and n != 3 and n != 9 and n != 10:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0, TYPE_BLOCK)
                elif a == 12:
                    for n in range(bullet_amount):
                        if n != 2 and n != 3 and n != 9:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0, TYPE_BLOCK)

                elif a == 13:
                    for n in range(bullet_amount):
                        if n == 0 or n == 1 or n == 9 or n == 12:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0, TYPE_BLOCK)

                elif a == 15 or a == 16:
                    for n in range(bullet_amount):
                        if n != 7 and n != 8 and n != 10 and n != 11:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0, TYPE_BLOCK)

                elif a == 17:
                    for n in range(bullet_amount):
                        if n != 10 and n != 11:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0, TYPE_BLOCK)

                elif 18 <= a and a < 23 :
                    for n in range(bullet_amount):
                        if n < 23 - a or n == 12:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0, TYPE_BLOCK)

                a += 1

            else :
                Pattern.add_event(PATTERN4)
        pass

    @staticmethod
    def draw(Pattern):
        pass

#글자
class Pattern4:

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
        global bullet, bacteria
        global start_time, a
        Pattern.add_time += get_time() - Pattern.current_time
        Pattern.current_time = get_time()
        if Pattern.add_time >= 0.25:
            Pattern.add_time = 0
            #bullet = Bullet(x, y, radius, degree, delta_radius, delta_degree)
            seprate = 50

            bullet_speed = 2.0
            bullet_ypos = 800

            bullet_xpos = 300

            if a < 13 * 4 + 30:
                k = a % 13
                if a < 53:
                    Pattern.draw_DIE(k, bullet_xpos, bullet_ypos, bullet_speed)
                    if k == 7:
                        for n in range(15):
                            for i in range(5):
                                Pattern.fire(bullet_xpos, bullet_ypos, 0, 75 * i + 3 * n, bullet_speed, -0.4)
                    if k == 10:
                        for n in range(15):
                            for i in range(6):
                                Pattern.fire(bullet_xpos, bullet_ypos, 0, 60 * i + 3 * n, bullet_speed, 0.7)

                a += 1
            else :
                Pattern.add_event(PATTERN5)
        pass
    def draw(Pattern):
        pass


class Pattern5:

    @staticmethod
    def enter(Pattern, event):
        global bullet
        global a, start_time
        global safeZoneX, safeZoneY
        Pattern.add_time = 0
        Pattern.current_time = get_time()

        safeZoneX = [0,0,0]
        safeZoneY = [0,0,0]

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
        global safeZoneX, safeZoneY
        Pattern.add_time += get_time() - Pattern.current_time
        Pattern.current_time = get_time()

        bullet_speed = 0.0
        bullet_ypos = 300
        bullet_xpos = 300

        bullet_amount = 11
        seprate = 3

        right = 0
        up = 90
        left = 180
        down = 270

        if Pattern.add_time >= 0.8:
            Pattern.add_time = 0
            #bullet = Bullet(x, y, radius, degree, delta_radius, delta_degree)
            if a < 70:

                bullet_amount = 11

                if a == 0:
                    seprate = 60
                elif a == 1:
                    seprate = 50
                elif a == 2:
                    seprate = 40
                elif a == 3:
                    seprate = 35
                elif a == 4:
                    seprate = 30
                if a < 5:
                    game_world.remove_object_in_layer(2)
                    Pattern.draw_pattern5_empty_square(bullet_xpos, bullet_ypos, bullet_amount, seprate)

                if a == 5:
                    Pattern.pattern5_line(down, 7.3, 6, 7)

                if a == 7:
                    #pattern5_left(self, move_speed, safe): #safe = 4~8
                    Pattern.pattern5_line(left, 7.3, 4, 5)
                    Pattern.pattern5_line(left, 8.0, 4, 5)
                if a == 9:
                    Pattern.pattern5_line(left, 7.3, 4, 5)
                if a == 10:
                    Pattern.pattern5_line(left, 7.3, 4, 5)
                    Pattern.pattern5_line(right, 2.0, 6, 7)
                if a == 11:
                    Pattern.pattern5_line(left, 15.0, 4, 5)
                if a == 13:
                    Pattern.pattern5_line(up, 7.7, 4, 5)
                if 14 <= a and a <= 20:
                    Pattern.pattern5_line(right, 2.0, 4, 5)
                if a == 17:
                    Pattern.pattern5_line(down, 7.7, 4, 5)
                if a == 18:
                    Pattern.pattern5_line(up, 3.7, 4, 5)
                    Pattern.pattern5_line(up, 3.0, 5, 6)
                    Pattern.pattern5_line(up, 2.3, 6, 7)
                    Pattern.pattern5_line(up, 1.4, 7, 8)
                if a == 24:
                    Pattern.pattern5_line(down, 2.4, 7, 8)
                    Pattern.pattern5_line(right, 2.4, 4, 5)
                if a == 25:
                    Pattern.pattern5_line(down, 2.2, 6, 7)
                    Pattern.pattern5_line(right, 2.2, 5, 6)
                if a == 26:
                    Pattern.pattern5_line(down, 2.0, 5, 6)
                    Pattern.pattern5_line(right, 2.0, 6, 7)
                if a == 28:
                    Pattern.pattern5_line(left, 6.0, 7, 8)
                    Pattern.pattern5_line(up, 6.0, 4, 5)
                if a == 33:
                    Pattern.pattern5_line(up, 1.7, 6, 7)
                if a == 34:
                    Pattern.pattern5_line(down, 1.7, 6, 7)
                if 30 <= a and a <= 35:
                    Pattern.pattern5_line(left, 15.0, 7, 8)
                    Pattern.pattern5_line(up, 15.0, 4, 5)
                if a == 36:
                    Pattern.pattern5_line(down, 7.0, 5, 6)
                    Pattern.pattern5_line(up, 7.0, 5, 6)
                if a == 41 or a == 43 or a == 45:
                    Pattern.pattern5_line(down, 2.0, 5, 4)
                    Pattern.pattern5_line(up, 2.0, 7, 8)
                if a == 48:
                    Pattern.pattern5_line(down, 0.3, 0, 11)
                    Pattern.pattern5_line(up, 0.3, 0, 11)
                    Pattern.pattern5_line(left, 0.3, 0, 21)
                    Pattern.pattern5_line(right, 0.3, 0, 21)
                if a == 64:
                    game_world.remove_object_in_layer(2)


                a += 1
            else:
                Pattern.add_event(PATTERN1)
        pass

    @staticmethod
    def draw(Pattern):
        pass

next_state_table = {
    Pattern1: {PATTERN1: Pattern1, PATTERN2: Pattern2, PATTERN3: Pattern3, PATTERN4: Pattern4, PATTERN5: Pattern5},
    Pattern2: {PATTERN1: Pattern1, PATTERN2: Pattern2, PATTERN3: Pattern3, PATTERN4: Pattern4, PATTERN5: Pattern5},
    Pattern3: {PATTERN1: Pattern1, PATTERN2: Pattern2, PATTERN3: Pattern3, PATTERN4: Pattern4, PATTERN5: Pattern5},
    Pattern4: {PATTERN1: Pattern1, PATTERN2: Pattern2, PATTERN3: Pattern3, PATTERN4: Pattern4, PATTERN5: Pattern5},
    Pattern5: {PATTERN1: Pattern1, PATTERN2: Pattern2, PATTERN3: Pattern3, PATTERN4: Pattern4, PATTERN5: Pattern5}
}


class Pattern:

    def __init__(self):
        self.x, self.y = 0, 0
        self.radius = 0
        self.radian = -1 * PI
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('WhiteBloodCell_50x50.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = Pattern2
        self.cur_state.enter(self, None)

        self.add_time = 0
        self.current_time = get_time()

        self.bgm = load_music('Undertale OST_ 072 - Song That Might Play When You Fight Sans.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

        self.want_remove_bullet = False

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
        game_world.add_object(bullet, 2)

    def fire(self, x = 300, y = 500, radius = 0, degree = 0, delta_radius = 0.0, delta_degree = 0, block_type = 0):
        bullet = Bullet(x, y, radius, degree, delta_radius, delta_degree, block_type)
        game_world.add_object(bullet, 2)
    def fire_not_collide(self, x = 300, y = 500, radius = 0, degree = 0, delta_radius = 0.0, delta_degree = 0, block_type = 0):
        bullet = Bullet(x, y, radius, degree, delta_radius, delta_degree, block_type)
        game_world.add_object(bullet, 3)

    def want_remove(self):
        if self.want_remove_bullet == True:
            return True
        return False
        pass

    def get_bb(self):
        return self.radius, self.x, self.y


    def draw_DIE(self, k, bullet_xpos, bullet_ypos, bullet_speed):
        if k == 0 or k == 4:
            for n in range(10):
                self.fire(bullet_xpos, bullet_ypos, 0, -115 + n, bullet_speed, 0, TYPE_BULLET)  # D
                self.fire(bullet_xpos, bullet_ypos, 0, -90 + n / 2, bullet_speed, 0, TYPE_BULLET)  # I
                self.fire(bullet_xpos, bullet_ypos, 0, -90 - n / 2, bullet_speed, 0, TYPE_BULLET)  # I

        if 1 <= k and k <= 3:
            self.fire(bullet_xpos, bullet_ypos, 0, -115 + 12, bullet_speed, 0, TYPE_BULLET)  # D

        if k == 0 or k == 2 or k == 4:
            for n in range(10):
                self.fire(bullet_xpos, bullet_ypos, 0, -75 + n, bullet_speed, 0, TYPE_BULLET)  # E

        if k < 5:
            self.fire(bullet_xpos, bullet_ypos, 0, -115, bullet_speed, 0, TYPE_BULLET)  # D
            self.fire(bullet_xpos, bullet_ypos, 0, -90, bullet_speed, 0, TYPE_BULLET)  # I
            self.fire(bullet_xpos, bullet_ypos, 0, -75, bullet_speed, 0, TYPE_BULLET)  # E
            pass

    def draw_empty_square(self, bullet_xpos, bullet_ypos, bullet_speed):
        # 사각형 크기 bullet_amount X seprate
        bullet_amount = 11
        seprate = 20
        #bullet_amount = 5
        #seprate = 50

        for n in range(bullet_amount):
            width_x = bullet_xpos - seprate * 5 + seprate * n
            width_y1 = bullet_ypos + seprate * 5
            width_y2 = bullet_ypos - seprate * 5
#
            height_y = bullet_ypos - seprate * 5 + seprate * n
            height_x1 = bullet_xpos + seprate * 5
            height_x2 = bullet_xpos - seprate * 5

            if n != 5 and n != 4 and n != 6:
                # 가로
                self.fire(width_x, width_y1, 0, -90, bullet_speed, 0, TYPE_BLOCK)
                self.fire(width_x, width_y2, 0, -90, bullet_speed, 0, TYPE_BLOCK)
                # 세로
                self.fire(height_x1, height_y, 0, -90, bullet_speed, 0, TYPE_BLOCK)
                self.fire(height_x2, height_y, 0, -90, bullet_speed, 0, TYPE_BLOCK)

    def draw_pattern5_empty_square(self, bullet_xpos, bullet_ypos, bullet_amount, seprate):
        # 사각형 크기 bullet_amount X seprate
        bullet_speed = 0
        # bullet_amount = 5
        # seprate = 50
        temp = 250
        for n in range(bullet_amount):
            width_x = bullet_xpos - seprate * 5 + seprate * n
            width_y1 = bullet_ypos + seprate * 5
            width_y2 = bullet_ypos - seprate * 5
            #
            height_y = bullet_ypos - seprate * 5 + seprate * n
            height_x1 = bullet_xpos + seprate * 5
            height_x2 = bullet_xpos - seprate * 5
            # 가로
            self.fire(width_x, width_y1, 0, -90, bullet_speed, 0, TYPE_BLOCK)
            self.fire(width_x, width_y2, 0, -90, bullet_speed, 0, TYPE_BLOCK)
            # 세로
            self.fire(height_x1, height_y, 0, -90, bullet_speed, 0, TYPE_BLOCK)
            self.fire(height_x2, height_y, 0, -90, bullet_speed, 0, TYPE_BLOCK)

    def draw_fill_square(self, bullet_xpos, bullet_ypos, bullet_amount, seprate):

        #bullet_amount = 5
        #seprate = 35

        for n in range(bullet_amount):
            for k in range(bullet_amount):
                width_x = bullet_xpos - seprate * 2 + seprate * n
                height_y = bullet_ypos - seprate * 2 + seprate * k

                self.fire(width_x, height_y, 0, -90, 0, 0)

    def pattern5_line(self, diraction, move_speed, safe1, safe2): #safe = 4~8
        bullet_ypos = 500
        bullet_xpos = 300

        right = 0
        up = 90
        left = 180
        down = 270

        if diraction == down or diraction == up:
            bullet_amount = 13
            seprate = 50
            for n in range(bullet_amount):
                if n != safe1 and n != safe2:
                    width_x = bullet_xpos - seprate * 6 + seprate * n
                    if diraction == down:
                        height_y = 600 - 25
                    elif diraction == up:
                        height_y = 0 + 25
                    self.fire(width_x, height_y, 0, diraction, move_speed, 0)

        elif diraction == right or diraction == left:
            bullet_amount = 21
            seprate = 50
            for n in range(bullet_amount):
                if n != safe1 and n != safe2:
                    height_y = bullet_ypos - seprate * 10 + seprate * n
                    if diraction == right:
                        width_x = 0 + 25
                    elif diraction == left:
                        width_x = 600 - 25
                    self.fire(width_x, height_y, 0, diraction, move_speed, 0)


#for n in range(bullet_amount):
#    seprate = 50
#    Pattern.fire(300 - seprate * 2 + seprate * n, 600, 0, -90, 1, 0)
#    Pattern.fire(300 - seprate * 2 + seprate * n, 800, 0, -90, 1, 0)
#    Pattern.fire(400, 800 - seprate * n, 0, -90, 1, 0)
#    Pattern.fire(200, 800 - seprate * n, 0, -90, 1, 0)