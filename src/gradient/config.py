from random import choice

debug = False


# basic setup
scaler = 1920;
fps = 24
seconds = 7

# some magic numbers to config the style
speedFactor = 10
elementFactor = 20



widht = scaler;
heightFactor = 1 / 16 * 9
height = round(scaler * heightFactor);
elementMaxAge = (1 / speedFactor) * 15 / seconds


# overwrite for debug
if (debug):
    fps = 1


# element setup
animLength = seconds * fps
elementCount = round(elementFactor * seconds)
