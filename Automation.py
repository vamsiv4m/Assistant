from os import startfile
import calendar
import time
import os
def notepad(text):
    filename=f"myfile{calendar.timegm(time.gmtime())}.txt"
    with open(filename,"w") as file:
        file.write(text)
    path_1="C:\\Users\\ASUS\\Desktop\\Virtual Sketch Assistant Project\\"+filename
    path_2="C:\\Users\\ASUS\\Desktop\\Virtual Sketch Assistant Project\\notepad\\"+filename
    os.rename(path_1,path_2)
    os.startfile(path_2)

def close_notepad():
    os.system("TASKKILL /F /im Notepad.exe")

def whatsapp(text):
    startfile("C:\\Users\\ASUS\\AppData\\Local\\WhatsApp\\WhatsApp.exe")


def visual_studio():
    startfile("C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

def close_vscode():
    os.system("TASKKILL /F /im C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")