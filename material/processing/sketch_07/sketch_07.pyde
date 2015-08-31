def setup():
    largura = 250
    altura = 350

    size(largura, altura)
    img = loadImage("magritte.jpg")
            
    image(img, 0, 0)
    
    for i in range(altura):
        largura_diff = -largura/2+random(largura)
        altura_diff = -altura/2+random(altura)
        
        r = floor(random(100))
        if(r> 25):
            image(img, largura_diff, i, largura, 1)
    
    save("saida/sketch-07-magritte.jpg")

