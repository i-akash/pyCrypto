from Crypto.Cipher import DES3
from Crypto import Random


def Encrypt(file_in,file_out,key,feed,chunk_size):
    des3=DES3.new(key,DES3.MODE_CFB,feed)

    with open(file_in,'r') as fin:
        with open(file_out,'w') as fout:
            while True:
                text=fin.read(chunk_size)
                if len(text)==0:
                    break
                if len(text)%16!=0:
                    text+=' '*(16-len(text)%16)

                etext=des3.encrypt(text)
                fout.write(etext)


def Decrypt(file_enc,file_dec,key,feed,chunk_size):
    des3=DES3.new(key,DES3.MODE_CFB,feed)

    with open(file_enc,'r') as enc:
        with open(file_dec,'w') as dec:
            while True:
                etext=enc.read(chunk_size)

                if len(etext)==0:
                    break
                if len(etext)%16!=0:
                    etext+=''*(16-len(etext)%16)
                dtext=des3.decrypt(etext)
                dec.write(dtext)



#key must be 16 or 24 in des3
key='0123456789101112'
feed=Random.get_random_bytes(8)
file_in='text.txt'
file_enc='enc.txt'
file_dec='dec.txt'

chunk_size=8192

with open(file_in,'r') as fin:
    print("text : %s"%fin.read())
Encrypt(file_in,file_enc,key,feed,chunk_size)
with open(file_enc,'r') as enc:
    print("enc : %s"%enc.read())
Decrypt(file_enc,file_dec,key,feed,chunk_size)
with open(file_dec,'r') as dec:
    print("dec : %s"%dec.read())
