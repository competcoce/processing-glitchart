void setup (){
  size(1000,1000);
  PImage img = loadImage ("img glitch png.png");
  for (int i = 0;i <img.pixels.length;i++){
        float vermelho = red (img.pixels[i]);
        float verde = green (img.pixels[i]);
        float azul = blue (img.pixels[i]);
        
        if (azul <100){
          azul = 0;
          vermelho = 255;
          verde = 255;
        }
        
        if (verde > 120){
          verde = 100;
        }
        
   img.pixels [i] = color (verde,vermelho,azul);    
        
   }  
   image (img, 0,0);
   save ("glitch9.png");

}
