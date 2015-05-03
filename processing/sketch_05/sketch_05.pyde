def setup():
    largura = 250
    altura = 350

    size(largura, altura)
    img = loadImage("magritte.jpg")

    for i in range(largura):
        for j in range(altura):
            indice = (j * largura) + i
            diff = -25 + floor(random(50))

            if (indice + diff < largura * altura):
                img.pixels[indice] = img.pixels[indice + diff]

    image(img, 0, 0)

    save("saida/sketch-05-magritte.jpg")

