from email.mime import image
from PIL import Image

img = Image.new("RGB",(200,200))
for x in range(100):
    img.putpixel((x,100),255)
img.save("run.bmp")