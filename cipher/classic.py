def caesar_encryption(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decryption(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def vigenere_encryption(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decryption(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def transposition_encrypt(text, key):
    key = int(key)
    rows = [text[i:i + key] for i in range(0, len(text), key)]
    ciphertext = "".join(["".join(row[i] for row in rows if i < len(row)) for i in range(key)])
    return ciphertext

def transposition_decrypt(text, key):
    key = int(key)
    num_cols = key
    num_rows = len(text) // key
    num_extra = len(text) % key

    grid = [''] * num_cols
    col_index = 0
    row_index = 0

    for char in text:
        grid[col_index] += char
        col_index += 1
        if col_index >= num_cols or (col_index == num_extra and row_index >= num_rows):
            col_index = 0
            row_index += 1

    plaintext = ''.join(grid)
    return plaintext

# Caesar Cipher
def caesar_encrypt_file(input_file, output_file, shift):
    with open(input_file, "rb") as f:
        data = f.read()
    encrypted_data = bytes((byte + shift) % 256 for byte in data)
    with open(output_file, "wb") as f:
        f.write(encrypted_data)

def caesar_decrypt_file(input_file, output_file, shift):
    with open(input_file, "rb") as f:
        data = f.read()
    decrypted_data = bytes((byte - shift) % 256 for byte in data)
    with open(output_file, "wb") as f:
        f.write(decrypted_data)

# Vigenère Cipher
def vigenere_encrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as f:
        data = f.read()
    key_bytes = key.encode()
    key_length = len(key_bytes)
    encrypted_data = bytes((byte + key_bytes[i % key_length]) % 256 for i, byte in enumerate(data))
    with open(output_file, "wb") as f:
        f.write(encrypted_data)

def vigenere_decrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as f:
        data = f.read()
    key_bytes = key.encode()
    key_length = len(key_bytes)
    decrypted_data = bytes((byte - key_bytes[i % key_length]) % 256 for i, byte in enumerate(data))
    with open(output_file, "wb") as f:
        f.write(decrypted_data)

# Transposition Cipher
def transposition_encrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as f:
        data = f.read()
    
    n = len(data)
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    encrypted_data = bytearray(n)
    
    for i in range(n):
        encrypted_data[key_order[i % len(key)] + (i // len(key)) * len(key)] = data[i]
    
    with open(output_file, "wb") as f:
        f.write(encrypted_data)

def transposition_decrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as f:
        data = f.read()
    
    n = len(data)
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    reverse_key_order = [0] * len(key)
    for i, k in enumerate(key_order):
        reverse_key_order[k] = i
    
    decrypted_data = bytearray(n)
    for i in range(n):
        decrypted_data[i] = data[reverse_key_order[i % len(key)] + (i // len(key)) * len(key)]
    
    with open(output_file, "wb") as f:
        f.write(decrypted_data)