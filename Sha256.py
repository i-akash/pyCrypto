from Crypto.Hash import SHA256

def check_password(input_pass,passwdhash):
    if SHA256.new(input_pass).hexdigest()==passwdhash:
        return True
    return False

h=SHA256.new()
h.update("akash")
print(h.hexdigest())
