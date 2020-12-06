import pyautogui
from tkinter import ttk
import time

class Cordinates:
    def wr_cor(self):
        pyautogui.click(self.corx, self.cory)
cor = Cordinates()
cor.corx = 1243 
cor.cory = 647

cor.wr_cor()

while True:
        pyautogui.write('t!tg train')
        pyautogui.press('enter', interval='5')
		
