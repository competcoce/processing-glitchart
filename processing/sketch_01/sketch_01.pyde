#colorbend
def setup():
    size(250,350)
    img = loadImage("magritte.jpg")
    
    for i in range(len(img.pixels)):
        vermelho = red(img.pixels[i])
        verde = green(img.pixels[i])
        azul = blue(img.pixels[i])
    
        if( azul > 100):
            azul = 255

        img.pixels[i] = color(vermelho,azul,green)
    
    image(img, 0,0)
    save("saida/magritte-01.jpg");
