import numpy as np
from PIL import Image

im = Image.open("picture.jpg")
pix = np.array(im)
print(len(pix),len(pix[1]))
print(pix[0])

def convertBlackWHite(image_file):
    return image_file.convert('1')
# convert image to black and white

def save(image_file,filename):
    return image_file.save(filename,'JPEG')

def open(filename):
    return Image.open(filename)

image=open("black1")
# image=convertBlackWHite(image)
# save(image,"black1")
x=np.array(image)
print(len(x),len(x[1]))
print(x[0])
