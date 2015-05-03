# colorbend com mais coisas
def setup():
    largura = 250
    altura = 350

    size(largura, altura)
    img = loadImage("magritte.jpg")

    for i in range(largura):
        for j in range(altura):
            indice = (j * largura) + i

            if(i < largura / 2):
                vermelho = red(img.pixels[indice])
                azul = blue(img.pixels[indice])
                verde = green(img.pixels[indice])
                img.pixels[indice] = color(verde, vermelho, azul)
                
            if(i > largura / 2):
                vermelho = red(img.pixels[indice])
                azul = blue(img.pixels[indice])
                verde = green(img.pixels[indice])
                img.pixels[indice] = color(verde+200, vermelho, azul)

            if(j < 400 and j > 100 and i > 100 and indice % 2 == 0):
                img.pixels[indice] = img.pixels[(i * altura) + j]

            if(j > 200 and i > 28 and j%10 == 0):
                img.pixels[indice] = img.pixels[indice - 100]
            
            if(j > 230 and j%2 == 0):
                img.pixels[indice] = img.pixels[indice - 100]

    image(img, 0, 0)
    save("saida/sketch-04-magritte.jpg")

