from msilib import Directory
import requests
import cv2

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

dir = "C://Users//space//Desktop"


half_img_save_from_api("https://cdn.tarkov-market.app/images/items/7.62x54r_7n1_sniper_cartridge_sm.png", dir, "7.5 20c_20x70mm")


