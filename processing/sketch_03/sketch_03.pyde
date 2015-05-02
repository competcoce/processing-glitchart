# colorbend com mais coisas
def setup():
    size(250, 350)
    img = loadImage("magritte.jpg")

    for i in range(len(img.pixels)):
    
        if i > 11345 and i < 29544:
            if(i % 2 == 0):
                vermelho = red(img.pixels[i + 150])
                azul = blue(img.pixels[i + 100])
                verde = green(img.pixels[i + 50])
                img.pixels[i] = color(vermelho, verde, azul)
            else:
                img.pixels[i] = img.pixels[i]
                
        elif ((200*250)+i) > (400*250):
            img.pixels[i] = color(
                                  blue(img.pixels[i]+100),
                                  red(img.pixels[i]),
                                  green(img.pixels[i])
                                  );
        else:
            img.pixels[i] = color(
                                  blue(img.pixels[i]-2),
                                  red(img.pixels[i]),
                                  green(img.pixels[i]+20)
                                  );

    image(img, 0, 0)
    save("saida/sketch-03-magritte.jpg")

