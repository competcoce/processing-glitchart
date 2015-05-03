# colorbend com mais coisas
def setup():
    size(250, 350)
    img = loadImage("magritte.jpg")

    for i in range(len(img.pixels)):

        if(i + 150 < len(img.pixels) and i > 13921 and i < 60921):
            diff_vermelho = -100 + floor(random(200))
            diff_verde = -100 + floor(random(200))
            diff_azul = -100 + floor(random(200))

            vermelho = red(img.pixels[i+50])
            verde = red(img.pixels[i+200])
            azul = red(img.pixels[i])

            img.pixels[i] = color(vermelho, verde, azul)
        
        if(i + 150 < len(img.pixels) and i > 10200 and i < 30921):
            if(i % 2 == 0):

                img.pixels[i] = img.pixels[i + 150]

                diff_vermelho = -100 + floor(random(200))
                diff_verde = -100 + floor(random(200))
                diff_azul = -100 + floor(random(200))

                vermelho = red(img.pixels[i]) + diff_vermelho
                verde = red(img.pixels[i]) + diff_verde
                azul = red(img.pixels[i]) + diff_azul

                img.pixels[i] = color(vermelho, verde, azul)


    image(img, 0, 0)
    save("sketch-06-magritte.jpg")

