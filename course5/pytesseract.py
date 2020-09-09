import pytesseract
from PIL import Image

# print(dir(Image))

image = Image.open("D:\python-workouts\workouts\images\R-logo.png")
# Image._show(image)
print(dir(pytesseract))

help(Image.Image.resize)
