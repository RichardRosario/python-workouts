import pytesseract
from PIL import Image
import inspect

# print(dir(Image))

image = Image.open("D:\python-workouts\workouts\images\R-logo.png")
# Image._show(image)
print(dir(pytesseract))

help(Image.Image.resize)
# src = inspect.getsource(pytesseract.image_to_string)
# print(src)
