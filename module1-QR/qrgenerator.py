import qrcode
with open("hashPeople.csv","rb") as hashPeople:
    data  = hashPeople.readlines()

for i in data:
    img = qrcode.make(i.decode('utf-8'))
    img.save(i.decode('utf-8')+".jpg")







