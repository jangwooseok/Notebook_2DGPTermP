from pico2d import *
import game_world
import main_state

#안된다 이유를 모르겠다
#from pattern import Pattern


PI = 3.141592

COLLIDE_SIZE = 21

TYPE_BULLET = 0
TYPE_BLOCK = 1
TYPE_WARNNING = 2
TYPE_HEART = 3

class Bullet:
    image_bullet = None
    image_block = None
    image_warning = None
    image_heart = None
    image_drug = None

    def __init__(self, x = 400, y = 800, radius = 0, degree = -90, delta_radius = 1, delta_degree = 0, type = TYPE_BULLET):
        self.radius = radius
        self.radian = degree/180 * PI
        self.delta_radius, self.delta_radian = delta_radius, delta_degree/180 * PI
        self.type = type

        if Bullet.image_bullet == None:
            Bullet.image_bullet = load_image('WhiteBloodCell_50x50.png')
        if Bullet.image_block == None:
            Bullet.image_block = load_image('block_50x50.png')
        if Bullet.image_warning == None:
            Bullet.image_warning = load_image('warnning_150x150.PNG')
        if Bullet.image_heart == None:
            Bullet.image_heart = load_image('heart.PNG')

        self.x, self.y = x, y

        self.bulletX, self.bulletY = 0, 0
        self.heart_opacity = 0

    def draw(self):
        #self.image.draw(self.x, self.y)
        if self.type == TYPE_BULLET:
            self.image_bullet.clip_draw(0, 0, 50, 50, self.bulletX, self.bulletY, COLLIDE_SIZE * 2 + 5, COLLIDE_SIZE * 2 + 5)
        if self.type == TYPE_BLOCK:
            self.image_block.draw(self.bulletX, self.bulletY)
        if self.type == TYPE_WARNNING:
            self.image_warning.opacify(0.3)
            self.image_warning.draw(self.bulletX, self.bulletY)
        if self.type == TYPE_HEART:
            self.image_heart.opacify(self.heart_opacity)
            self.image_heart.draw(self.bulletX, self.bulletY)

    def get_bb(self):
        if self.type == TYPE_HEART:
            return 200, self.bulletX, self.bulletY
        return COLLIDE_SIZE, self.bulletX, self.bulletY

    def update(self):
        if self.type == TYPE_HEART:
            if self.heart_opacity < 1:
                self.heart_opacity += 0.005

        self.radius += self.delta_radius
        self.bulletX = self.x + self.radius * math.cos(self.radian)
        self.bulletY = self.y + self.radius * math.sin(self.radian)

        self.radian -= self.delta_radian * PI * (1200 - self.radius) * 1/2800

        if self.radius > 900 or self.radius < 0:
            game_world.remove_object(self)
