import os
import binascii
from Crypto.Cipher import AES

ext = 'locked'

path = os.environ['USERPROFILE']
lst = os.walk(path)
files = []
for i in lst:
    local_dir = i[0]
    for j in i[2]:
        if j not in ['decryptor.exe']:
            str = f'{local_dir}\\{j}'
            files.append(str)


def decrypt(key, files, IV):
    cipher = AES.new(key, AES.MODE_CBC, IV)
    for file in files:
        try:
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'wb+') as f:
                decrypted_data = cipher.decrypt(data)
                f.write(decrypted_data.rstrip(b'0'))
            os.rename(file, file[:-len(ext) - 1])
            print(f'{file} decrypted')
        except:
            pass
            # print(f'{file} not decrypted')


key = binascii.unhexlify(input("Enter Decryption Key: ").encode())
IV = b'This is an IV456'

decrypt(key, files, IV)
