#colorbend com mais coisas
def setup():
    size(250,350)
    img = loadImage("magritte.jpg")
    
    for i in range(len(img.pixels)):
        if(i+100<len(img.pixels)):
            if(i%2 == 0):
                img.pixels[i] = img.pixels[i+100]
    
    image(img, 0,0)
