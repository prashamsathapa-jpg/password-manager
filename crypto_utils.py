import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
def derive_key(master_password:str,salt:bytes) -> bytes:
    """Turns the master password into a usable encryption key."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000
)
    key=base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key
def encrypt_password(password: str, key: bytes) -> bytes:
    f= Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(token: bytes, key: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(token).decode()
