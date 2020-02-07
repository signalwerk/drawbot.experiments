import math
from random import choice
import config as conf
import helper as h
import element as el
from imp import reload

# don't cache config, element and Helpers
# dirty but works
reload (conf)
reload (h)
reload (el)


# all elements are stored
allElements = []

## setup elements
for i in range(conf.elementCount):

    # random speed
    speedFactor = 1 + 1 * random()

    # maximum age for element
    elementMaxAge = conf.elementMaxAge / speedFactor

    # when does it appear on stage
    maxStart = 1 - elementMaxAge

    # create block with some randomness
    e = el.Block();
    e.size = 0.01 + 0.025 * random();
    e.age =  0 - (maxStart * random());
    e.maxAge = elementMaxAge;
    e.x = 1 / conf.elementCount * i
    e.y = 0
    e.speed = [0, 2 * 1 / elementMaxAge * speedFactor]

    allElements.append(e)


for time in range(conf.animLength):
    print(str(time) + " of " + str(conf.animLength))
    newPage(conf.widht, conf.height)
    frameDuration(1/conf.fps)
    stroke(None)
    fill(0,0,0)
    rect(0,0,conf.widht,conf.height)

    # this is manually tested
    translate(conf.widht * -0.54, conf.height * .53)
    scale(1.8, 1.8)
    rotate(-30)

    for e in allElements:
        e.draw(conf.widht, conf.height);
        e.tick(1 / conf.animLength);

    # if (time == round(conf.animLength/2)):
    #     saveImage('./rendering/gradient' + h.nowStr() + '.png')

if conf.fps > 10:
    saveImage('./rendering/gradient' + h.nowStr() + '.mp4')
    # saveImage('./rendering/gradient' + h.nowStr() + '.pdf')
