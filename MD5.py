import os
from Crypto.Hash import MD5

def get_file_checksum(filename):
    h=MD5.new()
    chunk_size=8192

    with open(filename,'rb') as f:
        while True:
            chunk=f.read(chunk_size)
            if not len(chunk):
                break
            h.update(chunk)
    return h.hexdigest()
    
