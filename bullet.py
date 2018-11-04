from pico2d import *
import game_world

PI = 3.141592


class Bullet:
    image = None

    def __init__(self, x = 400, y = 800, radius = 0, radian = -0.5 * PI, delta_radius = 1, delta_radian = 0.01):
        self.radius = radius
        self.radian = radian
        self.delta_radius, self.delta_radian = delta_radius, delta_radian
        if Bullet.image == None:
            Bullet.image = load_image('WhiteBloodCell_50x50.png')
        self.x, self.y = x, y

    def draw(self):
        #self.image.draw(self.x, self.y)
        self.image.draw(self.x + self.radius * math.cos(self.radian), self.y + self.radius * math.sin(self.radian))


    def update(self):
        #self.x += self.velocity
        self.radian -= self.delta_radian * PI
        self.radius += self.delta_radius
        if self.radius > 1000 or self.radius < 0:
            game_world.remove_object(self)
