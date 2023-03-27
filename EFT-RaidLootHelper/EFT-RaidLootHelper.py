################################################################################################################################
#Intro:

v = "v0.0.3.RLH"
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
                RaidLootHelper
###################################################
        - created by Maniac & Napo_II
        - """ + v + """
        - python 3.7
        - https://github.com/NapoII/Napos-EFT-BOTS
###################################################\n"""
print(F1)

################################################################################################################################
#import:

from base64 import standard_b64decode
import os
import os, sys
import time
import requests
import gtts
from pygame import mixer
import sounddevice as sd
from scipy.io.wavfile import write
import soundfile
import time
import speech_recognition as sr
import winsound
import keyboard
import pyautogui
import webbrowser

################################################################################################################################
#def:

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

def Text_to_Sound(Text, Lang, dir):
    log(Text)
    tts = gtts.gTTS(Text, lang= Lang)
    tts.save(dir)
    Play_Sound(dir)



def Play_Sound(dir):
    log("Sound abgespielt="+str(dir))
    mixer.init()
    mixer.music.load(dir)
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(0.1)
    mixer.music.unload
    mixer.quit()

def Zeit_pause(seconds):
        start_time = time.time()
        while True:                             # Zeit schelife startet
            current_time = time.time()
            elapsed_time = current_time - start_time        # berechung rest Zeit
            if elapsed_time > seconds:
                break

def Voice_rec(dir,seconds):
    fs = 44100  # Sample rate
      # Duration of recording
    log("Voice Rec START for ["+str(seconds)+"] seconds.")
    winsound.Beep(500, 200)
    winsound.Beep(1000, 200)
    winsound.Beep(500, 200)
    
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)


    start_time = time.time()
    x = seconds +1
    while True:                             # Zeit schelife startet
        current_time = time.time()
        elapsed_time = current_time - start_time
        
        start_time2 = time.time()
        while True:                            # Zeit schelife startet
            current_time2 = time.time()
            elapsed_time2 = current_time2 - start_time2        # berechung rest Zeit
            if elapsed_time2 > 1:
                winsound.Beep(500, 100)
                x = x - 1
                print("Voice Rec ["+str(x)+"] sec left.")
                break

        if elapsed_time > seconds:
            winsound.Beep(500, 200)
            winsound.Beep(1000, 200)
            winsound.Beep(500, 200)
            break


    sd.wait()  # Wait until recording is finished
    write(dir, fs, myrecording)  # Save as WAV file 
    log("Voice Rec End -> ["+str(dir)+"]")

    data, samplerate = soundfile.read(dir)
    soundfile.write(dir, data, samplerate, subtype='PCM_16')
    return dir


def Voice_To_Text(dir):

    data, samplerate = soundfile.read(dir)
    soundfile.write(dir, data, samplerate, subtype='PCM_16')

    # initialize the recognizer
    r = sr.Recognizer()
    # open the file
    with sr.AudioFile(dir) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        try:
            text = r.recognize_google(audio_data,language="de-DE")
            log("Voice_To_Text Output >>> ["+str(text)+"] <<<\n")
            return text
        except:
            log("Voice_To_Text Output >>> [] <<<\n")
            return False

################################################################################################################################
#Pre Set:

file_path = os.path.dirname(sys.argv[0])


Doku_Folder = Folder_gen ("EFT - Inventory Helper", "Documents/")
Log_Folder = Folder_gen ("Log", "Documents/EFT - Inventory Helper")
Log_File_name = Datei_name_mit_Zeit ("LogFile-RaidLootHelper")
Log_File = Erstelle_TextDatei (Log_File_name, Log_Folder, F1 + "Log-File\n")

API_Key = "KjC4QvLqfVqDGVRO"
url = "https://tarkov-market.com/api/v1/"

Voice_File = Log_Folder + "//Voice_File.wav"
Voice_File2 = Log_Folder + "//Voice_File2.mp3"

hotkey = pyautogui.prompt(text='HOTKEY für Voice abfrage.', title=' EFT- RaidLootHelper - HOTKEY SETTING' , default='p')
hotkey2 = pyautogui.prompt(text='HOTKEY für Manuele Eingabe.', title=' EFT- RaidLootHelper - HOTKEY SETTING' , default='l')

print("\n")
################################################################################################################################
#Programm: Item_preis_Request


def Item_preis_Request():
    while True:

        if keyboard.is_pressed(hotkey):
            
            Voice_rec(Voice_File,3)
            Voice_text = Voice_To_Text(Voice_File)

            if Voice_text == False:
                Voice_Line_Text = "Ihre Aufnahme war Leer. Versuche es Nochmal!"
                Text_to_Sound(Voice_Line_Text, "de", Voice_File2)

            if Voice_text == "googel" or Voice_text == "Google":
                Text_to_Sound("Nach welchem begriff soll gesucht werden?", "de", Voice_File2)
                Voice_rec(Voice_File,3)
                suchbegriff = Voice_To_Text(Voice_File)
                url_G = 'https://www.google.de/search?q='
                webbrowser.open(url_G+"EFT "+suchbegriff)
                log("URL open:"+ str(url_G) + "EFT " + str(suchbegriff))
                Text_to_Sound("Die Googel Suche "+ str(suchbegriff)+ " Wurde geöffnet ", "de", Voice_File2)
                continue


            if Voice_text == "Öffne Map" or Voice_text == "öffne map" or Voice_text == "öffne " or Voice_text == "öffnen" or Voice_text == "öffne karte" or Voice_text == "karte öffnen"or Voice_text == "Karte öffnen "or Voice_text == "Map öffnen"or Voice_text == "map öffnen":  
                Text_to_Sound("Welche Karte soll geöffnet werden?", "de", Voice_File2)
                Voice_rec(Voice_File,3)
                Map_name = Voice_To_Text(Voice_File)
                
                if type(Map_name) == str:
                    Map_name = Map_name.lower()
                else:
                    Text_to_Sound("Es Wurde keine Karte genannt. Suche wird beendet. ", "de", Voice_File2)
                    continue
        
                if Map_name == "factory" or Map_name == "fabrik":
                    log("Open URL ["+str(Factory_Map)+"]")
                    webbrowser.open(Factory_Map)
                    Text_to_Sound("Die Karte factory wurde geöffnet.", "de", Voice_File2)

                if Map_name == "reserve" or Map_name == "wisag" or Map_name == "resurf" or Map_name =="wieso" or Map_name =="iserv" or Map_name =="militär":
                    log("Open URL ["+str(Reserve_Map)+"]")
                    webbrowser.open(Reserve_Map)
                    Text_to_Sound("Die Karte reserve wurde geöffnet.", "de", Voice_File2)

                if Map_name == "customs" or Map_name == "zollgelände":
                    log("Open URL ["+str(Customs_Map)+"]")
                    webbrowser.open(Customs_Map)
                    Text_to_Sound("Die Karte zollgelände wurde geöffnet.", "de", Voice_File2)

                if Map_name == "interchange" or Map_name == "autobahn" or Map_name == "autobahnkreuz" or Map_name == "interchange" or Map_name == "autobahnkreuz":
                    log("Open URL ["+str(Interchange_Map)+"]")
                    webbrowser.open(Interchange_Map)
                    Text_to_Sound("Die Karte autobahnkreuz wurde geöffnet.", "de", Voice_File2)

                if Map_name == "woods" or Map_name == "wald" or Map_name == "wutz":
                    log("Open URL ["+str(Woods_Map)+"]")
                    webbrowser.open(Woods_Map)
                    Text_to_Sound("Die Karte wald wurde geöffnet.", "de", Voice_File2)

                if Map_name == "lighthouse" or Map_name == "leuchttrum":
                    log("Open URL ["+str(Lighthouse_Map)+"]")
                    webbrowser.open(Lighthouse_Map)
                    Text_to_Sound("Die Karte leuchttrum wurde geöffnet.", "de", Voice_File2)

                if Map_name == "lab" or Map_name == "labs" or Map_name == "labor":
                    log("Open URL ["+str(Lab_Map)+"]")
                    webbrowser.open(Lab_Map)
                    Text_to_Sound("Die Karte labor wurde geöffnet.", "de", Voice_File2)
                continue

            else:


                Item_full_request = tm_request_Item (API_Key, url, Voice_text )
                if Item_full_request == False:
                    Voice_Line_Text = "Kein Eintrag für "+ str(Voice_text)
                    Text_to_Sound(Voice_Line_Text, "de", Voice_File2)

                else:

                    Name = Item_full_request["name"]
                    tags = Item_full_request ["tags"]
                    shortName = Item_full_request ["shortName"]
                    avg24hPrice = Item_full_request ["avg24hPrice"]
                    diff24h = Item_full_request ["diff24h"]
                    diff7days = Item_full_request ["diff7days"]
                    traderName = Item_full_request ["traderName"]
                    traderPrice = Item_full_request ["traderPrice"]
                    slots = Item_full_request ["slots"]
                    updated = Item_full_request ["updated"]

                    traderPriceCur = Item_full_request ["traderPriceCur"]
                    if traderPriceCur == "₽":
                        traderPriceCur = "Rubel","RUB"
                    if traderPriceCur == "€":
                        traderPriceCur = "Euro", "EUR"
                    if traderPriceCur == "$":
                        traderPriceCur = "Dollar","Dollar"

                    card_1 =    "\n"+"--------------------------------------------------------"+"\n"
                    card_2 =    "   " + str(Name)+" ( "+str(shortName)+ " ) - Slot: "+str(slots)+ " - "+str(tags)+"\n"
                    card_3 =    "--------------------------------------------------------"+"\n"
                    card_4 =    "-- Flohmarkt Preis 24h	 ---> 	"+str(avg24hPrice)+ "	"+str(traderPriceCur[1])+"\n"
                    card_5 =    "-- Preis änderung in 24h ---> 	"+str(diff24h)+ "	%"+"\n"
                    card_6 =    "-- Preis änderung in 7d	 --->	"+str(diff7days)+ "	%"+"\n"
                    card_7 =    "-- "+str(traderName)+" 		--->	"+str(traderPrice)+ "	"+str(traderPriceCur[1])+"\n"
                    card_8 =    "--------------------------------------------------------"+"\n"
                    card_9 =    "	"+str(updated)+"\n"
                    log(str(card_1)+str(card_2)+str(card_3)+str(card_4)+str(card_5)+str(card_6)+str(card_7)+str(card_8)+str(card_9))


                    Voice_Line_Text = (r"Der Preis für " + str(Name) + " liegt bei "+ str(avg24hPrice)+" "+str(traderPriceCur[0]))

                    Text_to_Sound(Voice_Line_Text, "de", Voice_File2)

        if keyboard.is_pressed(hotkey2):
            
            Voice_text = pyautogui.prompt(text='HOTKEY für abfrage Zeitraum bestimmen.', title=' X und Y Coredinate der Maus bestimmen' , default='Bit') 

            if Voice_text == False:
                Voice_Line_Text = "Ihre Aufnahme war Leer. Versuche es Nochmal!"
                Text_to_Sound(Voice_Line_Text, "de", Voice_File2)
                continue
            else:


                Item_full_request = tm_request_Item (API_Key, url, Voice_text )
                if Item_full_request == False:
                    Voice_Line_Text = "Kein Eintrag für "+ str(Voice_text)
                    Text_to_Sound(Voice_Line_Text, "de", Voice_File2)

                else:

                    Name = Item_full_request["name"]
                    tags = Item_full_request ["tags"]
                    shortName = Item_full_request ["shortName"]
                    avg24hPrice = Item_full_request ["avg24hPrice"]
                    diff24h = Item_full_request ["diff24h"]
                    diff7days = Item_full_request ["diff7days"]
                    traderName = Item_full_request ["traderName"]
                    traderPrice = Item_full_request ["traderPrice"]
                    slots = Item_full_request ["slots"]
                    updated = Item_full_request ["updated"]

                    traderPriceCur = Item_full_request ["traderPriceCur"]
                    if traderPriceCur == "₽":
                        traderPriceCur = "Rubel","RUB"
                    if traderPriceCur == "€":
                        traderPriceCur = "Euro", "EUR"
                    if traderPriceCur == "$":
                        traderPriceCur = "Dollar","Dollar"

                    card_1 =    "\n"+"--------------------------------------------------------"+"\n"
                    card_2 =    "   " + str(Name)+" ( "+str(shortName)+ " ) - Slot: "+str(slots)+ " - "+str(tags)+"\n"
                    card_3 =    "--------------------------------------------------------"+"\n"
                    card_4 =    "-- Flohmarkt Preis 24h	 ---> 	"+str(avg24hPrice)+ "	"+str(traderPriceCur[1])+"\n"
                    card_5 =    "-- Preis änderung in 24h ---> 	"+str(diff24h)+ "	%"+"\n"
                    card_6 =    "-- Preis änderung in 7d	 --->	"+str(diff7days)+ "	%"+"\n"
                    card_7 =    "-- "+str(traderName)+" 		--->	"+str(traderPrice)+ "	"+str(traderPriceCur[1])+"\n"
                    card_8 =    "--------------------------------------------------------"+"\n"
                    card_9 =    "	"+str(updated)+"\n"
                    log(str(card_1)+str(card_2)+str(card_3)+str(card_4)+str(card_5)+str(card_6)+str(card_7)+str(card_8)+str(card_9))


                    Voice_Line_Text = (r"Der Preis für " + str(Name) + " liegt bei "+ str(avg24hPrice)+" "+str(traderPriceCur[0]))

                    Text_to_Sound(Voice_Line_Text, "de", Voice_File2)



            time.sleep(0.05)
        time.sleep(0.01)

################################################################################################################################
##Programm: Map_info
Map_List = ["Factory", "Reserve" ,"Customs", "Interchange", "Woods", "Lighthouse", "Lab", "Shorelin" ]
#Maps_Data::
#Factory:
Factory_Wiki = r"https://escapefromtarkov.fandom.com/wiki/Factory"
Factory_Map = r"https://mapgenie.io/tarkov/maps/factory"

#Reserve:
Reserve_Wiki = r"https://escapefromtarkov.fandom.com/wiki/Reserve"
Reserve_Map = r"https://static.wikia.nocookie.net/escapefromtarkov_gamepedia/images/4/42/3D_Map_by_loweffortsaltbox.png/"

#Customs:
Customs_Wiki = r"https://escapefromtarkov.fandom.com/wiki/Customs"
Customs_Map = r"https://mapgenie.io/tarkov/maps/customs"

#Interchange:
Interchange_Wiki = r"https://escapefromtarkov.fandom.com/wiki/Interchange"
Interchange_Map =r"https://mapgenie.io/tarkov/maps/Interchange"

#Woods:
Woods_Wiki = r"https://escapefromtarkov.fandom.com/wiki/Woods"
Woods_Map = r"https://mapgenie.io/tarkov/maps/woods"

#Lighthouse:
Lighthouse_Wiki = r"https://escapefromtarkov.fandom.com/wiki/Lighthouse"
Lighthouse_Map = r"https://eftmkg.com/lighthouse-full-Jindouz.html#2"

#The_Lab:
Lab_Wiki = r"https://escapefromtarkov.fandom.com/wiki/The_Lab"
Lab_Map = r"https://mapgenie.io/tarkov/maps/lab"

#Shorelin:
Shorelin_Wiki = r"https://escapefromtarkov.fandom.com/wiki/Shoreline"
Shorelin_Map = r"https://eftmkg.com/shoreline-full.html#3"





#################################################################################################################################




Item_preis_Request()