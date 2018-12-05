from Crypto import Random
from Crypto.Cipher import DES

rs=Random.get_random_bytes(8)

key='01234567'
text='i_secInc'

desFeed=DES.new(key,DES.MODE_CFB,rs)#public
desDec=DES.new(key,DES.MODE_CFB,rs)#private
cipherText=desFeed.encrypt(text)
print(cipherText)
print(desDec.decrypt(cipherText))
