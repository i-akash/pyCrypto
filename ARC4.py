from Crypto.Cipher import ARC4

text='i_secInc'
key='01234567'

arc=ARC4.new(key)
arcDec=arc
cipherText=arc.encrypt(text)
print(cipherText)
print(arcDec.decrypt(cipherText))
