from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
fernet = Fernet(key)
print(fernet)
with open('people.csv', 'rb') as file,open('hashPeople.csv', 'wb') as encrypted_file:
    original = file.readlines()
    for i in original:
        encrypted = fernet.encrypt(i)
        encrypted_file.write(encrypted)
        encrypted_file.write('\n'.encode('utf-8'))
