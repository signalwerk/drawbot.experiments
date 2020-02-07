### list all installed fonts plus it's variations
for fontName in installedFonts():
    variations = listFontVariations(fontName)
    if variations:
        print(fontName)
        for axis_name, dimensions in variations.items():
            print (axis_name, dimensions)
        print ()
