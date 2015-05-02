# colorbend com mais coisas
def setup():
    size(250, 350)
    img = loadImage("magritte.jpg")

    for i in range(len(img.pixels)):
        if i> 10345 and i<26560:
            if (i % 249) % 2 == 0:
                img.pixels[i] = img.pixels[i-150]
        else:
            img.pixels[i] = color(
                                  blue(img.pixels[i]),
                                  red(img.pixels[i]),
                                  green(img.pixels[i])
                                  );

    image(img, 0, 0)

