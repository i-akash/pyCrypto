from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto import Random

text="i_secInc"

key=RSA.generate(1024,Random.new().read)
hashed=SHA256.new(text).hexdigest()
hstext=key.sign(hashed,'')

print(hashed)
print("="*80)
print(hstext)
