import pyautogui

# Python program to explain cv2.rectangle() method 
   
# importing cv2 
import cv2 
   
# path 
path = r'E:\\Pr0grame\\My_ Pyhton\\work_in_progress\\EFT-Bots\\EFT-Item-List\\Bilder\\Page.png'
   
# Reading an image in default mode
image = cv2.imread(path)
   
# Window name in which image is displayed
window_name = 'Image'

while True:
    x = int(pyautogui.prompt(text='X?', title='Neuen Raid Erstellen' , default='940'))
    y = int(pyautogui.prompt(text='Y?', title='Neuen Raid Erstellen' , default='159'))


    # Start coordinate, here (5, 5)
    # represents the top left corner of rectangle
    start_point = (int(x)-10, y-10)
    
    # Ending coordinate, here (220, 220)
    # represents the bottom right corner of rectangle
    end_point = (x+10, y+10)
    
    # Blue color in BGR
    color = (255, 0, 0)
    
    # Line thickness of 2 px
    thickness = 2
    
    # Using cv2.rectangle() method
    # Draw a rectangle with blue line borders of thickness of 2 px
    image = cv2.rectangle(image, start_point, end_point, color, thickness)



    # Displaying the image 
    cv2.imshow('image', image)
    cv2.waitKey()
    cv2.destroyAllWindows()