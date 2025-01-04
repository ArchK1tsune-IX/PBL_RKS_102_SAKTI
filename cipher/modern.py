from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def aes_encrypt(text, key, aes_type):
    key = key.ljust(32 if aes_type == 256 else 16, ' ')[:32 if aes_type == 256 else 16]  # Pad or truncate key
    cipher = AES.new(key.encode(), AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(iv + ciphertext).decode()

def aes_decrypt(ciphertext, key, aes_type):
    key = key.ljust(32 if aes_type == 256 else 16, ' ')[:32 if aes_type == 256 else 16]  # Pad or truncate key
    try:
        raw = base64.b64decode(ciphertext)
        iv = raw[:16]
        cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(raw[16:]), AES.block_size).decode()
        return plaintext
    except ValueError:
        raise ValueError("Data tidak valid untuk dekripsi: mungkin data tidak sesuai padding atau rusak.")
