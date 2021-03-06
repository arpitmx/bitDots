
import sys
from PIL import Image

# pass the image as command line argument
#image_path = sys.argv[1]
img = Image.open("sample5.png")

# resize the image
width, height = img.size
aspect_ratio = height/width
new_width = 80
new_height = aspect_ratio * new_width * 0.4
img = img.resize((new_width, int(new_height)))
# new size of image
# print(img.size)

# converts my imagu to greyscale format
img = img.convert('L')
pixels = img.getdata()

chars  = "W/w/l/i/./,/ ".split("/")
#print("Total chars ", chars[int(4//3.69)], len(chars))

dec = 255 / (len(chars)-1)
new_pixels = [chars[int(pixel // dec )] for pixel in pixels]
new_pixels = ''.join(new_pixels)

# split string of chars into multiple strings of length equal to new width and create a list
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)

# write to a text file.
with open("output.txt", "w") as f:
 f.write(ascii_image)

