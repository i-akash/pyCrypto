from Crypto.Cipher import DES

text="i_secInc"
key='01234567'
des=DES.new(key,DES.MODE_ECB)
cipherText=des.encrypt(text)
print(cipherText)
print(des.decrypt(cipherText))
