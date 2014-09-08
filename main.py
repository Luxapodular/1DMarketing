import time
import screenconfig
import streamscreen

def main():
	#create screen object
        screen = StreamScreen(config.TOP_LEFT, config.BOTTOM_RIGHT)
	while True:
		#read pixel
                rgb = screen.getPixel(50,50)
                print rgb
                
		#send color to led

                #sleep 200ms
		time.sleep(0.2) 
