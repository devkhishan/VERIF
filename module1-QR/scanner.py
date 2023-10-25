import cv2
from pyzbar.pyzbar import decode 
import time
from checkinformationreturner import decoding
from tkinter import messagebox
import tkinter
root=tkinter.Tk()
root.withdraw()
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
with open("hashPeople.csv","rb") as hashPeople:
    data  = [i.decode('utf-8') for i in hashPeople.readlines()]

camera = True
while camera == True:
    success,frame = cap.read()
    for code in decode(frame):
        if code.data.decode('utf-8') in data:
            decoding(code.data)
            time.sleep(3)
            camera=False
        elif code.data.decode('utf-8') not in data:
            messagebox.showerror("Error","Unverified Person")
            time.sleep(3) 
            camera=False
    cv2.imshow('Testing-code-scan',frame)
    cv2.waitKey(1)
    