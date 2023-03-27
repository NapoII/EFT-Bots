import pyautogui
import pyperclip
import platform

def type(text: str):    
    pyperclip.copy(text)
    if platform.system() == "Darwin":
        pyautogui.hotkey("command", "v")
    else:
        pyautogui.hotkey("ctrl", "v")


type("Peter")