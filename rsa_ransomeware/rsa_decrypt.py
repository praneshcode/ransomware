from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

PRIVATE_RSA_KEY = '''-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAhRwa1M2VM1Evs2/DutWeJ4HA+KnFyLg9If+8YU122yJM+R/P
VAaHMK/+PyhQpTtdFElJfTeP64Fti022j1rzpovLyd4OyRLYVniQ2ENHhfzFibjN
BnPqegBrbtd3g5jNZwjQ9+HsTz6lHb5tLv7iZuUmLTJ8IQw5eNzSkL2LFqkBAvJl
aJUg8zBP5ba5odQA053za9oH2nkICPUfJeBKuDS/7/QJiLFxpWsRwglimPA5Ffu1
hwqd7tlPuDYj8IN+fozuYsRGOxqlUD8aLq9OTiX0r4LmoVxxW3aKySCrtaoqzfuz
rtZ336f5X2tATmWKBkm33gbCYUEeAyXAYfvgPwIDAQABAoIBAA4tWk2RteiY0Y1O
2UMkLxZDHiP9+mhbTdDktZI213LAhP/rBkCLT3PSktr0NslaeMVJMaVqDmSazOmP
izhai2U7h3wxL/703bYxXNqufnGED3Vl3u8R19v1q9D1lwTyTeeW9fbTiRaUSVl7
0jzf/d96sZBny6ETdb2XO2rEyAnPf/i8PZQywP83H7Hswb/Z6KYYCyEYrvNUgdKm
2Uk0Q4n0s2vClRUPk2kH5SI9QhJLGaPPk2AjlUSoSvkGCHZD7/LF1IBYyaoeBzIc
hnum914kbTB2OAbaXiidYR6+BdHPUjKGg9wovoT27rNzO6l14J5/LeRf6p26YwKq
KBRrJDkCgYEAthFFYbiIWtkTgyzjffcXZ3qMIa5yMlB56pluXb27VyLeBXVOeKch
PlEMSo+LQPzKECDrjamgIEJAgb6lgjC4p08PLjTGM+9ZCyieOLcFjdNKsZajbRNa
tF9XnKSdCYXBCFTMIiVpc5ln32lPB1EQUHERLUgz+SQ3jzhGl7RiYzkCgYEAuyl2
pmf9Lf39hNe2sXn1dUDQZP+a+FZb9Yh9aWPhzvFXoandulAY0sWOtn4oa/3lEE8A
YOSvcad6e0XIQCIH6++hFV0nCAMQlVCMzbrGU8z/m4BFLQwc2mSbg42zL90wvjVo
eXiuAtYfmEmr24Pvoy6S8BtSkcYeEBI3rAcyBzcCgYBfa/XdHYX5d0QOv/wLDPGr
PkMrc+5OCHedSQTbBJGnPZL3cV/LRGzb6EZ03X6ydMrCYT6TZI+T2KVOWskLztU4
eusN4ILwvUUB4CvstZ+nkVHYeYb1p+smFcIpSu0zDHL7FtZWHx2BhKk4Ik1VHFtc
jaXfAbSboyurWGdHIzddoQKBgBWXxgmSy8HnoL0XygsVv/zkGmbcmnt2MyvTsGxd
Sqr+axbKqzsYjJScmEdzrKQw6aGFC80h9R/Oq7HXLjA//Nv6jIITejJRcDNZ1LTT
jJgUeZTuKoz07ctAejSmP3sRMNNxA/mns6O+Im0Gat5rjVUtRWSQMmmBCuzdvTCK
r/nnAoGAXgUv6mxf4xlnHD1nWa5MwKKVErwizqseGqIM+lqtgoK8/DQEtibtENqG
SQ09Epn8HAfDsBKW7Xi4O1KJc9xS0F6ZkxxAJgN5LSOpG6WegjKoGYfWQNkNqivU
Ra97MeC0xV/X5vyACZJhxYJPHFiiK1zyfiIFQ00AZA2MsIMR30o=
-----END RSA PRIVATE KEY----- 
'''

with open(input('Path: '), 'rb') as f:
    data = f.read()

private_key = RSA.import_key(PRIVATE_RSA_KEY)
rsa_decryptor = PKCS1_OAEP.new(private_key)
decrypted_key = rsa_decryptor.decrypt(data)
print(f'Decrypted Key: {decrypted_key.decode()}')
