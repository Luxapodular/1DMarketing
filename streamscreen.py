import ImageGrab

#calibrate reference points for stream
class StreamScreen:
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.topLeftX = topLeft[0]
        self.topLeftY = topLeft[1]

        self.bottomRight = bottomRight
        self.bottomRightX = bottomRight[0]
        self.bottomRightY = bottomRight[1]

        self.width = self.bottomRightX - self.topLeftX
        self.height = self.bottomRightY - self.topLeftY

        self.topRightX = self.bottomRightX
        self.topRightY = self.topLeftY
        self.topRight = (self.topRightX, self.topRightY)

        self.bottomLeftX = self.topLeftX
        self.bottomLeftY = self.bottomRightY
        self.bottomLeft = (self.bottomLeftX, self.bottomLeftY)

#Get pixel from calibrated x,y point.         
    def getPixel(self,x = self.width/2,y = self.height/2):
        image = ImageGrab.grab()
        newX = x + self.topLeftX
        newY = y + self.topLeftY
        rgb = image.getpixel((newX,newY))
        return rgb

    

    

    
