from Crypto.PublicKey import RSA
from Crypto import Random

text="i_secInc"
length=1024 #128byte or 128 char
key=RSA.generate(length,Random.new().read)

publicKey=key.publickey()

etext=publicKey.encrypt(text,32)
print('decrypt'.center(80,'='))
print(etext)
print("="*80)

print('encrypt'.center(80,'='))
print(key.decrypt(etext))
print("="*80)
