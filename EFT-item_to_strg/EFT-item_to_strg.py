py_name = "EFT-item_to_strg" 
v = "0.0.1"
####################################################################################################
# #   Intro

f0 =  """ 


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

import pytesseract
import keyboard
import pyperclip
import winsound

file_path = os.path.dirname(sys.argv[0])
#pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = file_path +"\\Tesseract-OCR\\tesseract.exe"


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

def Img_to_str(img):
    result = pytesseract.image_to_string(img)
    log("Es wurde  folgender Str ausgelsen: "+ str(result))
    return result

def def_pos():
    x, y = pyautogui.position()
    log(("x,y pos: (") + str(x) + "," + str(y) +")")
    return x,y

def BimBam():
    winsound.Beep(500, 200)
    #winsound.Beep(1000, 200)
    #winsound.Beep(500, 200)

################################################################################################################################
#Main programm


Hotkey_start = pyautogui.prompt(text='HotKey Festlegen um Str zu scan', title="HotKey Festlegen" , default='s')
log("Hotkey_start: "+str(Hotkey_start)+"\n")

while True:
    if keyboard.is_pressed(Hotkey_start):

        time.sleep(0.5)
        log (str(Hotkey_start) + " get pressd >>> Scan Start!")
        pos = def_pos()
        ScrenS = pyautogui.screenshot(region=((pos[0]),((pos[1])-22), 500, 22))
        result = Img_to_str(ScrenS)
        pyperclip.copy(result)
        BimBam()
        print ("Ergebniss: [" + str(result) + "] wurde dem ClipBoard hinzugefüht.")
        time.sleep(1)



        

    time.sleep(0.01)

    