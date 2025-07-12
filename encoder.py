# encoder.py
import cv2
import numpy as np
from utils import text_to_bits

def encode_message_in_image(image_path, message_part, output_path):
    img = cv2.imread(image_path)
    message_bits = text_to_bits(message_part) + '1111111111111110'  # End marker

    flat = img.flatten()
    for i in range(len(message_bits)):
        flat[i] = (flat[i] & 0xFE) | int(message_bits[i])  # Set LSB

    encoded_img = flat.reshape(img.shape)
    cv2.imwrite(output_path, encoded_img)
