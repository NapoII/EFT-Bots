import pathlib
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "Template.ui"


class TemplateWidget(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(TemplateWidget, self).__init__(master, **kw)
        self.Logo = ttk.Label(self)
        self.img_EFTBotLogo = tk.PhotoImage(file='EFT Bot Logo.png')
        self.Logo.configure(image=self.img_EFTBotLogo, text='label8')
        self.Logo.pack(side='top')
        self.frame3 = ttk.Frame(self)
        self.Loot_Helper = ttk.Label(self.frame3)
        self.img_Raid_LootHelper_logo = tk.PhotoImage(file='Raid_Loot-Helper_logo.png')
        self.Loot_Helper.configure(image=self.img_Raid_LootHelper_logo, text='label9')
        self.Loot_Helper.pack(side='left')
        self.AmmoFill = ttk.Label(self.frame3)
        self.img_Ammo_Fill_logo = tk.PhotoImage(file='Ammo_Fill_logo.png')
        self.AmmoFill.configure(image=self.img_Ammo_Fill_logo, text='label10')
        self.AmmoFill.pack(side='left')
        self.BestBullet = ttk.Label(self.frame3)
        self.img_Best_Bullet_logo = tk.PhotoImage(file='Best_Bullet_logo.png')
        self.BestBullet.configure(image=self.img_Best_Bullet_logo, text='label15')
        self.BestBullet.pack(side='left')
        self.Autobuy = ttk.Label(self.frame3)
        self.img_Auto_BUY_logo = tk.PhotoImage(file='Auto_BUY_logo.png')
        self.Autobuy.configure(image=self.img_Auto_BUY_logo, text='label16')
        self.Autobuy.pack(side='left')
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
