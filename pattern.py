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



# Boy Event
PATTERN1, PATTERN2, PATTERN3, PATTERN4 = range(4)

key_event_table = {
}


# 이거 쓰면 값을 받아 올 수 있음
#boy = main_state.get_boy()


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

        print('111111111111')

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


            if a < 20:
                Pattern.fireSound.play(1)
                #bullet = Bullet(x, y, radius, degree, delta_radius, delta_degree)
                if a < 10:
                    for n in range(30):
                        if a % 2 == 0:
                            Pattern.fire(bullet_xpos, bullet_ypos, 0, -6 * n, bullet_speed, 0)
                        else:
                            Pattern.fire(bullet_xpos, bullet_ypos, 0, -6 * n + 3, bullet_speed, 0)
                else:
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
        Pattern.add_time = 0
        Pattern.current_time = get_time()
        print('22222222222222222')

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

        if Pattern.add_time >= 0.8:
            Pattern.add_time = 0
            #bullet = Bullet(x, y, radius, degree, delta_radius, delta_degree)
            if a < 20:
                k = a % 7


                if k == 0:
                    #Pattern.draw_square(bullet_amount, bullet_xpos, bullet_ypos, 0)
                    Pattern.draw_square(bullet_xpos, bullet_ypos, 0)

                if a > 4:
                    game_world.remove_object_in_layer(2)
                    print('지으ㅏ져러')

                a += 1
            else:
                Pattern.add_event(PATTERN3)
        pass

    @staticmethod
    def draw(Pattern):
        pass


class Pattern3:

    @staticmethod
    def enter(Pattern, event):
        global bullet
        global a, start_time
        Pattern.add_time = 0
        Pattern.current_time = get_time()

        print('33333333333333333')
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
            bullet_ypos = 600
            bullet_move_down = -90


            if a < 25:
                if a < 4:
                    for n in range(bullet_amount):
                        if n != 2 and n != 3 and n != 10 and n != 11:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0)

                elif (4 == a ) or a == 14 or (a == 9 ):
                    for n in range(bullet_amount):
                        if n < 2 or n > 11:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0)

                elif 5 <= a and a < 9:
                    for n in range(bullet_amount):
                        if n != 6 and n != 7 :
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0)

                elif a == 11 or a == 10:
                    for n in range(bullet_amount):
                        if n != 2 and n != 3 and n != 9 and n != 10:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0)

                elif a == 12:
                    for n in range(bullet_amount):
                        if n != 2 and n != 3 and n != 9:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0)

                elif a == 13:
                    for n in range(bullet_amount):
                        if n == 0 or n == 1 or n == 9 or n == 12:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0)

                elif a == 15 or a == 16:
                    for n in range(bullet_amount):
                        if n != 7 and n != 8 and n != 10 and n != 11:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0)

                elif a == 17:
                    for n in range(bullet_amount):
                        if n != 10 and n != 11:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0)

                elif 18 <= a and a < 23 :
                    for n in range(bullet_amount):
                        if n < 23 - a or n == 12:
                            Pattern.fire(seprate * (n), bullet_ypos, 0, bullet_move_down, bullet_speed, 0)

                a += 1

            else :
                Pattern.add_event(PATTERN4)
        pass

    @staticmethod
    def draw(Pattern):
        pass


class Pattern4:

    @staticmethod
    def enter(Pattern, event):
        global bullet
        global a, start_time
        Pattern.add_time = 0
        Pattern.current_time = get_time()

        print('4444444444444')
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

            if a < 13 * 4:
                k = a % 13
                Pattern.draw_DIE(k, bullet_xpos, bullet_ypos, bullet_speed)
                if k == 7:
                    for n in range(40):
                        for i in range(6):
                            Pattern.fire(bullet_xpos, bullet_ypos, 0, 90 * i + n, bullet_speed, 0.5)
                if k == 10:
                    for n in range(40):
                        for i in range(6):
                            Pattern.fire(bullet_xpos, bullet_ypos, 0, 60 * i + n, bullet_speed, 0.7)

                a += 1

            else :
                Pattern.add_event(PATTERN1)
        pass
    def draw(Pattern):
        pass
next_state_table = {
    Pattern1: {PATTERN1: Pattern1, PATTERN2: Pattern2, PATTERN3: Pattern3 , PATTERN4: Pattern4},
    Pattern2: {PATTERN1: Pattern1, PATTERN2: Pattern2, PATTERN3: Pattern3 , PATTERN4: Pattern4},
    Pattern3: {PATTERN1: Pattern1, PATTERN2: Pattern2, PATTERN3: Pattern3 , PATTERN4: Pattern4},
    Pattern4: {PATTERN1: Pattern1, PATTERN2: Pattern2, PATTERN3: Pattern3 , PATTERN4: Pattern4}
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

        self.bgm = load_music('toby_fox_UNDERTALE_Soundtrack_100_MEGALOVANIA.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

        self.fireSound = load_wav('pickup.wav')
        self.fireSound.set_volume(32)

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

    def fire(self, x = 300, y = 500, radius = 0, degree = 0, delta_radius = 0.0, delta_degree = 0):

        bullet = Bullet(x, y, radius, degree, delta_radius, delta_degree)
        game_world.add_object(bullet, 2)

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
                self.fire(bullet_xpos, bullet_ypos, 0, -115 + n, bullet_speed, 0)  # D
                self.fire(bullet_xpos, bullet_ypos, 0, -90 + n / 2, bullet_speed, 0)  # I
                self.fire(bullet_xpos, bullet_ypos, 0, -90 - n / 2, bullet_speed, 0)  # I

        if 1 <= k and k <= 3:
            self.fire(bullet_xpos, bullet_ypos, 0, -115 + 12, bullet_speed, 0)  # D

        if k == 0 or k == 2 or k == 4:
            for n in range(10):
                self.fire(bullet_xpos, bullet_ypos, 0, -75 + n, bullet_speed, 0)  # E

        if k < 5:
            self.fire(bullet_xpos, bullet_ypos, 0, -115, bullet_speed, 0)  # D
            self.fire(bullet_xpos, bullet_ypos, 0, -90, bullet_speed, 0)  # I
            self.fire(bullet_xpos, bullet_ypos, 0, -75, bullet_speed, 0)  # E
            pass

    # 사각형 만드는 함수 만들려고 하던 중임 - 미완
    def draw_square(self, bullet_xpos, bullet_ypos, bullet_speed):
        # 사각형 크기 bullet_amount X seprate
        bullet_amount = 11
        seprate = 20
        temp = 250

        for n in range(bullet_amount):
            width_x = bullet_xpos - seprate * 5 + seprate * n
            width_y1 = bullet_ypos + seprate * 5
            width_y2 = bullet_ypos - seprate * 5

            height_y = bullet_xpos - seprate * 5 + seprate * n
            height_x1 = bullet_xpos + seprate * 5
            height_x2 = bullet_xpos - seprate * 5

            if n != 5 and n != 4 and n != 6:
                # 가로
                self.fire(width_x, width_y1, 0, -90, bullet_speed, 0)
                self.fire(width_x, width_y2, 0, -90, bullet_speed, 0)
                # 세로
                self.fire(height_x1, bullet_ypos - seprate * 5 + seprate * n, 0, -90, bullet_speed, 0)
                self.fire(height_x2, bullet_ypos - seprate * 5 + seprate * n, 0, -90, bullet_speed, 0)


#for n in range(bullet_amount):
#    seprate = 50
#    Pattern.fire(300 - seprate * 2 + seprate * n, 600, 0, -90, 1, 0)
#    Pattern.fire(300 - seprate * 2 + seprate * n, 800, 0, -90, 1, 0)
#    Pattern.fire(400, 800 - seprate * n, 0, -90, 1, 0)
#    Pattern.fire(200, 800 - seprate * n, 0, -90, 1, 0)