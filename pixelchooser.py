import random
import pointlists
import datetime
import screenconfig

class PixelChooser:
    def __init__(self,width,height):
        currentTime = datetime.datetime.now().time()
        
        self.pixelRatio = self.choosePixel(currentTime.minute % 10)
        
        self.pixel = (int(self.pixelRatio[0] * width),
                      int(self.pixelRatio[1] * height))
        
    def update(self,width,height):
        print width, height, self.pixelRatio, self.pixel
        
        currentTime = datetime.datetime.now().time()
        
        if(currentTime.second == 23):
            self.pixelRatio = self.choosePixel(currentTime.minute % 10)
            
            self.pixel = (int(self.pixelRatio[0] * width + screenconfig.OFFSETX),
                          int(self.pixelRatio[1] * height + screenconfig.OFFSETY))
            
    def choosePixel(self,minute):
        if minute in [0,1]:
            return random.choice(pointlists.list023)
        elif minute in [2]:
            return random.choice(pointlists.list223)
        elif minute in [3]:
            return random.choice(pointlists.list323)
        elif minute in [4,5,6]:
            return random.choice(pointlists.list423)
        elif minute in [7]:
            return random.choice(pointlists.list723)
        elif minute in [8,9]:
            return random.choice(pointlists.list823)
        
    
