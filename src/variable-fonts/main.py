def geometricMean(min, max, t):
    range = max - min
    return min + range * t


# canvas setup
scaler = 1920;

widht = scaler;
height = round(scaler / 16 * 9);
fps = 5
duration = 7 * fps


fontName = "RecursiveBeta030-SansLinearA_Sans-Linear-Medium"
variations = listFontVariations(fontName)


# draw my font-test
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
    fontSize(scaler * 0.07)
    text("hello world", (scaler * 0.1, scaler * 0.1))

# saveImage('./rendering/typo-bubbles' + nowStr() + '.mp4')
