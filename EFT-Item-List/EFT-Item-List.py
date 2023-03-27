v = "v0.0.1"
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
                Inventory Helper (Ammo)
###################################################
        - created by Napo_II
        - """ + v + """
        - python 3.7
        - https://github.com/NapoII/Napos-EFT-BOTS
###################################################\n"""
print(F1)

################################################################################################################################
#import

import cv2                  # für Bild erkennung
import numpy as np          # für Bild erkennung
import pyautogui            # für Bildschirm screanshot und Maus bewegung
import os                   # um Ordner des Scripts zu ermitteln
import sys, os
from win32gui import FindWindow, GetWindowRect
import pyautogui
import time
from PIL import Image

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

def Str_Slice(String):
    b = (String[0:3])
    a = (String[4:])
    return a , b

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

def Screanshot(window_rect, Img_name):

    Page_img_dir = Bot_Path +"/Bilder/"+Img_name+".png"

    myScreenshot = pyautogui.screenshot(region=(window_rect))   # Screanshot
    myScreenshot.save(r""+ Page_img_dir)
    return Page_img_dir


def filter(Page_img_dir):
    img_src = cv2.imread(Page_img_dir)

    #edge detection filter
    kernel = np.array([[1, 1, 1], 
                    [1, 1, 1],
                    [1, 1, 1]])

    kernel = kernel/(np.sum(kernel) if np.sum(kernel)!=0 else 1)

    #filter the source image
    img_rst = cv2.filter2D(img_src,-1,kernel)

    #save result image
    cv2.imwrite(Page_img_dir,img_rst)

def ItemFilterLayer(Page_img_dir, Result_img_dir, Item, thershold):
    Page_img_dir_T = Page_img_dir
    Item_T = Item

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
    Color = 0, 0, 0

    for (x, y) in zip(xloc, yloc):
        button = cv2.rectangle(Result, (x+15,y+15), (x + w-15, y + h-15) , (Color),2)
        #button = cv2.putText(Result, 'H', (x+20,y+42), cv2.FONT_HERSHEY_SIMPLEX, 1, (Color), 3, cv2.FONT_HERSHEY_PLAIN)
        button = cv2.putText(Result, Item, (x+20,y+42), cv2.FONT_HERSHEY_SIMPLEX, 1, (Color), 1, cv2.FONT_HERSHEY_PLAIN)

    button = cv2.line(Result, (0,0), (0,0), (0,255,255), 1)   # umrandet button
    #image = cv2.rectangle(image, start_point, end_point, color, thickness)
    #image = cv2.line(image, start_point, end_point, color, thickness)
    os.chdir(Bot_Path+"/Bilder/")
    #cv2.imshow('button', button)
    cv2.imwrite('Result.png',button)

    cv2.waitKey()
    cv2.destroyAllWindows()

    #return(len(xloc))

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

def Img_Padge(Img_BG, Img_Padge, Result_img_dir, Pos):
    Img_BG = Image.open(Img_BG)
    Img_Padge = Image.open(Img_Padge)

    back_im = Img_BG.copy()
    back_im.paste(Img_Padge)
    back_im.save(Result_img_dir, quality=95)

    back_im = Img_BG.copy()
    back_im.paste(Img_Padge, Pos)
    back_im.save(Result_img_dir, quality=95)


def Zeit_pause(seconds):
    start_time = time.time()
    while True:                             # Zeit schelife startet
        current_time = time.time()
        elapsed_time = current_time - start_time        # berechung rest Zeit
        if elapsed_time > seconds:
            break


def Shift_plus_Klick(x,y):
    pyautogui.keyDown('shift')  # hold down the shift key
    pyautogui.click(x, y)
    pyautogui.keyUp('shift')    # release the shift key
    Zeit_pause(0.5)

################################################################################################################################
#PreSet Programm

Doku_Folder = Folder_gen ("EFT - Inventory Helper", "Documents/")
Log_Folder = Folder_gen ("Log", "Documents/EFT - Inventory Helper")
Log_File_name = Datei_name_mit_Zeit ("LogFile-AmmoTool")
Log_File = Erstelle_TextDatei (Log_File_name, Log_Folder, F1 + "Log-File\n")


window_name = "EscapeFromTarkov"
Bot_Path = os.path.dirname(sys.argv[0])

Low_Ammo_List_dir = Bot_Path +"/Ballin on a Budget - Kopie.txt"
Best_Ammo_list_dir = Bot_Path +"/Best Overall - Kopie.txt"
Filter_Ammo_List_dir = Bot_Path +"/Fillter_List.txt"

Low_Ammo_List = Textdatei_to_List(Low_Ammo_List_dir)
Best_Ammo_List = Textdatei_to_List(Best_Ammo_list_dir)
Filter_List = Textdatei_to_List(Low_Ammo_List_dir)



log ( "Bot_Path: ["+str(Bot_Path) + "]\n")
log ("List: Low_Ammo:")
log ("Low_Ammo_List_dir: ["+str(Low_Ammo_List_dir) + "]")
log (str(Low_Ammo_List))

log ("\n")

log ("List: Best_Ammo:")
log ("Best_Ammo_list_dir: ["+str(Best_Ammo_list_dir) + "]")
log (str(Best_Ammo_List))
log ("\n")
################################################################################################################################
# Main Programm

window_rect = that_window_pos(window_name)
pyautogui.alert("einzugeben!")
Page_img_dir = Screanshot(window_rect, "Page")
Result_img_dir = Screanshot(window_rect, "Result")
#filter(Page_img_dir)

Len = len(Best_Ammo_List)
List = "Best"
Prozent_1 = (100/Len) 
while True:
    Len = Len - 1
    Prozent = int(100-(Prozent_1 * Len))
    print(str(Prozent) + " %")
    if Len == 0 :
        break
    Item = Best_Ammo_List.pop()

    Item = Str_Slice(Item)
    Ammo = Item[0]
    thershold = float(Item[1])

    log("AMMO : "+str(Ammo)+"\n			List:		Best_Ammo_List\n 			Thershold :	"+str(thershold)+"\n")   
    ItemCount(Page_img_dir, Result_img_dir, Ammo, thershold, List)
    print("\n")

pyautogui.alert(text="High Bullet Fertig !!!",title="Done !!!",button='OK')

Len = len(Low_Ammo_List)
List = "Low"
Prozent_1 = (100/Len)
while True:
    Len = Len - 1
    Prozent = int(100-(Prozent_1 * Len))
    print(str(Prozent) + " %")
    if Len == 0 :
        break
    Item = Low_Ammo_List.pop()

    Item = Str_Slice(Item)

    Ammo = Item[0]
    thershold = float(Item[1])

    log("AMMO :		"+str(Ammo)+"\n			List:		Low_Ammo_List\n 			Thershold :	"+str(thershold)+"\n")
    
    ItemCount(Page_img_dir, Result_img_dir, Ammo, thershold, List)
    print("\n")

pyautogui.alert(text=" lowBullet Fertig !!!",title="Done !!!",button='OK')




################################################################################################################################