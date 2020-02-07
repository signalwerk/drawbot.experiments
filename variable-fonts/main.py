
def s(x):
  return x * scaler

def geometricMean(min, max, t):
    range = max - min
    return min + range * t


# canvas setup
scaler = 1000;

widht = s(1);
height = round(s(1 / 16 * 9));
fps = 1
duration = 7 * fps


fontName = "RecursiveBeta030-SansLinearA_Sans-Linear-Medium"
variations = listFontVariations(fontName)




for time in range(duration):
    newPage(widht, height)
    frameDuration(1/fps)
    t = 1 / duration * time

    font(fontName);
    fontVariations(
        wght = geometricMean(variations["wght"]["maxValue"], variations["wght"]["minValue"], t),
        slnt = geometricMean(variations["slnt"]["minValue"], variations["slnt"]["maxValue"], t),
        CASL = variations["CASL"]["maxValue"]
    )
    fontSize(s(0.07))
    text("hello world", (s(0.1), s(0.1)))
    # saveImage('./rendering/typo-bubbles' + nowStr() + '.mp4')








# RecursiveBeta030-SansLinearA_Sans-Linear-Medium
# MONO {'name': 'Monospace', 'minValue': 0.0, 'maxValue': 1.0, 'defaultValue': 0.0}
# CASL {'name': 'Casual', 'minValue': 0.0, 'maxValue': 1.0, 'defaultValue': 0.0}
# wght {'name': 'Weight', 'minValue': 300.0, 'maxValue': 1000.0, 'defaultValue': 300.0}
# slnt {'name': 'Slant', 'minValue': -15.0, 'maxValue': 0.0, 'defaultValue': 0.0}
# ital {'name': 'Italic', 'minValue': 0.0, 'maxValue': 1.0, 'defaultValue': 0.5}
