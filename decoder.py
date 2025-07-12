# decoder.py
import cv2
from utils import bits_to_text

def decode_message_from_image(image_path):
    img = cv2.imread(image_path)
    flat = img.flatten()
    
    bits = ''
    for i in range(len(flat)):
        bits += str(flat[i] & 1)
        if bits[-16:] == '1111111111111110':
            break

    bits = bits[:-16]
    return bits_to_text(bits)
