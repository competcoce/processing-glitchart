def setup (): 
    altura = 1000
    largura = 1000
    
    size(largura,altura)
    img = loadImage("img glitch jpg.jpg")
    
    for a in range(altura):
        for l in range (largura):        
            i = (a * largura) + l
            if i+100 < altura*largura:
                ver_random = red(img.pixels[i+100])+floor(random(255))
                                 
            verde = green (img.pixels[i])
            azul = blue (img.pixels[i])
            vermelho = ver_random
            
            img.pixels[i] = color(verde,azul,vermelho)

    image(img, 0,0)
    save("glitch94.jpg")
