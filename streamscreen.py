import ImageGrab

class StreamScreen:
    def __init__(self, topLeft, bottomRight):
        # Calibrate reference points for stream
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
         
    def getPixel(self, x, y):
        # Get pixel from calibrated x,y point.
        newX = x + self.topLeftX
        newY = y + self.topLeftY

        image = ImageGrab.grab()
        rgb = image.getpixel((newX,newY))
        
        return rgb

    

    

    
