#colorbend
def setup():
    size(250,350)
    img = loadImage("magritte.jpg")
    
    for i in range(len(img.pixels)):
        vermelho = red(img.pixels[i])
        verde = green(img.pixels[i])
        azul = blue(img.pixels[i])
        
        if i == 2:
            println(img.pixels[i])
    
        if( azul > 100):
            azul = 255
        
        if(azul > 200 and vermelho > 200 and verde > 200):
            azul = 0
            verde = 255
            vermelho = 255
            
        if(azul < 50 and vermelho < 50 and verde < 50):
            azul = 255
            verde = 0
            vermelho = 0
            
        img.pixels[i] = color(verde,azul,vermelho)
    
    image(img, 0,0)
    save("saida/magritte-01.jpg");
