from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes="bcrypt", deprecated='auto')

class Hash():
    
    def bcrypt(password: str):
        hash_pass = pwd_cxt.hash(password)
        return hash_pass
    
    def verify_pass(plain_pass, hash_pass):
        return pwd_cxt.verify(plain_pass, hash_pass)
    
    
    
    
 