from __future__ import print_function
import os, sys
import PIL 
from PIL import Image, ImageDraw, ImageFont

img = Image.open("html/images/nataliemartinez(edit).png", "r")
width, height = img.size
square = 50
startx, starty = 200, 200
nested = []

def writePixelData(img, data, x, y):
    #print(x)
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
    d.text((x, y), data, font=fnt, fill=(0,0,0))

#gray = img.convert('1')
#bw = gray.point(lambda x: 0 if x<128 else 255, '1')

px = img.load()

#get store pixel values in list
i = 0
while i < square:
    row_list = []
    j = 0
    while j < square:
        x = startx + j
        y = starty + i
        row_list.append(px[x,y])
        j = j + 1

    nested.append(row_list)
    i = i + 1
count = 0

img_size = square * 50
next_x = 0
next_y = 0
movelist_x = 0
movelist_y = 0
newimg = Image.new('RGB', (img_size, img_size), color = "red")
for y in range(img_size):
    
# Verical Loop
    next_y = next_y + 1
    #print(next_x)
    count = 0

    for x in range(img_size):
        if(count < 10000):
            print(x)
            count = count + 1
        # Horizontal Loop
        next_x = next_x + 1
        if(next_x == square):
            #print("inside")
            #read the next pixel data in the list
            newimg.putpixel((x, y), (0,0,0))
            if(movelist_x == (square - 1)):
                movelist_x = 0
            else:
                movelist_x = movelist_x + 1
            next_x = 0
        #   img.putpixel((x,y), new_green)
        elif(next_y == square):
            if(next_x == 22):
                #print("count", count, " x = ", x)
                R,G,B,A = nested[movelist_x][movelist_y]
                brightness = (sum([R,G,B])/3)/2.55
                writePixelData(newimg, str(round(brightness, 2)), y, x + 10)

            newimg.putpixel((x, y), (0,0,0))
        else: 
            newimg.putpixel((x, y), nested[movelist_x][movelist_y])
    
    if(next_y == square):
        # read the next pixel data in the list
        movelist_y = movelist_y + 1
        next_y = 0

print("Done!!") 
newimg.save("test.png")


