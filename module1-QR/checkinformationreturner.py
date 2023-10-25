from tkinter import messagebox
from cryptography.fernet import Fernet
with open('filekey.key', 'rb') as filekey:
    fernet=Fernet(filekey.read())
with open('hashPeople.csv', 'rb') as enc_file,open('revealHashPeople.csv', 'wb') as dec_file:
    qr=enc_file.readlines()
    for i in qr:
        dec_file.write(fernet.decrypt(i))
        

def decoding(hash):
    with open('filekey.key','rb') as filekey:
        fernet = Fernet(filekey.read())
    a = fernet.decrypt(hash).decode('UTF-8').split(',')
    messagebox.showinfo("Info","    VERIFIED PERSON        \nName : %s\nAge  : %d" % (a[0],int(a[1])))
   
