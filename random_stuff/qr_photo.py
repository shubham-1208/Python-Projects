import qrcode
from PIL import Image
# Create The variable to store the information
data = "C:/Users/shubh/Desktop/study/projects"
data = Image.open("image.png") 
# Encode The Link
img = qrcode.make(data)
print(type(img))
# Save the QR Code
img.save("testimage.jpg")