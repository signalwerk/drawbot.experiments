import config as conf
from random import choice
import drawBot

from imp import reload
reload (conf)


possibleColors = [
    [163, 163, 163], # gray
    [222, 27, 27], # red
    [25, 183, 227], # blue
    [240, 240, 40], # yellow
    [255, 255, 255] # white
]


class Block:
    """A simple example class"""

    age = 0
    maxAge = 0
    size = 1
    speed = [0, 0]
    color = [0,0,0]
    x = 0
    y = 0

    def __init__(self):
        # self.size = 0.01 + 0.1 * random() #* random()
        self.color = choice(possibleColors)

    def tick(self, t):
        self.age = self.age + t
        if (self.age >= 0 and self.age < self.maxAge) :
            self.x = self.x + self.speed[0] * t
            self.y = self.y + self.speed[1] * t

    def draw(self, widht, height):
        if (self.age >= 0 and self.age < self.maxAge) :
            drawBot.stroke(self.color[0]/255,self.color[1]/255,self.color[2]/255);
            drawBot.fill(None);
            drawBot.strokeWidth(self.size * widht)

            scaleX = self.x * widht
            scaleY = self.y * height
            drawBot.line((scaleX, scaleY), (scaleX, scaleY - height))
