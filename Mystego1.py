import cv2
import os
import string

# Read the image
img = cv2.imread("Jaan.jpg")  # Replace with the correct image path

# Get the dimensions of the image
height, width, _ = img.shape

# Inputs from user
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Dictionaries to map characters to ASCII and back
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Encoding the message
n, m, z = 0, 0, 0
for i in range(len(msg)):
    if n >= height or m >= width:
        break
    img[n, m, z] = d[msg[i]]
    n = n + 1 if z == 2 else n
    m = (m + 1) % width if z == 2 else m
    z = (z + 1) % 3

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
cv2.imshow("Encrypted Image", img)
cv2.waitKey(0)  # Wait for a key press to close the image

# Decryption
message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        if n >= height or m >= width:
            break
        message += c[img[n, m, z]]
        n = n + 1 if z == 2 else n
        m = (m + 1) % width if z == 2 else m
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")