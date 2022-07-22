from cv2 import *
import pyfiglet
import os

appname = 'who am i'

def capture():
    cam_port = 0
    cam = VideoCapture(cam_port)
    
    result, image = cam.read()
    imshow(appname, image)
    while True:

        key = waitKey(20)
        if key == 27: # exit on ESC
            break
    destroyWindow(appname)
  
def clear_screen():
    name = os.name;
    if name == 'nt':
        _ = os.system('cls')
  
    else:
        _ = os.system('clear')
def look_at_me():
    clear_screen()

    result = pyfiglet.figlet_format("Look at me !!")
    print(result)

look_at_me()
capture()
