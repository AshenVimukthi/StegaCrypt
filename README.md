# 🔐 StegaCrypt — Secure Multi-Image Steganography + Cryptography System

> 🚀 A hybrid Python project that hides secret messages across **four images** using a blend of cryptography, randomness, and pixel-level transformations.

---

## 📸 Overview

**StegaCrypt** is a secure message hiding system that:
- 🔐 Uses **cryptographic logic** (secret key)
- 🖼️ Applies **multi-image steganography** (LSB encoding)
- 🎲 Adds **randomness with Dirichlet distributions**
- 🧠 Requires **all 4 images + key** to recover the message

> The message is split, hidden, and protected — and only reconstructable if you know the exact key and have all encoded images.

---

## 🧰 Tech Stack

| Area | Tools |
|------|-------|
| Language | Python 3.13+ |
| Libraries | `NumPy`, `OpenCV`, `Pillow`, `Matplotlib`, `scikit-image` |
| Concepts | Steganography, Cryptography, Probability, Pixel-level LSB manipulation |

---

## 📂 Folder Structure

StegaCrypt/  
├── encoder.py # Encoding logic  
├── decoder.py # Decoding logic  
├── utils.py # Message splitting & helper functions  
├── main.py # Run encode/decode from terminal   
├── test_images/ # Original input images  
├── output_images/ # Encoded images with hidden data  
├── requirements.txt # Python dependencies  
└── README.md # This file  

---

## 🚀 How to Use

### 1️⃣ Encoding

```bash
python main.py
```

Then choose:

```bash
1. Encode
Enter secret message: this is a secret message
Enter key: open123
```
✅ This creates 4 encoded images in output_images/ folder.

### 2️⃣ Decoding

```bash
python main.py
```
Choose:

```bash
2. Decode
Enter key: open123

```

✅ This reconstructs and displays the original hidden message.

## 🖼️ Test Images
Use any 4 PNG images and place them inside test_images/ folder as:
```bash
image1.png
image2.png
image3.png
image4.png
```
🟡 Note: Avoid JPEG files — they use compression that can corrupt hidden data.

## 💡 Features
🔐 Key-based secure splitting and reconstruction

🖼️ Visually indistinguishable stego images

🧮 Uses Dirichlet distributions for randomness

🧠 Precision-focused image encoding at bit level

✅ Works entirely offline and locally

## 📌 Future Improvements
✅ Add error correction and checksum

🧠 Use stronger encryption (e.g., AES or RSA)

🌐 Web interface with Flask or React

🖼️ Drag-and-drop GUI

### 👨‍💻 Author
Made with ❤️ by Ashen Vimukthi
🔗 Connect on: GitHub | LinkedIn

### 📜 License
This project is licensed under the MIT License.
