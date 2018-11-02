from pico2d import *
import game_world

class Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Bullet.image == None:
            Bullet.image = load_image('WhiteBloodCell_50x50.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        #self.x += self.velocity

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
