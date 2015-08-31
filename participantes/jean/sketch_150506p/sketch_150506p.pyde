def setup (): 
    altura = 667
    largura = 1000
    
    size(largura,altura)
    img = loadImage("DSC_0474 copy.jpg")
    
    for a in range(altura):
        for l in range (largura):
            i = (a * largura + l)
            if a < 1000 and l < 100 and i%1 == 0:
               img.pixels[i] = color (255,255,255)
            if a < 200 and l < 1000 and i%4 == 0:
               img.pixels[i] = color (255,255,255)
               
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

        if azul < 255:
            azul = 0
            
        img.pixels[i] = color (vermelho,azul,verde)

    image(img, 0,0)
    save("glitch96.jpg")
