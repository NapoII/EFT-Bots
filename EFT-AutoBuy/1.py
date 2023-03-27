#import
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"E:\\Pr0grame\\My_ Pyhton\work_in_progress\\EFT-Bots\Auto_BUY\\Tesseract-OCR\\tesseract.exe"
import cv2
import matplotlib as plt
import numpy as np
from PIL import Image
import time
import pyautogui
import keyboard
import random
import os
import sys, os

def Zeit_pause(seconds):
    start_time = time.time()
    while True:                             # Zeit schelife startet
        current_time = time.time()
        elapsed_time = current_time - start_time        # berechung rest Zeit
        if elapsed_time > seconds:
            break

def If_pic_in_Region(Img_dir, region, Genauigkeit):

    myScreenshot = pyautogui.screenshot(region=(region))   # Screanshot
    open_cv_image = np.array(myScreenshot) 
    # Convert RGB to BGR 
    myScreenshot = open_cv_image[:, :, ::-1].copy()

    button = cv2.imread(Img_dir, cv2.IMREAD_UNCHANGED)

    result = cv2.matchTemplate(myScreenshot, button, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print (str(max_val))
    if max_val > Genauigkeit:     # Genauigkeits abfrage
        return True
    else:
        False

file_path = os.path.dirname(sys.argv[0])
file_path_Bilder = file_path + "/Bilder/"

HauptMenü_dir = file_path_Bilder + "HauptMenu.png"
FlohmarktMenu_dir = file_path_Bilder + "FlohmarktMenu.png"
Handel_pos = (1076,826)
Flohmarkt_pos = (956, 66)
Fenster_MainMenü_pos = (788,778,258,96)
FlohmarktSuchZeile_pos = (397, 157)
Fenster_Flohmarkt_pos =(1179, 87, 212, 51)
Flohmarkt_SuchZeile_First_Item_pos = (505,194)
Flohmarkt_Suche_cheack_dir = file_path_Bilder + "Suche.png"
Fenster_Flohmarkt_Suche_cheack_pos = (439, 180, 173, 33)

def Klick_on(Region):
    Random = random.uniform(0.1, 0.5)
    pyautogui.moveTo(Region[0], Region[1], Random)
    pyautogui.click(button='left')
    Zeit_pause(Random + 0.2)

def Next_Item_from_list(list_dir):
    while True:
        try:
            Item_raw = Rotation_List.pop()
        except:
            with open(list_dir, 'r') as f:
                Rotation_List = f.read().splitlines()
                Rotation_List_Len = len(Rotation_List)
                Item_raw = Rotation_List.pop()

        Item_Split = Item_raw.split(", ")

        Item = Item_Split[0]
        Preis_max = Item_Split[1]
        Seller = Item_Split[2]

        print(Item)
        print(Preis_max)
        print(Seller)


abfrage = pyautogui.confirm(text="Wunsch Item auswählen" , buttons=['Anderes Item', 'Metallschere',"Ultraviolette Lampe","HK G28 B&T QD 7.62x51 sound suppressor","Auto Rotation"])
if abfrage == "Anderes Item":
    Preis_max = pyautogui.prompt(text='Bis zu welchem Preis soll gekauft werden', title="Auto Buy if Preis OK" , default='14000')
if abfrage == "Metallschere":
    Preis_max = 14049
if abfrage == "Ultraviolette Lampe":
    Preis_max = 9799
if abfrage == "HK G28 B&T QD 7.62x51 sound suppressor":
    Preis_max = 33040
if abfrage == "Pestilys Pestmaske":
    Preis_max = 58838
if abfrage == "Auto Rotation":
    pyautogui.alert(text="Geh ins Hauptmenü um mit der Roation zu beginnen! ",title="Achtung !!!",button='OK - EFT ist im Hauptmenü')

    Random = random.uniform(0.1, 0.5)
    Zeit_pause(Random + 0.2)
    pyautogui.moveTo(Handel_pos[0],Handel_pos[1], Random)
    Zeit_pause(Random + 0.2)
    while True:
        if If_pic_in_Region(HauptMenü_dir, Fenster_MainMenü_pos, 0.7) == True:
            Random = random.uniform(0.1, 0.5)
            Klick_on(Handel_pos)
            Zeit_pause(Random + 0.2)
            Klick_on(Flohmarkt_pos)

def Suche_Nach_Item(Item):
    allError()
    Random = random.uniform(0.1, 0.5)
    Zeit_pause(Random + 0.5)
    pyautogui.press('ESC')
    Random = random.uniform(0.1, 0.5)
    Zeit_pause(Random + 0.2)
    pyautogui.moveTo(Handel_pos[0],Handel_pos[1], Random)
    Zeit_pause(Random + 0.2)
    while True:
        if If_pic_in_Region(HauptMenü_dir, Fenster_MainMenü_pos, 0.7) == True:
            break
        Random = random.uniform(0.1, 0.5)
        Klick_on(Handel_pos)
        Zeit_pause(Random + 0.2)
        Klick_on(Flohmarkt_pos)

    while True:
        if If_pic_in_Region(FlohmarktMenu_dir, Fenster_Flohmarkt_pos, 0.7) == True:
            break
        allError()
        Random = random.uniform(0.1, 0.5)
        Klick_on(FlohmarktSuchZeile_pos)
        Zeit_pause(Random + 0.2)
        pyautogui.write(Item, interval=0.05)
        Zeit_pause(Random + 1.5)
        Klick_on(Flohmarkt_SuchZeile_First_Item_pos)
        while True:
            if If_pic_in_Region(Flohmarkt_Suche_cheack_dir, Fenster_Flohmarkt_Suche_cheack_pos, 0.7) == True:
                break
            else:
                pyautogui.alert(text="Es ["+str(Item)+"] nicht gefunden. Starten sie das Programm neu und überprüfen sie das Item.",title="Achtung !!!",button='OK - EFT ist im Hauptmenü')





"""

                        
            time.sleep(0.05)
        time.sleep(0.01)




