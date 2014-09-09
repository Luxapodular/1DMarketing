import time
import screenconfig
import blinkcontrol
import datetime
import pixelchooser
from streamscreen import StreamScreen

def main():
  #create screen object
  screen = StreamScreen(screenconfig.TOP_LEFT, screenconfig.BOTTOM_RIGHT)

  #choose first pixel
  currentTime = datetime.datetime.now().time()
  pixel = pixelchooser.choosePixel((currentTime.minute % 10))
  while True:
    currentTime = datetime.datetime.now().time()
    if (currentTime.second == 23):
      pixel = pixelchooser.choosePixel(currentTime.minute)

    print currentTime
    print pixel
      
    #read pixel
    rgb = screen.getPixel(pixel[0],pixel[1])

    #send color to led
    blinkcontrol.setColor(rgb);

    #sleep 200ms
    time.sleep(0.01)

main()
