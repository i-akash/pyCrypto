from Crypto.Cipher import DES3
from Crypto import Random
import os

text="i_secInc"
key='0123456789101112'
iv=Random.get_random_bytes(8)
des3 = DES3.new(key, DES3.MODE_CFB, iv)
