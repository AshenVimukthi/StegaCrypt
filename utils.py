# utils.py
import numpy as np

def split_message(message, key):
    np.random.seed(sum(ord(c) for c in key))
    proportions = np.random.dirichlet(np.ones(4))
    message_parts = []
    start = 0
    for p in proportions:
        length = int(p * len(message))
        message_parts.append(message[start:start+length])
        start += length
    while len(message_parts) < 4:
        message_parts.append('')
    return message_parts

def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)

def bits_to_text(bits):
    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
    return ''.join(chars)
