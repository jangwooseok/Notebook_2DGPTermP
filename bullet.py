from pico2d import *
import game_world

PI = 3.141592


class Bullet:
    image = None

    def __init__(self, x = 400, y = 800, radius = 0, degree = -90, delta_radius = 1, delta_degree = 0):
        self.radius = radius
        self.radian = degree/180 * PI
        self.delta_radius, self.delta_radian = delta_radius, delta_degree/180 * PI
        if Bullet.image == None:
            Bullet.image = load_image('WhiteBloodCell_50x50.png')
        self.x, self.y = x, y



        self.bulletX, self.bulletY = 0, 0

    def draw(self):
        #self.image.draw(self.x, self.y)
        self.image.draw( self.bulletX, self.bulletY)

    def get_bb(self):
        return 25, self.bulletX, self.bulletY

    def update(self):

        self.radius += self.delta_radius
        self.bulletX = self.x + self.radius * math.cos(self.radian)
        self.bulletY = self.y + self.radius * math.sin(self.radian)
        #if self.radius < 200:
        #    self.radian -= self.delta_radian * 0.8 * PI
        #elif self.radius > 200 and self.radius < 400:
        #    self.radian -= self.delta_radian * 0.4 * PI
        #else:
        #    self.radian -= self.delta_radian * 0.2 * PI

        self.radian -= self.delta_radian * PI * (1200 - self.radius) * 1/2400

        if self.radius > 1200 or self.radius < 0:
            game_world.remove_object(self)
