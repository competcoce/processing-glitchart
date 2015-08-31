def setup (): 
    size(1000,1000)
    img = loadImage("img glitch jpg.jpg")
  
    for i in range(len(img.pixels)):
        
        vermelho = red (img.pixels[i]);
        verde = green (img.pixels[i]);
        azul = blue (img.pixels[i]);
        
        if (azul > 100):
          azul = 255
          vermelho = 0
          verde = 0
          
        if i-900000 < len(img.pixels):
            azul = blue (img.pixels [i-900000])
        
        if i+20000 < len(img.pixels):
            verde = green (img.pixels [i+20000])
        
        if i+1000 < len(img.pixels):
            vermelho = red (img.pixels [i+1000])
            
        img.pixels[i] = color (azul,verde,vermelho)
   
    image(img, 0,0)
    save("glitch33.jpg")
