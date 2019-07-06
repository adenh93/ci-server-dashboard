from cryptography.fernet import Fernet
from ..config import FERNET_KEY


__cipher = Fernet(FERNET_KEY)


def decrypt_key(to_decode: bytes):
    to_plain = __cipher.decrypt(to_decode)
    decoded = to_plain.decode('utf-8')
    return decoded


def encrypt_key(to_encode: bytes):
    to_bytes = bytes(to_encode, 'utf-8')
    return __cipher.encrypt(to_bytes)
