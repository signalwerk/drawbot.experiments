from random import choice
import datetime
import math


def s(x):
  return x * scaler

def rand():
    return random() * scaler

def nowStr():
    return datetime.datetime.now().strftime("%Y-%m-%d--%H-%M.%S")

def sinOffset(t, max):
    return math.sin(math.tau * 1 / max * t)

# canvas setup
scaler = 1000;
fps = 24
bubbleCount = 300
debug = False

if (debug):
    fps = 1
    bubbleCount = 20


animLength = 18 * fps
fSize = s(0.1)

widht = s(1);
height = round(s(1 / 16 * 9));





possibleTexts = ["t", "y", "p", "o", "*", ",", ")", "_", ".", "t", "y", "p", "o" ]


## bubbles start
## bubbleX = map(rand, range(bubbleCount))
## bubbleY = map(rand, range(bubbleCount))

class Bubble:
    """A simple example class"""
    size = 1
    speed = [0, 0]
    age = 0
    maxAge = 0
    offset = [0, 0]
    x = 0
    y = 0
    text = "×"
    frequency = 1;
    z = 0


    # def __init__(self):
    #     self.size = rand()

    def tick(self):
        self.age = self.age + 1
        if (self.age >= 0 and self.age < self.maxAge) :
            self.x = self.x + self.speed[0]
            self.y = self.y + self.speed[1]

    def draw(self):
        if (self.age >= 0 and self.age < self.maxAge) :


            with savedState():
                translate(self.offset[0],self.offset[1])

                # if debug:
                #     fill(1,0,0)
                #     rect(0,0,s(.1),s(1));

                with savedState():
                    # strokeWidth(s(0.001));
                    # stroke(0,0,0);
                    # fill(None);
                    # oval(0,self.y,self.size,self.size);


                    stroke(None);
                    fill(0,0,0);

                    currentFontsize = fSize / self.maxAge * self.age * self.size
                    sinOffsetX = sinOffset(self.age, self.maxAge / self.frequency) * self.speed[0]

                    font("AkzidenzGroteskPro-Super")
                    fontSize(currentFontsize)

                    textBox(self.text, (0 - fSize + sinOffsetX, self.y - fSize / 2, fSize * 2, fSize), align="center")

                    # if (round(currentFontsize * 2) > 0):
                    #     im = ImageObject()
                    #     with im:
                    #
                    #         # set a size for the image
                    #
                    #         size(round(currentFontsize * 2), round(currentFontsize * 2))
                    #
                    #         font("AkzidenzGroteskPro-Super")
                    #         fontSize(currentFontsize)
                    #
                    #         # draw something
                    #         # fill(1, 0, 0)
                    #         # rect(0, 0, currentFontsize * 2, currentFontsize * 2)
                    #         fill(0)
                    #         fontSize(currentFontsize)
                    #         # textBox(self.text, (0, 0, currentFontsize * 2, currentFontsize), align="center")
                    #
                    #         textBox(self.text, (0, 0 - currentFontsize / 2.5, currentFontsize * 2, currentFontsize * 2), align="center")
                    #         #text("Hello World", (0, currentFontsize * 2))
                    #
                    #     # draw in the image in the main context
                    #     im.gaussianBlur(self.z)
                    #
                    #     image(im, (0 - currentFontsize, self.y - currentFontsize))





allBubbles = []

## setup bubbles
for i in range(bubbleCount):


    bubbleMaxAge = animLength / 6

    # bubbleSpeed = (height * .7 + height * .3 * random() )/ bubbleMaxAge
    bubbleSpeed = (height * .7 + height * .3 * random() )/ bubbleMaxAge


    maxStart = animLength - bubbleMaxAge
    b = Bubble();
    b.age =  0 - (maxStart * random());
    b.maxAge = bubbleMaxAge;


    frequencyScaler = 0.7 * random() + 0.3
    b.size = 1 - frequencyScaler;
    b.frequency = 7 * frequencyScaler

    b.z = round(random() * s(0.003))

    b.speed = [s(0.01) * frequencyScaler, bubbleSpeed];


    b.offset = [s(1 / (bubbleCount - 1) * i),0];
    b.text = choice(possibleTexts)
    allBubbles.append(b)

## drawer
def bubbles(t):
    for b in allBubbles:
        b.draw();
        b.tick();

def gState():
    stroke(None)
    fill(1,1,1)
    rect(0,0,widht,height)




filenameExt = nowStr()

for time in range(animLength):
    print(str(time) + " of " + str(animLength))
    newPage(widht, height)
    gState()
    frameDuration(1/fps)

    with savedState():
        bubbles(time)

    # saveImage("./typo-bubbles__%d.png" % time)
    # saveImage('./typo-bubbles' + filenameExt + "___" + str(time) + '.png')



if animLength > 20:
    saveImage('./rendering/typo-bubbles' + nowStr() + '.mp4')





# print(list(bubbleX))
