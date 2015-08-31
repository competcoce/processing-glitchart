def setup (): 
    size(1000,1000)
    img = loadImage("img glitch jpg.jpg")
  
    for i in range (626011, len(img.pixels)):
     
        if i-900000 < len(img.pixels):
            azul = blue (img.pixels [i-900000])
        
        if i+20000 < len(img.pixels):
            verde = green (img.pixels [i+20000])
        
        if i+1000 < len(img.pixels):
            vermelho = red (img.pixels [i+1000])
            
    for i in range (2000, len(img.pixels)):
     
        if i+10000 < len(img.pixels):
            azul = blue (img.pixels [i+10000])
            
        verde = green (img.pixels [i])
        vermelho = red(img.pixels [i])
            
        img.pixels[i] = color (azul,verde,vermelho)
   
    image(img, 0,0)
    save("glitch31.jpg")
