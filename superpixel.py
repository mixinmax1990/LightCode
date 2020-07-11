import PIL 
from PIL import Image, ImageDraw, ImageFont
import json
import numpy as np


class Superpixel_L1():
    image = None
    


    def identCenterPixelPos(self, px, square, startX, startY):
        #print("trying classes")
        spSize = 3
        rowcount = 1
        columncount = 0
        self.image = px
        superpixelOBJ = []
        superpixelRow = []
        superX = 0
        superY = 0
        pixelcount = 0
    
        i = 0
        while i < square:

            j = 0
            superX = 0
            while j < square:
                x = j + startX
                y = i + startY
                pixelcount = pixelcount + 1
                #print(pixelcount)
                columncount = columncount + 1
                # store Column info

                try:
                    superpixelRow.insert(superX, px[x,y])
                    print("SuperX Pixel:" + str(pixelcount) + " - belongs To Superpixel - " + str(superX))
                except ValueError:
                    superpixelRow.append(px[x,y])
                    print("Pixel:" + str(pixelcount) + " - belongs To Superpixel - " + str(superX))

                #superpixelRow.append([superX])
                #superpixelOBJ[superX].append(px[x,y])
            
                
                if(columncount == spSize):
                    superX = superX + 1
                    columncount = 0
                
                j = j + 1
            print(superpixelRow)
 
            if(rowcount == spSize):
                
                superpixelOBJ.append([superY])
                superpixelOBJ[superY].append(superpixelRow)
        
                superY = superY + 1
                superpixelRow = []
                rowcount = 1
            rowcount = rowcount + 1
            i = i + 1

        #print(np.matrix(superpixelOBJ))


    #def identPeriPixels()