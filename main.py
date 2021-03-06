import time
import screenconfig
import blinkcontrol
from pixelchooser import PixelChooser
from streamscreen import StreamScreen

def main():
  #create screen object
  screen = StreamScreen(screenconfig.TOP_LEFT, screenconfig.BOTTOM_RIGHT)

  #create pixel chooser object
  pixelChooser = PixelChooser(screen.width,screen.height)

  while True:
    #update pixel chooser
    pixelChooser.update(screen.width,screen.height)
      
    #read pixel from screen
    rgb = screen.getPixel(pixelChooser.pixel[0], pixelChooser.pixel[1])
    print pixelChooser.pixel[0], pixelChooser.pixel[1]

    #send color to led
    blinkcontrol.setColor(rgb);

    #wait a little bit
    time.sleep(0.01)

main()
