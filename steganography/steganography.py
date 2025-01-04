from PIL import Image
from cipher.modern import aes_encrypt, aes_decrypt

def embed_text(image_path, text, output_path):
    img = Image.open(image_path)
    binary_text = ''.join(format(ord(char), '08b') for char in text) + '00000000'  # EOF marker
    pixels = list(img.getdata())

    if len(binary_text) > len(pixels) * 3:
        raise ValueError("Text too long to embed in this image.")

    new_pixels = []
    binary_index = 0

    for pixel in pixels:
        r, g, b = pixel[:3]
        if binary_index < len(binary_text):
            r = (r & ~1) | int(binary_text[binary_index])
            binary_index += 1
        if binary_index < len(binary_text):
            g = (g & ~1) | int(binary_text[binary_index])
            binary_index += 1
        if binary_index < len(binary_text):
            b = (b & ~1) | int(binary_text[binary_index])
            binary_index += 1
        
        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(output_path)
    return output_path

def extract_text(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    binary_text = ""

    for pixel in pixels:
        r, g, b = pixel[:3]
        binary_text += str(r & 1)
        binary_text += str(g & 1)
        binary_text += str(b & 1)

    eof_index = binary_text.find("00000000")
    if eof_index != -1:
        binary_text = binary_text[:eof_index]

    chars = [chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8)]
    extracted_text = ''.join(chars)

    return extracted_text

def embed_and_encrypt(image_path, text, key, aes_type, output_path):
    print(f"Embedding: Text={text}, Key={key}, AES Type={aes_type}")  # Debugging log
    encrypted_text = aes_encrypt(text, key, aes_type)
    return embed_text(image_path, encrypted_text, output_path)

def extract_and_decrypt(image_path, key, aes_type):
    print(f"Extracting with Key={key}, AES Type={aes_type}")  # Debugging log
    encrypted_text = extract_text(image_path)
    print(f"Extracted Encrypted Text: {encrypted_text}")  # Debugging log
    return aes_decrypt(encrypted_text, key, aes_type)
