py_name = "Take_Best_bullets" 
v = "0.0.1"
####################################################################################################
# #   Intro

f0 =  """ 
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

- """ + py_name + """
- created by Napo_II
- """ + v + """
- python 2.7
- https://github.com/NapoII/

"""
print(" \nProgramm wird gestartet ...")

####################################################################################################
#import

import os
import os, sys
import time
import pyautogui
import keyboard
from win32gui import FindWindow, GetWindowRect
import cv2
import numpy as np  

####################################################################################################
#def

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

def Zeit_pause(seconds):
    start_time = time.time()
    while True:                             # Zeit schelife startet
        current_time = time.time()
        elapsed_time = current_time - start_time        # berechung rest Zeit
        if elapsed_time > seconds:
            break

################################################################################################################################
#PreSet Programm

file_path = os.path.dirname(sys.argv[0])
file_path_Bilder = file_path + "/Bilder/"
file_path_Work_Folder = file_path + "/Work_Folder/"


Doku_Folder = Folder_gen (py_name, "Documents/")
Log_Folder = Folder_gen ("Log", ("Documents/"+str(py_name)))
Log_File_name = Datei_name_mit_Zeit ("LogFile-"+str(py_name))
Log_File = Erstelle_TextDatei (Log_File_name, Log_Folder, f0 + "Log-File:\n---------------------------------------------------------------------------------------\n")

Bot_Path = os.path.dirname(sys.argv[0])

log ( "Bot_Path: ["+str(Bot_Path) + "]\n")

print(f0)

################################################################################################################################
# def

def Textdatei_to_List(dir):
    with open(dir) as r:
        data = r.readlines()

    data_len = len(data)
    data_list = []

    while True:
        data_len = len(data)
        if data_len == 0:
            break
        Item = data.pop()
        Item = Item.replace('\n',"")
        data_list.append(Item)

    return data_list

def Screanshot(window_rect, Img_name):
    cv2.waitKey()
    cv2.destroyAllWindows()
    Page_img_dir = Bot_Path +"/Bilder/"+Img_name+".png"

    myScreenshot = pyautogui.screenshot(region=(window_rect))   # Screanshot
    myScreenshot.save(r""+ Page_img_dir)
    return Page_img_dir

def that_window_pos(window_name):

    # FindWindow takes the Window Class name (can be None if unknown), and the window's display text. 
    
    while True:
        try:
            window_handle = FindWindow(None, window_name)
            window_rect   = GetWindowRect(window_handle)
            break
        except:
            print (" Das Fenster >>> "+str(window_name)+" <<< konnte nicht gefunden werden")

    print("Das Fenster >> "+ str(window_name) + "<<< ist auf pos > "+ str(window_rect))
    #(0, 0, 800, 600)
    return window_rect

def Str_Slice(String):
    b = (String[0:3])
    a = (String[4:])
    return a , b

def Shift_plus_Klick(x,y):
    pyautogui.keyDown('shift')  # hold down the shift key
    pyautogui.click(x, y)
    pyautogui.keyUp('shift')    # release the shift key
    Zeit_pause(0.5)

def ItemCount(Page_img_dir, Result_img_dir, Item, thershold, List):
    Page_img_dir_T = Page_img_dir
    Item_T = Item

    if List == "Low":
        x2 = 10
        y2 = 50
        Text = "L"
        Farbe =  255, 255 , 100
    if List == "Best":
        x2 = 40
        y2 = 50
        Text = "B"
        Farbe = 0, 215, 215

    cv2.waitKey()
    cv2.destroyAllWindows()

    button_img_dir = Bot_Path +"/Bilder/"+ Item_T + ".png"

    Result = cv2.imread(Result_img_dir, cv2.IMREAD_UNCHANGED)
    Page = cv2.imread(Page_img_dir_T, cv2.IMREAD_UNCHANGED)   # transform IMG in cv2
    button = cv2.imread(button_img_dir, cv2.IMREAD_UNCHANGED)

    #cv2.imshow('Page', Page)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

    #cv2.imshow('button', button)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

    result = cv2.matchTemplate(Page, button, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    thershold_x = thershold
    yloc, xloc = np.where(result >= thershold_x)

    if max_val >= thershold_x:
        Found = True
    else:
        Found = False

    log("Max_val:	" + str(max_val)+ "\n			Max_loc:	" + str(max_loc)+"\n			Found =		"+ str(Found) +"\n")

    #cv2.imshow('result', result)
    cv2.waitKey()
    cv2.destroyAllWindows()

    w = button.shape[1]     #legt die größe des button fest
    h = button.shape[1]

    LX = []
    LY = []
    for (x, y) in zip(xloc, yloc):
        #button = cv2.rectangle(Result, (x+15,y+15), (x + w-15, y + h-15) , (255,255,255),2)

        Shift_plus_Klick(x+10,y+10)
        button = cv2.putText(Result, Text, (x+x2,y+y2), cv2.FONT_HERSHEY_SIMPLEX, 1, (Farbe), 2, cv2.FONT_HERSHEY_PLAIN)
        #button = cv2.putText(Result, Item, (x+20,y+42), cv2.FONT_HERSHEY_SIMPLEX, 1, (Farbe), 1, cv2.FONT_HERSHEY_PLAIN)

    button = cv2.line(Result, (0,0), (0,0), (0,255,255), 1)   # umrandet button
    #image = cv2.rectangle(image, start_point, end_point, color, thickness)
    #image = cv2.line(image, start_point, end_point, color, thickness)
    os.chdir(Bot_Path+"/Bilder/")
    #cv2.imshow('button', button)
    cv2.imwrite('Result.png',button)

    cv2.waitKey()
    cv2.destroyAllWindows()

    #return(len(xloc))

def found(Img_dir, region, Genauigkeit):
    print("found(Img_dir, region, Genauigkeit)")
    cv2.waitKey()
    cv2.destroyAllWindows()

    myScreenshot = pyautogui.screenshot(region=(region))   # Screanshot
    open_cv_image = np.array(myScreenshot) 
    # Convert RGB to BGR 
    myScreenshot = open_cv_image[:, :, ::-1].copy()
    Screanshot(region, "found_Test")
    button = cv2.imread(Img_dir, cv2.IMREAD_UNCHANGED)

    result = cv2.matchTemplate(myScreenshot, button, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    #print("min_val: " +str(min_val))
    #print("min_loc: " +str(min_loc))

    #print("max_val: " +str(max_val))
    #print("max_loc: " +str(max_loc))
    cv2.waitKey()
    cv2.destroyAllWindows()

    if max_val > Genauigkeit or max_val == Genauigkeit:
        print ("max_val: " + str(max_val))
        print ("max_loc: " + str(max_loc))
        return max_loc, max_val
    else:
        print ("max_val: " + str(max_val))
        return False

def Shift_plus_Klick(x,y):
    pyautogui.keyDown('shift')  # hold down the shift key
    pyautogui.click(x, y)
    pyautogui.keyUp('shift')    # release the shift key
    Zeit_pause(0.5)

def working_str(str):
    str = (str.replace("\"", "")) 
    str = (str.replace("/", "-"))
    return str

################################################################################################################################
# pre data

Stach_regio = (1232,0,688,1079)
Low_Ammo_List_dir = Bot_Path +"/Low_Ammo_List_Class3.txt"
Low_Ammo_List = Textdatei_to_List(Low_Ammo_List_dir)

High_Ammo_List_dir = Bot_Path +"/High_Ammo_List_Class4plus.txt"
High_Ammo_List = Textdatei_to_List(High_Ammo_List_dir)

window_name = "EscapeFromTarkov"

hotkey = pyautogui.prompt(text='HOTKEY Um den Bullet Pick zu starten.', title='Take Best bullets' , default='s')


################################################################################################################################

log ("List: Low_Ammo:")
log ("Low_Ammo_List_dir: ["+str(Low_Ammo_List_dir) + "]")
log (str(Low_Ammo_List) + "\n")


print("RDY !")

while True:

    if keyboard.is_pressed(hotkey):
        break

window_rect = that_window_pos(window_name)
Low_Ammo_List_Len = len(Low_Ammo_List)

while True:
    Low_Ammo_List_Len = len(Low_Ammo_List)
    if Low_Ammo_List_Len == 0:
        break

    Item = Low_Ammo_List.pop(0)
    Item_imge_dir = file_path_Bilder + Item + ".png"
    print(Item)
    x = 0
    Main_Cheack = 0.83
    cheack = Main_Cheack
    while True:
        #x = x + 1
        #Screanshot(Stach_regio, str(x))
        print("cheack: "+str(cheack))

        pos = found(Item_imge_dir, Stach_regio, cheack)
        if pos == False:
            break
        cheack = pos[1]-0.05
        if cheack < Main_Cheack:
            cheack = Main_Cheack
        pos = pos[0]
        if pos != False:

            pos = (Stach_regio[0]+pos[0])+10, (pos[1])+10
            print("ONE PICK\n")
            print(Item)
            Shift_plus_Klick(pos[0],pos[1])
            Zeit_pause(0.5)

print("RDY !")

while True:

    if keyboard.is_pressed(hotkey):
        break

window_rect = that_window_pos(window_name)
High_Ammo_List_Len = len(High_Ammo_List)

while True:
    High_Ammo_List_Len = len(High_Ammo_List)
    if High_Ammo_List_Len == 0:
        break

    Item = High_Ammo_List.pop(0)
    Item_imge_dir = file_path_Bilder + Item + ".png"
    print(Item)
    x = 0
    Main_Cheack = 0.83
    cheack = Main_Cheack
    while True:
        #x = x + 1
        #Screanshot(Stach_regio, str(x))
        print("cheack: "+str(cheack))

        pos = found(Item_imge_dir, Stach_regio, cheack)
        if pos == False:
            break
        cheack = pos[1]-0.05
        if cheack < Main_Cheack:
            cheack = Main_Cheack
        pos = pos[0]
        if pos != False:

            pos = (Stach_regio[0]+pos[0])+10, (pos[1])+10
            print("ONE PICK\n")
            print(Item)
            Shift_plus_Klick(pos[0],pos[1])
            Zeit_pause(0.5)


print("ENDE")
