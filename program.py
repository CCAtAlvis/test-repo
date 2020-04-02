from PIL import Image
import sys

size = (240,240)
image = 'input.jpeg'

im = Image.open(image)
im.thumbnail(size)
im.save('output.jpeg')
