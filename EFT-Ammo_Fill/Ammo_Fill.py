v = "v0.0.2.AF"
F1 = """
MMMMMMMMMMMM#    #MMMMMMMMMMMM: @MMMMMMMMMMMMMMMMM
MMMMMMMMMMMM#    #MMMMMMMMMMMM: @MMMMMMMMMMMMMMMMM
MM@+++++++++:    #MM%+++++++++, +++++++#MM@+++++++
MM#              #MM:                  +MM%       
MM#              #MM:                  +MM%       
MM#              #MM:                  +MM%       
MMMMMMMMMMMM.    #MM#%%%%%%%%:         +MM%       
MMMMMMMMMMMM.    #MMMMMMMMMMM%         +MM%       
MM@%%%%%%%%%.    #MMM@@@@@@@@%         +MM%      
MM#              #MM:                  +MM%            
MM#              #MM:                  +MM%           
MM#              #MM:                  +MM%       
MMM@@@@@@@@@@,   #MM:                  +MM%       
MMMMMMMMMMMMM,   #MM:                  +MM%       
#############,   +##:                  :##+       
                Ammo Fill
###################################################
        - created by Napo_II
        - """ + v + """
        - python 3.7
        - https://github.com/NapoII/Napos-EFT-BOTS
###################################################\n"""
print(F1)

################################################################################################################################
#import
from tkinter.constants import X

import cv2
import matplotlib as plt
import numpy as np
from PIL import Image
import time
import pyautogui
import os
import sys, os
import keyboard

file_path = os.path.dirname(sys.argv[0])

################################################################################################################################

################################################################################################################################

def Folder_gen(Folder_Name, Folder_dir ):
   print("Ordner Struktur wird überprüft und ggf. angelegt...\n")
   folder = Folder_Name
   dir = "~/"+str(Folder_dir)+"/"+str(folder)           # gibt gewünschten Datei-Pfad an
   full_path = os.path.expanduser(dir)                 # ergänzt datei pfad mit PC User name
   if os.path.exists(full_path):                       # Prüft datei pfad nach exsistänz Ture/False
      print("Ordner Struktur existiert bereits")
      print("  ->   " + str(full_path))
   else:                                               # Erstellt Ordner falls nicht vorhadnen
      os.makedirs(full_path)
      print("Der Ordner ["+folder+"] wurde erstellt im Verzeichnis:" )
      print("  ->   " + str(full_path))
   print("\n")
   return(full_path)

def Datei_name_mit_Zeit(FileName):
    Date = Date_Time=(time.strftime("%d_%m-%Y-%H.%M"))        # Generiert date formater
    FullName = (FileName+"-"+(Date))                           # Generiert Datei name
    return FullName

def Erstelle_TextDatei( Text_File_name, save_path, Inhalt ):
    complete_Path_Text = os.path.join(save_path+"\\"+Text_File_name+".txt")     # Path + text datei name
    if os.path.exists(complete_Path_Text):
        return complete_Path_Text
    else:
        print("\nTextdatei ["+str(Text_File_name)+".txt] wird erstellt...")
        file1 = open(complete_Path_Text, "w")                                         # Datei erstellen
        #toFile = input("Write what you want into the field")                   # Datei input def.
        file1.write(Inhalt)                                                    # Datei wird gefüllt mit input
        file1.close()
        return complete_Path_Text

def Fill_Datei(dir, toFill, Attribut):
    file1 = open(dir, Attribut)                                 # Datei wird geöffnet
    #print("Datei ["+str(dir) + "] wird beschrieben und gespeichtert...\n")
    file1.write(toFill)                                             # Datei wird gefüllt mit input
    file1.close()

def TimeStemp():
    TimeStemp = Date_Time=(time.strftime("%d_%m-%Y_%H:%M:%S"))
    return TimeStemp

def log(Log_input):
    Fill_Datei(Log_File, TimeStemp()+" --> " + Log_input+"\n", "a")
    print (TimeStemp()+" --> " + Log_input+"\n")

def Pos_Matrix(Max_Slots, pos_slot_10X, pos_slot_1Y, pos_slot_1Y2, Slot_Dis):
    
    Pos_matrix1 = []
    Pos_matrix2 = []

    Slot_num = -1
    for i in range(Max_Slots):
        Slot_num = Slot_num +1
        pos = (pos_slot_10X+(Slot_num*Slot_Dis), pos_slot_1Y)
        Pos_matrix1.append(pos)

    Slot_num = -1
    for i in range(Max_Slots):
        Slot_num = Slot_num +1
        pos = (pos_slot_10X+(Slot_num*Slot_Dis), pos_slot_1Y2)
        Pos_matrix2.append(pos)

    return Pos_matrix1, Pos_matrix2

def Zeit_pause(seconds):
    start_time = time.time()
    while True:                             # Zeit schelife startet
        current_time = time.time()
        elapsed_time = current_time - start_time        # berechung rest Zeit
        if elapsed_time > seconds:
            break

def drag_plus_crtl_from(x,y):
    pyautogui.moveTo(x, y)
    Zeit_pause(0.1)
    pyautogui.keyDown('ctrl')  # hold down the shift key
    pyautogui.drag((0-Slot_Dis), 0, 0.2, button='left')   # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button
    pyautogui.keyUp('ctrl')    # release the shift key

def retrun_pos_of_imgFound(Img_dir, region, Genauigkeit):

    myScreenshot = pyautogui.screenshot(region=(region))   # Screanshot
    open_cv_image = np.array(myScreenshot) 
    # Convert RGB to BGR 
    myScreenshot = open_cv_image[:, :, ::-1].copy()

    button = cv2.imread(Img_dir, cv2.IMREAD_UNCHANGED)

    result = cv2.matchTemplate(myScreenshot, button, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    #cv2.imshow('Page', Page)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

    #cv2.imshow('button', button)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    thershold = Genauigkeit
    thershold_x = thershold
    yloc, xloc = np.where(result >= thershold_x)

    if max_val >= thershold_x:
        Found = True
    else:
        Found = False
    x = max_loc[0] + region[0]
    y = max_loc[1] + region[1]
    pos = (x,y)
    #log("Max_val:	" + str(max_val)+ "\n			Max_loc:	" + str(max_loc)+"\n			Found =		"+ str(Found) +"\n")

    #cv2.imshow('result', result)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

    return pos

def if_error(Img_dir, region, Genauigkeit):

    myScreenshot = pyautogui.screenshot(region=(region))   # Screanshot
    open_cv_image = np.array(myScreenshot) 
    # Convert RGB to BGR 
    myScreenshot = open_cv_image[:, :, ::-1].copy()

    button = cv2.imread(Img_dir, cv2.IMREAD_UNCHANGED)

    result = cv2.matchTemplate(myScreenshot, button, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val > Genauigkeit:       # Genauigkeits abfrage
        #log (str(max_val)+" --> "+ str(Img_dir))
        #pyautogui.alert(text="Eine Error Box >> "+str(max_val) +"<< Wurde gefunden. ",title="Achtung !!!" ,button='OK - Weiter, wenn Error behoben! ')
        return True

    else :
        return False

def Split_Bullet(Bullet_Anzahl,xy):
    x = xy[0]
    y = xy[1]
    drag_plus_crtl_from(x,y)

    while True:
        Teilen_pos_result = if_error(Bilder_Folder+"\Ammo_Teilen.png", Teilen_Region, 0.6)
        if Teilen_pos_result == True:
            break
    Zeit_pause(0.1)
    pyautogui.write(str(Bullet_Anzahl))
    #Zeit_pause(0.1)
    pyautogui.press('enter')  # press the Enter key


################################################################################################################################

file_path = os.path.dirname(sys.argv[0])
Bilder_Folder = str(file_path)+"/Bilder"
Doku_Folder = Folder_gen ("EFT - Inventory Helper", "Documents/")
Log_Folder = Folder_gen ("Log", "Documents/EFT - Inventory Helper")
Log_File_name = Datei_name_mit_Zeit ("LogFile-Ammo_Fill")
Log_File = Erstelle_TextDatei (Log_File_name, Log_Folder, F1 + "Log-File\n")

Bot_Path = os.path.dirname(sys.argv[0])

log ( "Bot_Path: ["+str(Bot_Path) + "]\n")

Mags = int(pyautogui.confirm(text="Anzahl an aufzufüllenden Mags" , buttons=[1,2,3,4]))
Mag_size = int(pyautogui.confirm(text="Slot-Breite des Mags" , buttons=[1, 2]))
Mag_größe = int(pyautogui.confirm(text="Größe des Mags" , buttons=[30,60,100,10,20,25,40,41,50]))
Ammo_diffrent = int(pyautogui.confirm(text="Anzahl verschiedener Bullets" , buttons=[2,3]))
Bullet_Rhythmus = int(pyautogui.confirm(text="Bullet-Rhythmus" , buttons=[1,2,3,15]))

log ("Settings: [ Mags=" + str(Mags) + ", Mag_size=" +str(Mag_size) + ", Mag_größe=" + str(Mag_größe) + ", Ammo_diffrent=" + str(Ammo_diffrent) + " ]" )

pos_slot_10X = 1305
pos_slot_10Y = 874
pos_slot_10Y2 = 933
Max_Slots = 10
Slot_Dis = 62

Mag_pos = (1303,866)

Teilen_Region = (1216, 561, 704, 519)

Bullet_pos_1 = (1865, 904)
Bullet_pos_2 = (1862, 841)
Bullet_pos_3 = (1862, 841)

Pos_Matrix = Pos_Matrix(Max_Slots, pos_slot_10X, pos_slot_10Y, pos_slot_10Y2, Slot_Dis)
log("[Max_Slots=" + str(Max_Slots) + " pos_slot_10X=" + str(pos_slot_10X) + " pos_slot_10Y=" + str(pos_slot_10Y) + " pos_slot_10Y2=" + str(pos_slot_10Y2) + " Slot_Dis=" + str(Slot_Dis)+"]\n")

log("Slot Pos Matrix: 1, 2 ")
log(str(Pos_Matrix[0]))
log(str(Pos_Matrix[1])+"\n")

################################################################################################################################

Bullets = ((Mag_größe*Mags)/Ammo_diffrent)/Bullet_Rhythmus
Bullet_ges = Mag_größe * Mags
Bullets_proRound = Bullet_Rhythmus*Ammo_diffrent
Mag_pos_x = Mag_pos[0]
Mag_pos_y = Mag_pos[1]



MagsX = -1
BulletsY = 0

Hotkey_start = pyautogui.prompt(text='HotKey Festlegen Ammo fill zu starten', title="HotKey Festlegen" , default='s')
log("Hotkey_start: "+str(Hotkey_start)+"\n")

while True:
    if keyboard.is_pressed(Hotkey_start):

        while True:
            Mag_pos_x = Mag_pos[0]
            MagsX = MagsX + 1

            if MagsX == Mags:
                break
            if Mag_size == 2:
                Slot_DisX = Slot_Dis * 2
                Mag_pos_x = Mag_pos_x + (MagsX*Slot_DisX)
            else:
                Mag_pos_x = Mag_pos_x + (MagsX*Slot_Dis)

            log("Mag Nr: "+str(MagsX+1)+"\n")
            BulletsX = 0
            while True:
                if BulletsX >= Mag_größe:
                    break
                BulletsX = BulletsX + Bullets_proRound
                BulletsY = BulletsY + Bullets_proRound
                prozent = round((100/Bullet_ges)*BulletsY,2)
                log (str(prozent)+ "% Bullets: "+str(BulletsY)+"/"+str(Bullet_ges))




                if_error(Bilder_Folder+"\Hauptmenue.png", (320, 514, 376, 134), 0.7)
                Split_Bullet(Bullet_Rhythmus ,Bullet_pos_1)
                Split_Bullet(Bullet_Rhythmus ,Bullet_pos_2)
                if Ammo_diffrent == 3:
                    Split_Bullet(Bullet_Rhythmus ,Bullet_pos_3)

                if_error(Bilder_Folder+"\Hauptmenue.png", (320, 514, 376, 134), 0.7)
                pyautogui.moveTo(Bullet_pos_1[0]-Slot_Dis, Bullet_pos_1[1], duration=0.2)  # move mouse to XY coordinates over num_second seconds
                pyautogui.mouseDown(button='left')
                pyautogui.moveTo(Mag_pos_x,Mag_pos_y, duration=0.3)  # move mouse to XY coordinates over num_second seconds
                pyautogui.mouseUp(button='left')
            
                if_error(Bilder_Folder+"\Hauptmenue.png", (320, 514, 376, 134), 0.7)
                pyautogui.moveTo(Bullet_pos_2[0]-Slot_Dis, Bullet_pos_2[1], duration=0.2)  # move mouse to XY coordinates over num_second seconds
                pyautogui.mouseDown(button='left')
                pyautogui.moveTo(Mag_pos_x,Mag_pos_y, duration=0.3)
                pyautogui.mouseUp(button='left')

                if Ammo_diffrent == 3:
                    if_error(Bilder_Folder+"\Hauptmenue.png", (320, 514, 376, 134), 0.7)
                    pyautogui.moveTo(Bullet_pos_3[0]-Slot_Dis, Bullet_pos_3[1], duration=0.2)  # move mouse to XY coordinates over num_second seconds
                    pyautogui.mouseDown(button='left')
                    pyautogui.moveTo(Mag_pos_x,Mag_pos_y, duration=0.3)
                    pyautogui.mouseUp(button='left')

        time.sleep(0.01)
