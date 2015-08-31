def setup (): 
    altura = 1000
    largura = 1000
    
    size(largura,altura)
    img = loadImage("img glitch jpg.jpg")
    
    for a in range(altura):
        for l in range (largura):
            i = (a * largura + l)
            if a < 200 and l < 600 and i%4 == 0:
               img.pixels[i] = color (255,255,255)
            else:
                if (i+100 < len(img.pixels)):
                    img.pixels[i] = img.pixels[i+100]
                    
    for i in range(len(img.pixels)):
     
        if i-900 < len(img.pixels):
            azul = blue (img.pixels [i-900])
        
        if i+200 < len(img.pixels):
            verde = green (img.pixels [i+200])
        
        if i+100 < len(img.pixels):
            vermelho = red (img.pixels [i+100])
            
        img.pixels[i] = color (vermelho,verde,azul)
        
    for i in range(len(img.pixels)):
        
        vermelho = red (img.pixels [i])
        verde = green (img.pixels [i])
        azul = blue (img.pixels [i])  
        
        if verde > 200:
            azul = 255
            verde = 255
            vermelho = 255
            
        if vermelho < 30:
            azul = 0
            verde = 0
            vermelho = 0
            
        img.pixels[i] = color (azul, verde, vermelho)

    image(img, 0,0)
    save("glitch78.jpg")
