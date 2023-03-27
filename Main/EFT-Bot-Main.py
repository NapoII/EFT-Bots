v = "v0.0.2.Main"
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
                Bots
###################################################
        - created by Napo_II
        - """ + v + """
        - python 3.7
        - https://github.com/NapoII/Napos-EFT-BOTS
###################################################\n"""
print(F1)
################################################################################################################################

import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import os, sys
import os
import time
import webbrowser

################################################################################################################################
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "newproject"

file_path = os.path.dirname(sys.argv[0])
file_path_Bilder = file_path + "/Bilder"

EFTBotLogo = file_path_Bilder + "/EFT_Bot_Logo.png"
Ammo_Fill_logo = file_path_Bilder + "/Ammo_Fill_logo.png"
Best_Bullet_logo = file_path_Bilder + "/Best_Bullet_logo.png"
Auto_BUY_logo = file_path_Bilder + "/Auto_BUY_logo.png"
Raid_helper_logo = file_path_Bilder + "/Raid_Loot-Helper_logo.png"

"""
command= openGitHub
, command= Start_Raid_LootHelper
, command= Start_Ammo_Fill_exe
, command= Start_Best_Bullet_exe)
, command= Start_Auto_BUY_exe"""



file_path = os.path.dirname(sys.argv[0])
file_path =(file_path.replace("\\","/"))

 
Ammo_Fill_exe = file_path + "/EFT_Bot-Ammo_Fill/EFT_Bot-Ammo_Fill.exe"
Best_Bullet_exe = file_path + "/EFT_Best_Bullet/EFT-Best_Bullet.exe"
Auto_BUY_exe =  file_path + "/EFT_Bot-Auto_Buy/EFT_Bot-Auto_Buy.exe"
Raid_LootHelper_exe = file_path + "/EFT-RaidLootHelper\EFT-RaidLootHelper.exe"


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


def openGitHub():
    webbrowser.open("https://github.com/NapoII/EFT-Bots")

def Start_Ammo_Fill_exe():
    log ("Starte ["+ str(Ammo_Fill_exe)+"]")
    os.system(Ammo_Fill_exe)

def Start_Best_Bullet_exe():
    log ("Starte ["+ str(Best_Bullet_exe)+"]")
    os.system(Best_Bullet_exe)

def Start_Auto_BUY_exe():
    log ("Starte ["+ str(Auto_BUY_exe)+"]")
    os.system(Auto_BUY_exe)

def Start_Raid_LootHelper():
    log ("Starte ["+ str(Raid_LootHelper_exe)+"]")
    os.system(Raid_LootHelper_exe)


file_path = os.path.dirname(sys.argv[0])
Bilder_Folder = str(file_path)+"/Bilder"
Doku_Folder = Folder_gen ("EFT - Inventory Helper", "Documents/")
Log_Folder = Folder_gen ("Log", "Documents/EFT - Inventory Helper")
Log_File_name = Datei_name_mit_Zeit ("EFT_Bots_Main")
Log_File = Erstelle_TextDatei (Log_File_name, Log_Folder, F1 + "Log-File\n")

################################################################################################################################


import pathlib
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Template.ui"


class TemplateWidget(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(TemplateWidget, self).__init__(master, **kw)
        self.frame3 = ttk.Frame(self)
        self.button_EFTBotLogo = ttk.Button(self.frame3)
        self.img_EFTBotLogo = tk.PhotoImage(file=EFTBotLogo)
        self.button_EFTBotLogo.configure(image=self.img_EFTBotLogo, text='command= openGitHub',command= openGitHub)
        self.button_EFTBotLogo.pack(side='top')
        self.button_Raid_helper = ttk.Button(self.frame3)
        self.img_Raid_helper_logo = tk.PhotoImage(file=Raid_helper_logo)
        self.button_Raid_helper.configure(image=self.img_Raid_helper_logo, text='command= Start_Raid_LootHelper',command= Start_Raid_LootHelper)
        self.button_Raid_helper.pack(side='left')
        self.button_Ammo_Fill = ttk.Button(self.frame3)
        self.img_Ammo_Fill_logo = tk.PhotoImage(file=Ammo_Fill_logo)
        self.button_Ammo_Fill.configure(image=self.img_Ammo_Fill_logo, text='command= Start_Ammo_Fill_exe',command= Start_Ammo_Fill_exe)
        self.button_Ammo_Fill.pack(side='left')
        self.button_Best_Bullet = ttk.Button(self.frame3)
        self.img_Best_Bullet_logo = tk.PhotoImage(file=Best_Bullet_logo)
        self.button_Best_Bullet.configure(image=self.img_Best_Bullet_logo, text='command= Start_Best_Bullet_exe',command= Start_Best_Bullet_exe)
        self.button_Best_Bullet.pack(side='left')
        self.button_Auto_BUY_logo = ttk.Button(self.frame3)
        self.img_Auto_BUY_logo = tk.PhotoImage(file=Auto_BUY_logo)
        self.button_Auto_BUY_logo.configure(image=self.img_Auto_BUY_logo, text='command= Start_Auto_BUY_exe',command= Start_Auto_BUY_exe)
        self.button_Auto_BUY_logo.pack(side='left')
        self.frame3.configure(height='200', width='200')
        self.frame3.pack(side='top')
        self.frame7 = ttk.Frame(self)
        self.Text = tk.Text(self.frame7)
        self.Text.configure(background='#222222', blockcursor='false', height='5', insertbackground='#ffd9d9')
        self.Text.configure(insertunfocussed='none', takefocus=False, width='95', wrap='word')
        _text_ = '''created Napo_II
v 0.0.3
python 3.7
https://github.com/NapoII/Napos-EFT-BOTS
'''
        self.Text.insert('0.0', _text_)
        self.Text.pack(side='top')
        self.frame7.configure(height='200', width='200')
        self.frame7.pack(side='top')


if __name__ == '__main__':
    root = tk.Tk()
    widget = TemplateWidget(root)
    widget.pack(expand=True, fill='both')
    root.mainloop()

