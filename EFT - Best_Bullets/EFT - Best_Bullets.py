py_name = "EFT - Best_Bullets" 
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

import imp
import os
import os, sys
import time
import pyautogui
import requests
import cv2

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

API_Key = "KjC4QvLqfVqDGVRO"
url = "https://tarkov-market.com/api/v1/"

def half_img_save_from_api(url, dir, name):

    dir = dir + "//"+str(name)+".png"
    var = requests.get(url)

    with open(dir,"wb") as f:
        f.write(var.content)

    img = cv2.imread(dir)
    # cv2.imread() -> takes an image as an input
    h, w, channels = img.shape
    # this is horizontal division
    half2 = h//2
    top = img[:half2, :]

    #cv2.imshow('Top', top)
    #cv2.waitKey(0)
    cv2.imwrite(dir,top)

def tm_request_Item (API_Key, url, Item ):

    log("Item Request:")
    log("Item:" + str(Item) + ", API_Key:" + str(API_Key)+ ", Url:" +str(url))
    url = url+ "item?q=" + Item + "&x-api-key=" + API_Key
    log(str(url)+"\n")
    # url = "https://tarkov-market.com/api/v1/"

    res = requests.get(url) # request the API Full URL
    json = res.json()       # Convert request to Json Data
    #print(json)
    try:
        dic = (json[0])         # Delt List
    except:
        dic = False
    return dic              # Output the request

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

def half_img_save_from_api(url, dir, name):

    dir = dir + "//"+str(name)+".png"
    var = requests.get(url)

    with open(dir,"wb") as f:
        f.write(var.content)

    img = cv2.imread(dir)
    # cv2.imread() -> takes an image as an input
    h, w, channels = img.shape
    # this is horizontal division
    half2 = h//2
    top = img[:half2, :]

    #cv2.imshow('Top', top)
    #cv2.waitKey(0)
    cv2.imwrite(dir,top)

def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()

################################################################################################################################

Best_Bullet_list_dir = file_path + "//" + "Best_Bullet.txt"
Best_Bullet_list = Textdatei_to_List(Best_Bullet_list_dir)


while True:

    Best_Bullet_list_len = len(Best_Bullet_list)
    if Best_Bullet_list_len == 0: 
        break

    Item = Best_Bullet_list.pop(0)
    Item_full_request = tm_request_Item (API_Key, url, Item)

    Name = Item_full_request["name"]
    icon_url = Item_full_request["icon"]

    half_img_save_from_api(icon_url, file_path_Bilder, Name)

pyautogui.alert(text='Bilder wurden erstellt.', title='Best Bullet List', button='OK')