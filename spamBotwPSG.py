import PySimpleGUI as sg
import pyautogui
from tkinter import ttk

sg.theme('Dark blue 3')

layout = [ [sg.Text('Enter the delay time for the script')],
           [sg.InputText('', key='-TIME-')],
           [sg.Text('Enter your screen coordinates, where the bot will insert the commands(First x, second y)')], 
           [sg.InputText('', key='-COORDINATESX-')], 
           [sg.InputText('', key='-COORDINATESY-')],
           [sg.Text('Enter what you want to spam')],
           [sg.InputText('', key='-TEXT-')],
           [sg.Submit(), sg.Cancel()] ]

window = sg.Window('Configurations', layout)
event, values = window.read()
window.close()

class Cordinates:
    def wr_cor(self):
        pyautogui.click(self.corx, self.cory)
cor = Cordinates()
cor.corx = int(values['-COORDINATESX-'])
cor.cory = int(values['-COORDINATESY-'])

cor.wr_cor()

while True:
    pyautogui.write(values['-TEXT-'])
    #The delay is given in seconds
    #If you don't want delay just put 0
    pyautogui.press('enter', interval= int(values['-TIME-']))
