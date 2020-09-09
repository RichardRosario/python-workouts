# From the image you can see there are two parameters which are being varied for each sub-image. First, the rows are changed by color channel, where the top is the red channel, the middle is the green channel, and the bottom is the blue channel. Wait, why don't the colors look more red, green, and blue, in that order? Because the change you to be making is the ratio, or intensity, or that channel, in relationship to the other channels. We're going to use three different intensities, 0.1 (reduce the channel a lot), 0.5 (reduce the channel in half), and 0.9 (reduce the channel only a little bit).

# For instance, a pixel represented as (200, 100, 50) is a sort of burnt orange color. So the top row of changes would create three alternative pixels, varying the first channel(red). one at(20, 100, 50), one at(100, 100, 50), and one at(180, 100, 50). The next row would vary the second channel(blue), and would create pixels of color values(200, 10, 50), (200, 50, 50) and (200, 90, 50).

import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFont
from PIL import ImageDraw

# read image and convert to RGB
image = Image.open("readonly/msi_recruitment.gif")
image = image.convert('RGB')

# set the image size
width, height = image.size
# declare newImg variable with PIL.Image,new()
newImg = PIL.Image.new(image.mode, (width, (height + 100)))
newImg.paste(image, (0, 0))

# creating a drawText function with color and intensity, emage as parameters


def drawText(color, intensity, img):
    text = "channel {} intensity {}".format(color, intensity)
    font = ImageFont.truetype(r'readonly/fanwood-webfont.ttf', 75)
    Draw = ImageDraw.Draw(img)
    Draw.text((10, 470), text, fill="white", font=font)


# defining the intensity function to set intensity of color
def setIntensity(col_intense, img, color):
    newImage = PIL.Image.new(img.mode, (newImg.width, newImg.height))

    for row in range(height):
        for col in range(width):
            p = img.getpixel((col, row))
            if color == 0:
                newImage.putpixel(
                    (col, row), (int(p[0]*col_intense), p[1], p[2]))
            elif color == 1:
                newImage.putpixel(
                    (col, row), (p[0], int(p[1]*col_intense), p[2]))
            elif color == 2:
                newImage.putpixel(
                    (col, row), (p[0], p[1], int(p[2]*col_intense)))
    return newImage


# use three different intensities starting from 0.1
intensity = [0.1, 0.5, 0.9]
colors = [0, 1, 2]  # "red","green","blue" channel respectively

# create a list of new images
images = []
# let's loop through the colors and intensity using for loop
for color in colors:
    for i in intensity:
        images.append(setIntensity(i, newImg, color))
        drawText(color, i, images[-1])

# output the images to the contact_sheet
contact_sheet = PIL.Image.new(newImg.mode, (newImg.width*3, (newImg.height)*3))
# set initial value of x,y for image
x = 0
y = 0

for img in images:
    contact_sheet.paste(img, (x, y))
# let's update our x and y positions
    if x+newImg.width == contact_sheet.width:
        x = 0
        y = y+newImg.height
    else:
        x = x+newImg.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize(
    (int(contact_sheet.width/2), int(contact_sheet.height/2)))
display(contact_sheet)
