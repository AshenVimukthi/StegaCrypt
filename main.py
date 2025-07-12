# main.py
import os
from encoder import encode_message_in_image
from decoder import decode_message_from_image
from utils import split_message

def encode_full(message, key):
    parts = split_message(message, key)
    for i in range(4):
        encode_message_in_image(
            f'test_images/image{i+1}.png',
            parts[i],
            f'output_images/encoded{i+1}.png'
        )
    print("✅ Encoding complete. Check output_images folder.")

def decode_full(key):
    decoded_parts = []
    for i in range(4):
        part = decode_message_from_image(f'output_images/encoded{i+1}.png')
        decoded_parts.append(part)
    message = ''.join(decoded_parts)
    print(f"🔓 Decoded Message: {message}")

# Example Usage
if __name__ == "__main__":
    option = input("1. Encode\n2. Decode\nChoose: ")
    if option == '1':
        msg = input("Enter secret message: ")
        key = input("Enter key: ")
        encode_full(msg, key)
    else:
        key = input("Enter key: ")
        decode_full(key)
