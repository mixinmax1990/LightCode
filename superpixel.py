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
        columncount = 1
        self.image = px
        superpixelOBJ = []
        superpixelRow = []
        superX = 1
        superY = 1
        pixelcount = 0
    
        i = 0
        while i < square:

            j = 0
            superX = 1
            while j < square:
                x = j + startX
                y = i + startY
                pixelcount = pixelcount + 1
                print(pixelcount)
                columncount = columncount + 1
                # store Column info

        
                superpixelRow.append([superX])
                superpixelOBJ[superX].append(px[x,y])
                
                
                if(columncount == spSize):
                    superX = superX + 1
                    rowcount = 0
                
                j = j + 1
 
            if(rowcount == spSize):
                
                superpixelOBJ.append([superY])
                superpixelOBJ[superY].append(superpixelRow)
        
                superY = superY + 1
                superpixelRow = []
                rowcount = 1
            rowcount = rowcount + 1
            i = i + 1

        print(np.matrix(superpixelOBJ))


    #def identPeriPixels()