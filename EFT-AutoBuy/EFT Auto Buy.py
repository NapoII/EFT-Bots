v = "v0.1.1.AB"
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
                Auto Buy if Preis OK
###################################################
        - created by Napo_II
        - """ + v + """
        - python 3.7
        - https://github.com/NapoII/Napos-EFT-BOTS
###################################################\n"""
print(F1)

################################################################################################################################
#import
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
#pytesseract.pytesseract.tesseract_cmd = r"E:\\Pr0grame\\My_ Pyhton\work_in_progress\\EFT-Bots\Auto_BUY\\Tesseract-OCR\\tesseract.exe"

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
import win32gui
import pyperclip
import platform

file_path = os.path.dirname(sys.argv[0])
#pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = file_path +"\\Tesseract-OCR\\tesseract.exe"


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

def Aktiv_if_window_name(Window_Name):
    while True:
        w=win32gui
        Window = w.GetWindowText (w.GetForegroundWindow())
        if Window_Name in Window:
            return True
        else:
            print(str(Window_Name)+ "Nicht aktives Fenster --> " +str(Window))

def Numbers_from_region(pos):
    log("Numbers_from_region -->" + str(pos))
    img = pyautogui.screenshot(region= pos)
    String = pytesseract.image_to_string(img, config="-c tessedit_char_whitelist=0123456789 -c preserve_interword_spaces=7") # Nur 1-9 keine Buchstaben
    #String = pytesseract.image_to_string(Bild)     # alles
    String = String.replace(" ", "")
    if len(String) == 0:
        String = 1.0
    try:
        print(String)
        String = int(float(String))
        print(String)
        log("["+str(String)+" # erkannt")
        return String
        
    except:
        log("["+str(String)+" # erkannt darum output = 1.0")
        String = 1.0
        return String

def Zeit_pause(seconds):
    start_time = time.time()
    while True:                             # Zeit schelife startet
        current_time = time.time()
        elapsed_time = current_time - start_time        # berechung rest Zeit
        if elapsed_time > seconds:
            break

def if_Error_1503(Img_dir, region, Genauigkeit):

    myScreenshot = pyautogui.screenshot(region=(region))   # Screanshot
    open_cv_image = np.array(myScreenshot) 
    # Convert RGB to BGR 
    myScreenshot = open_cv_image[:, :, ::-1].copy()

    button = cv2.imread(Img_dir, cv2.IMREAD_UNCHANGED)

    result = cv2.matchTemplate(myScreenshot, button, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > Genauigkeit:       # Genauigkeits abfrage
        log (str(max_val)+" --> "+ str(Img_dir))
        Timerandom = random.uniform(0, 0.5)
        pyautogui.moveTo(pos_Error_1503_enter[0], pos_Error_1503_enter[1], Timerandom)
        
        Zeit_pause(Timerandom + 0.3)
        pyautogui.click()
        return True

    else :
        log (str(max_val)+" --> "+ str(Img_dir))
        return False

def if_error(Img_dir, region, Genauigkeit):

    myScreenshot = pyautogui.screenshot(region=(region))   # Screanshot
    open_cv_image = np.array(myScreenshot) 
    # Convert RGB to BGR 
    myScreenshot = open_cv_image[:, :, ::-1].copy()

    button = cv2.imread(Img_dir, cv2.IMREAD_UNCHANGED)

    result = cv2.matchTemplate(myScreenshot, button, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > Genauigkeit:       # Genauigkeits abfrage
        log (str(max_val)+" --> "+ str(Img_dir))
        pyautogui.alert(text="Eine Error Box >> "+str(max_val) +"<< Wurde gefunden. ",title="Achtung !!!" ,button='OK - Weiter, wenn Error behoben! ')
        Zeit_pause(1)
        return True

    else :
        return False

def if_ESC(Img_dir, region, Genauigkeit):

    myScreenshot = pyautogui.screenshot(region=(region))   # Screanshot
    open_cv_image = np.array(myScreenshot) 
    # Convert RGB to BGR 
    myScreenshot = open_cv_image[:, :, ::-1].copy()

    button = cv2.imread(Img_dir, cv2.IMREAD_UNCHANGED)

    result = cv2.matchTemplate(myScreenshot, button, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > Genauigkeit:       # Genauigkeits abfrage
        log (str(max_val)+" --> "+ str(Img_dir))
        pyautogui.alert(text="Auto BuyBot wurde pausiert >> "+str(max_val) +"<< Wurde gefunden. ",title="Achtung !!!",button='OK - Wenn weiter!')
        Zeit_pause(1)
        return True

    else :
        return False

def buy():
    Aktiv_if_window_name("EscapeFromTarkov")
    if_Error_1503(Error_img_dir, Fenster_pos_Error_1503, 0.8)
    pyautogui.moveTo(pos_Item_Buy_Top[0], pos_Item_Buy_Top[1], random.uniform(0, 0.5))
    pyautogui.click(button='left')
    Zeit_pause(random.uniform(0, 0.2))
    pyautogui.press('y')
    Zeit_pause(1)
    if_Error_1503(Error_img_dir, Fenster_pos_Error_1503, 0.8)
    Zeit_pause(0.5)

def allError():
    Aktiv_if_window_name("EscapeFromTarkov")
    if_Error_1503(Error_img_dir, Fenster_pos_Error_1503, 0.8)
    if_error(Anti_Bot_img_dir, Fesnter_pos_Anti_Bot_error, 0.8)
    if_error(Error_NichtGenugGeld_dir, Fenster_Error_NichtGenugGeld, 0.8)
    if_error(Error_NichtPlatz_dir, Fenster_Error_NichtPlatz, 0.8)
    if_error(Error_ItemNotMove_dir , Fesnter_pos_Error_ItemNotMove, 0.8)
    if_Error_1503(Error_img_dir, Fenster_pos_Error_1503, 0.8)
    if_ESC(Buy_menue_dir, Fesnter_pos_Buy_menue, 0.8)

def Len_Line_in_Text(list_dir):
    with open(list_dir, 'r') as f:
        List = f.read().splitlines()
        List_Len = len(List)
        return List_Len

def Next_Item_from_list(list_dir, x):

    with open(list_dir, 'r') as f:
        Rotation_List = f.read().splitlines()
        Rotation_List_Len = len(Rotation_List)
        Item_raw = Rotation_List[x]

        Item_Split = Item_raw.split(", ")
        return Item_Split

def If_pic_in_Region(Img_dir, region, Genauigkeit):

    myScreenshot = pyautogui.screenshot(region=(region))   # Screanshot
    open_cv_image = np.array(myScreenshot) 
    # Convert RGB to BGR 
    myScreenshot = open_cv_image[:, :, ::-1].copy()

    button = cv2.imread(Img_dir, cv2.IMREAD_UNCHANGED)

    result = cv2.matchTemplate(myScreenshot, button, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    print (str(max_val)+" --> "+ str(Img_dir))
    if max_val > Genauigkeit:     # Genauigkeits abfrage
        log("Img in Region --> "+ str(HauptMenü_dir)+ "Pos: "+ str(Fenster_MainMenü_pos)+"\n")
        return True
    else:
        False


def Klick_on(Region):
    Random = random.uniform(0.1, 0.5)
    pyautogui.moveTo(Region[0], Region[1], Random)
    pyautogui.click(button='left')
    log("Klick on --> " + str(Region)+"\n")
    Zeit_pause(Random + 0.2)

def type(text: str):    
    pyperclip.copy(text)
    if platform.system() == "Darwin":
        pyautogui.hotkey("command", "v")
    else:
        pyautogui.hotkey("ctrl", "v")

def Suche_Nach_Item(Item):
    allError()
    Random = random.uniform(0.1, 0.5)
    Zeit_pause(Random + 0.5)
    pyautogui.press('ESC')
    log("Pressing --> ESC")
    Random = random.uniform(0.1, 0.5)
    Zeit_pause(Random + 0.2)
    while True:
        if If_pic_in_Region(Buy_menue_dir, Fesnter_pos_Buy_menue, 0.7) == True:
            break
    Klick_on(Flohmarkt_pos)
    log("Klick on --> "+ "Flohmarkt_pos: " +str(Flohmarkt_pos)+"\n")
    Random = random.uniform(0.1, 0.5)

    while True:
        if If_pic_in_Region(FlohmarktMenu_dir, Fenster_Flohmarkt_pos, 0.7) == True:
            break
    allError()
    Zeit_pause(Random + 0.2)
    Random = random.uniform(0.1, 0.5)
    Klick_on(FlohmarktSuchZeile_pos)
    log("Klick on --> "+ "FlohmarktSuchZeile_pos: " +str(FlohmarktSuchZeile_pos))
    Zeit_pause(Random + 0.2)
    type(Item)
    Zeit_pause(Random + 1.5)
    Klick_on(Flohmarkt_SuchZeile_First_Item_pos)
    log("Klick on --> "+ "Flohmarkt_SuchZeile_First_Item_pos: " +str(Flohmarkt_SuchZeile_First_Item_pos))
    while True:
        if If_pic_in_Region(Flohmarkt_Suche_cheack_dir, Fenster_Flohmarkt_Suche_cheack_pos, 0.7) == True:
            break
        else:
            log("Es ["+str(Item)+"] nicht gefunden. Starten sie das Programm neu und überprüfen sie das Item."+"\n")
            pyautogui.alert(text="Es ["+str(Item)+"] nicht gefunden. Starten sie das Programm neu und überprüfen sie das Item.",title="Achtung !!!",button='OK - EFT ist im Hauptmenü')
                


def Len_Line_in_Text(list_dir):
    with open(list_dir, 'r') as f:
        List = f.read().splitlines()
        List_Len = len(List)
        return List_Len

def Next_Item_from_list(list_dir, x):

    with open(list_dir, 'r') as f:

        Rotation_List = f.read().splitlines()
        Rotation_List_Len = len(Rotation_List)
        log("Open File --> " +str(list_dir))
        log("Open File Len --> " +str(Rotation_List_Len))
        Item_raw = Rotation_List[x]

        Item_Split = Item_raw.split(", ")
        log("Next Item --> "+ str(Item_Split)+"\n")
        return Item_Split



################################################################################################################################

################################################################################################################################
#PreSet Programm

file_path = os.path.dirname(sys.argv[0])
file_path_Bilder = file_path + "/Bilder/"

Doku_Folder = Folder_gen ("EFT - Inventory Helper", "Documents/")
Log_Folder = Folder_gen ("Log", "Documents/EFT - Inventory Helper")
Log_File_name = Datei_name_mit_Zeit ("LogFile-AutoBuy")
Log_File = Erstelle_TextDatei (Log_File_name, Log_Folder, F1 + "Log-File\n")

Bot_Path = os.path.dirname(sys.argv[0])

log ( "Bot_Path: ["+str(Bot_Path) + "]\n")

Hotkey_start = pyautogui.prompt(text='HotKey Festlegen um Autobuy zu starten', title="Auto Buy if Preis OK" , default='p')
log("Hotkey_start: "+str(Hotkey_start)+"\n")

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

Fesnter_pos_Preis = (1306, 175, 213, 71,) #x ,y ,w ,h
#Fesnter_pos_Preis = (1342, 175, 171,71) #x ,y ,w ,h # Normal im ferntsrmodus

pos_Item_Top = (923, 212)
pos_Item_Buy_Top = (1773, 212)

Fenster_pos_Error_1503 = (739, 511, 458, 120)
pos_Error_1503_enter = (967, 598)

Fesnter_pos_Anti_Bot_error = (559, 152  , 865, 837)
Error_img_dir = file_path_Bilder + "Error_1503.png"
Anti_Bot_img_dir = file_path_Bilder + "Error_Bot.png"
Error_NichtGenugGeld_dir = file_path_Bilder + "Error_NichtGenugGeld.png"

Fenster_Error_NichtGenugGeld = (767, 504, 402, 134)
Fenster_Error_NichtPlatz = (739, 510, 459, 212) #####

Error_NichtPlatz_dir = file_path_Bilder + "Error_NichtPlatz.png"
Buy_menue_dir = file_path_Bilder + "Buy_menue.png"
Fesnter_pos_Buy_menue = (648, 376, 640, 345) 

Error_ItemNotMove_dir = file_path_Bilder + "Error_ItemNotMove.png"
Fesnter_pos_Error_ItemNotMove = (739, 501, 458, 140) 

list_dir = file_path +"\\ListeAutoRotation.txt"

HauptMenü_dir = file_path_Bilder + "HauptMenu.png"
FlohmarktMenu_dir = file_path_Bilder + "FlohmarktMenu.png"
Handel_pos = (1076,826)
Flohmarkt_pos = (963, 64)
Fenster_MainMenü_pos = (788,778,258,96)
FlohmarktSuchZeile_pos = (397, 157)
Fenster_Flohmarkt_pos =(1179, 87, 212, 51)
Flohmarkt_Suche_cheack_dir = file_path_Bilder + "Suche.png"
Fenster_Flohmarkt_Suche_cheack_pos = (44, 173, 580, 55)
Flohmarkt_SuchZeile_First_Item_pos = (505,194)

pyautogui.alert(text="Stelle EFT mit [ALT + Enter] in den Fenster Modus!",title="Achtung !!!",button='OK')

log("Fesnter_pos_Preis: "+str(Fesnter_pos_Preis))
log("pos_Item_Top: "+str(pos_Item_Top))
log("pos_Item_Buy_Top: "+ str(pos_Item_Buy_Top))
log("Fenster_pos_Error_1503: " +str(Fenster_pos_Error_1503))
log("pos_Error_1503_enter: "+str(pos_Error_1503_enter))
log("Fesnter_pos_Anti_Bot_error: "+str(Fesnter_pos_Anti_Bot_error))######
log("Error_img_dir: "+ str(Error_img_dir)+"\n")
log("Anti_Bot_img_dir: "+str(Anti_Bot_img_dir))
log("Error_NichtGenugGeld_dir: "+str(Error_NichtGenugGeld_dir))
log("Fenster_Error_NichtGenugGeld: "+str(Fenster_Error_NichtGenugGeld))
log("Fenster_Error_NichtPlatz: "+str(Fenster_Error_NichtPlatz))
log("Error_NichtPlatz_dir: "+str(Error_NichtPlatz_dir))
log("Buy_menue_dir: "+str(Buy_menue_dir))
log("Fesnter_pos_Buy_menue: "+str(Fesnter_pos_Buy_menue))
log("Error_ItemNotMove_dir: "+str(Error_ItemNotMove_dir))
log("Fesnter_pos_Buy_menue: "+str(Fesnter_pos_Error_ItemNotMove)+"\n")




################################################################################################################################

if abfrage == "Auto Rotation":
    allError()
    while True:
        
        if keyboard.is_pressed(Hotkey_start):
            log("Auto Rotation BUY gestartet Start!"+"\n")

            Random = random.uniform(0.1, 0.5)
            Zeit_pause(Random + 0.2)
            pyautogui.moveTo(Handel_pos[0],Handel_pos[1], Random)
            log("Move to Handel --> " + str(Handel_pos[0])+", "+str(Handel_pos[1]))
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

            while True:


                Zeit_pause(1)
                Len_Line = Len_Line_in_Text(list_dir)+1
                x2 = -1
                while True:
                    Len_Line = Len_Line -1
                    x2 = x2 + 1
                    log("Noch "+str(Len_Line)+ "on list für volle Roation.")
                    if Len_Line == 0:
                        break

                    Raw_Item = Next_Item_from_list(list_dir, x2)

                    Item = Raw_Item[0]
                    Preis_max = Raw_Item[1]
                    Seller = Raw_Item[2]
                    log("Preis_max: "+str(Preis_max))
                    Preis_max = int(Preis_max)
                    Preis_Max_Len = len(str(Preis_max ))
                    #pyautogui.alert(text="Max Preis bestätigen ["+str(Preis_max)+"] für ["+str(Item)+"]",title="Achtung !!!",button='OK')

                    log("Suche nach Item im Flohmarkt")
                    Suche_Nach_Item(Item)

                    log("Auto Buy gestartet Start für ["+str(Item)+"!")
                    x = 0 

                    Preis = 1
                    Aktiv_if_window_name("EscapeFromTarkov")
                    log(" Pressing F5")
                    pyautogui.press('f5')
                    Error = allError()
                    start_time = time.time()
                    
                    log("Start Zeit für Item ["+str(Item)+"] ["+ str(time.strftime('%M:%S', time.localtime(start_time)))+"]")
                    while True:
                        Error = allError()
                        if Error == True:
                            start_time = time.time()
                            log("Start Zeit für Item ["+str(Item)+"] wurde wegen einer Error Warnung zurück gestellt auf ["+ str(time.strftime('%M:%S', time.localtime(start_time)))+"]")
                        current_time = time.time()
                        elapsed_time = current_time - start_time
                        log("Zeit für Item über ["+str(Item)+"] ["+ str(time.strftime('%M:%S', time.localtime(elapsed_time)))+"]")
                        if elapsed_time > 10:
                            break
                        Preis = Numbers_from_region(Fesnter_pos_Preis)
                        if Preis == None:
                            Preis = 1
                        Pries_Len = len(str(Preis))
                        if Pries_Len == Preis_Max_Len:
                            if Preis == Preis_max or Preis < Preis_max:
                                start_time = time.time()
                                log("Item wurde versucht zu kaufen. Start Zeit für Item ["+str(Item)+"] wurde zurück gestellt auf ["+ str(time.strftime('%M:%S', time.localtime(start_time)))+"]")
                                buy()
                        #anomali = pyautogui.confirm(text='Es ist eine unstimmkikeit aufgefallen soll das item für ['+str(Preis)+"] gekauft werden?", title='Anomalie!!!', buttons=['Kaufen !', 'Nicht kaufen!'])                    Zeit_pause(0.2)
                        if not Pries_Len == Preis_Max_Len or not Preis == Preis_max or not Preis < Preis_max:
                            pyautogui.press('f5')
                            Error = allError()
                            if Error == True:
                                start_time = time.time()
                                log("Start Zeit für Item ["+str(Item)+"] wurde wegen einer Error Warnung zurück gestellt auf ["+ str(time.strftime('%M:%S', time.localtime(start_time)))+"]")


else:
    log("Preis_max: "+str(Preis_max))
    Preis_max = int(Preis_max)
    Preis_Max_Len = len(str(Preis_max ))
    pyautogui.alert(text="Max Preis bestätigen ["+str(Preis_max)+"]",title="Achtung !!!",button='OK')


    while True:
        if keyboard.is_pressed(Hotkey_start):

            log("Auto Buy gestartet Start!")
            x = 0 
            while True:
                Preis = 1
                Aktiv_if_window_name("EscapeFromTarkov")
                pyautogui.press('f5')
                allError()
                while True:
                    Preis = Numbers_from_region(Fesnter_pos_Preis)
                    if Preis == None:
                        Preis = 1
                    Pries_Len = len(str(Preis))
                    if Pries_Len == Preis_Max_Len:
                        if Preis == Preis_max or Preis < Preis_max:
                            buy()
                            allError()
                        break
                    #anomali = pyautogui.confirm(text='Es ist eine unstimmkikeit aufgefallen soll das item für ['+str(Preis)+"] gekauft werden?", title='Anomalie!!!', buttons=['Kaufen !', 'Nicht kaufen!'])                    Zeit_pause(0.2)
                    else:
                        pyautogui.press('f5')
                        allError()
                        Zeit_pause(0.2)
            time.sleep(0.05)
        time.sleep(0.01)