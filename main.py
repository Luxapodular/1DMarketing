import time
import screenconfig
from streamscreen import StreamScreen

def main():
  #create screen object
  screen = StreamScreen(screenconfig.TOP_LEFT, screenconfig.BOTTOM_RIGHT)
  while True:
    #read pixel
    rgb = screen.getPixel(50,50)
    print rgb

    #send color to led

    #sleep 200ms
    time.sleep(0.2)

main()
