import cv2
import tkinter as tk
from tkinter import filedialog

def sketch():
    filetypes = (
        ('jpg type', '*.jpg'), 
        ('png type', '*.png*')
    )
    root=tk.Tk()
    root.withdraw()
    filepath=filedialog.askopenfilename(filetypes=filetypes,initialdir="/Pictures")
    img = cv2.imread(filepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.ADAPTIVE_THRESH_MEAN_C, 7, 7)
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cv2.imshow("edges", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

