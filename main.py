import time
import screenconfig
import blinkcontrol
from streamscreen import StreamScreen

def main():
  #create screen object
  screen = StreamScreen(screenconfig.TOP_LEFT, screenconfig.BOTTOM_RIGHT)
  while True:
    #read pixel
    rgb = screen.getPixel(1700,300)

    #send color to led
    blinkcontrol.setColor(rgb);

    #sleep 200ms
    time.sleep(0.01)

main()
