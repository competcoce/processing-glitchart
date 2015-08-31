def setup (): 
    size(1000,1000)
    img = loadImage("img glitch jpg.jpg")
  
    for i in range(0,len(img.pixels)):
     
        vermelho = red (img.pixels [i])
        verde = green (img.pixels [i])
        azul = blue (img.pixels [i])
                        
        if i+200 < len(img.pixels):
            if i%50:
                azul = blue (img.pixels [i+200])
                verde = green (img.pixels [i+200])
                vermelho = red (img.pixels [i+200])
    
        img.pixels[i] = color (azul,verde,vermelho)
   
    image(img, 0,0)
    save("glitch40.jpg")
