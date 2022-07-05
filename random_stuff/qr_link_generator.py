import qrcode
#from PIL import Image
# Create The variable to store the information
data = "https://www.google.com"
#data = Image.open("image.png") 
# Encode The Link
img = qrcode.make(data)
print(type(img))
# Save the QR Code
img.save("test1.jpg")