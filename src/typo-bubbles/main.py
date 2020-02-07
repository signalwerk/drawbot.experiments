from random import choice
import datetime
import math

# helper functions
def s(x):
  return x * scaler

def rand():
    return random() * scaler

def nowStr():
    return datetime.datetime.now().strftime("%Y-%m-%d--%H-%M.%S")

def sinOffset(t, max):
    return math.sin(math.tau * 1 / max * t)

# seutp animatinon 1920px@24 fps
scaler = 1920;
fps = 24

# how many bubbles
bubbleCount = 300

debug = False

# have it reduced in debug mode
if (debug):
    fps = 1
    bubbleCount = 20

# 18 sec animation
animLength = 18 * fps

# fontSize
fSize = s(0.1)
fontName = "WorkSans-Regular_Black"

# canvas setup
widht = s(1);
height = round(s(1 / 16 * 9));

# what characters do we need to draw (some appear more often)
possibleTexts = ["t", "y", "p", "o", "*", ",", ")", "_", ".", "t", "y", "p", "o" ]


# bubble class
class Bubble:
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

    # get a lifetime tick
    def tick(self):
        self.age = self.age + 1
        if (self.age >= 0 and self.age < self.maxAge) :
            self.x = self.x + self.speed[0]
            self.y = self.y + self.speed[1]

    # draw current state
    def draw(self):
        if (self.age >= 0 and self.age < self.maxAge) :

            with savedState():
                translate(self.offset[0],self.offset[1])

                with savedState():

                    stroke(None);
                    fill(0,0,0);

                    currentFontsize = fSize / self.maxAge * self.age * self.size
                    sinOffsetX = sinOffset(self.age, self.maxAge / self.frequency) * self.speed[0]

                    font(fontName)
                    fontSize(currentFontsize)

                    textBox(self.text, (0 - fSize + sinOffsetX, self.y - fSize / 2, fSize * 2, fSize), align="center")

                    # this would be for a Z-Index to have it blured

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


    # the maximum age a bubble can become
    bubbleMaxAge = animLength / 6

    # the speed the bubbe rices per life unit
    bubbleSpeed = (height * .7 + height * .3 * random() )/ bubbleMaxAge

    # don't generate a bubble too late so it can't disapear before the
    # animation ends
    maxStart = animLength - bubbleMaxAge

    # create bubble and set the current age and maximum age
    b = Bubble();
    b.age =  0 - (maxStart * random());
    b.maxAge = bubbleMaxAge;

    # bigger bubbles have a bigger sidways tension
    frequencyScaler = 0.7 * random() + 0.3
    b.size = 1 - frequencyScaler;
    b.frequency = 7 * frequencyScaler

    # not needed right now see
    b.z = round(random() * s(0.003))

    b.speed = [s(0.01) * frequencyScaler, bubbleSpeed];


    b.offset = [s(1 / (bubbleCount - 1) * i),0];
    b.text = choice(possibleTexts)
    allBubbles.append(b)


# set the state and background
def gState():
    stroke(None)
    fill(1,1,1)
    rect(0,0,widht,height)

# now run the animation
for time in range(animLength):
    print(str(time) + " of " + str(animLength))
    newPage(widht, height)
    gState()
    frameDuration(1/fps)

    for b in allBubbles:
        b.draw();
        b.tick();

# only save if we ar not testing...
if animLength > 20:
    saveImage('./rendering/typo-bubbles' + nowStr() + '.mp4')
