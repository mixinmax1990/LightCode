from __future__ import print_function
import os, sys
import trendsetter
import superpixel
import PIL 
from PIL import Image, ImageDraw, ImageFont
import time


t0 = time.time()
img = Image.open("html/images/sunset.jpg", "r")
width, height = img.size
square = 50
startx, starty = 0, 0
nested = []
px = img.load()


superpixelL1 = superpixel.Superpixel_L1()
superpixelL1.identCenterPixelPos(px, square, startx, starty)
t1 = time.time()
total = t1-t0
print(total)
sys.exit()
#get store pixel values in list
#sys.exit()
i = 0
while i < square:
    row_list = []
    j = 0
    while j < square:
        x = startx + j
        y = starty + i
        row_list.append(px[x,y])
        j = j + 1
        R,G,B = px[x,y]

        trendsetter.rbgChange(R,G,B)

    nested.append(row_list)
    i = i + 1
    



# ---------------------------- Draw new Image --------------------------

def writePixelData(img, data, x, y, bright):
    #print(x)
    if(bright > 50):
        color = (0,0,0)
    else:
        color = (255,255,255)

    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
    d.text((x, y), data, font=fnt, fill=color)
    #print("Prints - X = " + str(x) + " ; Y = " + str(y))


img_size = square * 50
next_x = 0
next_y = 0
movelist_x = 0
movelist_y = 0
count = 0
newimg = Image.new('RGB', (img_size, img_size), color = "red")
for y in range(img_size): 

    print(y)
    # Verical Loop
    next_y = next_y + 1
    #print(next_x)

    for x in range(img_size):

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
        #img.putpixel((x,y), new_green)
        elif(next_y == square):
            if(next_x == 15):
                count = count + 1
                R,G,B = nested[movelist_y][movelist_x]
                brightness = ((R + G + B) / float(3))/2.55
                #print("count = " + str(count) + " ; R = " + str(R) + " - G = " + str(G) + " - B " + str(B) + " - Bright = " + str(bright))
                writePixelData(newimg, str(count), x, y - 30, brightness)

            newimg.putpixel((x, y), (0,0,0))
        else: 
            newimg.putpixel((x, y), nested[movelist_y][movelist_x])
    
    if(next_y == square):
        # read the next pixel data in the list
        movelist_y = movelist_y + 1
        next_y = 0

print("Done!!") 
newimg.save("test2.png")


