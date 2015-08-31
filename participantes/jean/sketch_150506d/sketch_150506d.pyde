def setup (): 
    size(1000,1000)
    img = loadImage("img glitch jpg.jpg")
  
    for i in range(817232, len(img.pixels)):
     
        if i-10000 < len(img.pixels):
            azul = blue (img.pixels [i-10000])
        
        if i+200 < len(img.pixels):
            verde = green (img.pixels [i+200])
        
        if i+100 < len(img.pixels):
            vermelho = red (img.pixels [i+100])
   
    for i in range(len(img.pixels)/2):
     
        if i-9000 < len(img.pixels):
            azul = blue (img.pixels [i-9000])
        
        verde = green (img.pixels [i])
        vermelho = red (img.pixels [i])
        
        img.pixels[i] = color (azul,verde,vermelho)
   
    image(img, 0,0)
    save("glitch20.jpg")
