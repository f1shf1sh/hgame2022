from Cryptodome.Cipher import Blowfish
import binascii

cipher = b'546F4EBFB4ED937B82D2A07E13D3EFDD2209AE0F594EDF61B933782C1C07E532'
key = b'LET_U_D'
flag = ''

cipher = binascii.a2b_hex(cipher)
blowfish = Blowfish.new(key, Blowfish.MODE_ECB)
plain = blowfish.decrypt(cipher)

for i in range(8):
    text = plain[i*4:i*4+4]
    text = text[::-1]
    flag += text.decode('utf-8')

print(flag)
