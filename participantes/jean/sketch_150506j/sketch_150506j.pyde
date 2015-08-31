def setup (): 
    size(1000,1000)
    img = loadImage("img glitch jpg.jpg")
    
    for i in range(len(img.pixels)):
     
        if i-900000 < len(img.pixels):
            azul = blue (img.pixels [i-900000])
        
        if i+20000 < len(img.pixels):
            verde = green (img.pixels [i+20000])
        
        if i+1000 < len(img.pixels):
            vermelho = red (img.pixels [i+1000])
            
        img.pixels[i] = color (azul,verde,vermelho)
      
    for i in range(len(img.pixels)/2):
        
        vermelho = red (img.pixels [i])
        verde = green (img.pixels [i])
        azul = blue (img.pixels [i]) 
                           
        if i%15 != 0:
            img.pixels[i] = color(vermelho, verde, azul)
        else:
            img.pixels[i] = color (255, 255, 255)
   
    image(img, 0,0)
    save("glitch51.jpg")
