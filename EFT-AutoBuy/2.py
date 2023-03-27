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

list_dir = "E:\\Pr0grame\\My_ Pyhton\\work_in_progress\\EFT-Bots\\Auto_BUY\\ListeAutoRotation.txt"

def Zeit_pause(seconds):
    start_time = time.time()
    while True:                             # Zeit schelife startet
        current_time = time.time()
        elapsed_time = current_time - start_time        # berechung rest Zeit
        if elapsed_time > seconds:
            break

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

while True:
    Zeit_pause(1)
    Len_Line = Len_Line_in_Text(list_dir)+1
    x = -1
    while True:
        Len_Line = Len_Line -1
        x = x + 1
        if Len_Line == 0:
            break

        Raw_Item = Next_Item_from_list(list_dir, x)

        Item = Raw_Item[0]
        Preis_max = Raw_Item[1]
        Seller = Raw_Item[2]

        print (Item)



