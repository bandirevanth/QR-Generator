# Encoding QR Code
import qrcode
import cv2

user_inp = input("Enter Website URL: ")
img = qrcode.make(user_inp)
img.save("QR-code.jpg")

# Decoding QR Code
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("QR-code.jpg"))
print("Decoded Text: ", val)
