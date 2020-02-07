import math
from random import choice
import config as conf
import helper as h
import element as el

# don't cache config
from imp import reload
reload (conf)
reload (h)
reload (el)




allElements = []

## setup bubbles
for i in range(conf.elementCount):

    speedFactor = 1 + 1 * random()
    elementMaxAge = conf.elementMaxAge / speedFactor
    maxStart = 1 - elementMaxAge

    e = el.Block();
    e.size = 0.01 + 0.025 * random();
    e.age =  0 - (maxStart * random());
    e.maxAge = elementMaxAge;
    e.x = 1 / conf.elementCount * i
    e.y = 0
    e.speed = [0, 2 * 1 / elementMaxAge * speedFactor]




    # b.age =  0 - (maxStart * random());
    #
    # b.maxAge = bubbleMaxAge;

    allElements.append(e)


for time in range(conf.animLength):
    print(str(time) + " of " + str(conf.animLength))
    newPage(conf.widht, conf.height)
    frameDuration(1/conf.fps)
    stroke(None)
    fill(0,0,0)
    rect(0,0,conf.widht,conf.height)

    translate(conf.widht * -0.54, conf.height * .53)
    scale(1.8, 1.8)
    rotate(-30)


    # fill(0,1,0)
    # rect(0,0,conf.widht,conf.height)


    for e in allElements:
        e.draw(conf.widht, conf.height);
        e.tick(1 / conf.animLength);


if conf.fps > 10:
    saveImage('./rendering/gradient' + h.nowStr() + '.mp4')
