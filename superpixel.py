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
        superpixelOBJ = {}
        superpixelRow = {}
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
                
                # store Column info
                datapixel = {'pixel_no': str(pixelcount), 'rgb': str(px[x,y])}
                try:
                    superpixelRow['' + str(superX) + ''].append(datapixel)
                    #superpixelRow.insert(superX, px[x,y])
                    #print("SuperX Pixel:" + str(pixelcount) + " - belongs To Superpixel - " + str(superX))
                except KeyError:
                    superpixelRow['' + str(superX) + ''] = []
                    superpixelRow['' + str(superX) + ''].append(datapixel)
                    #print("Pixel:" + str(pixelcount) + " - belongs To Superpixel - " + str(superX))

                #superpixelRow.append([superX])
                #superpixelOBJ[superX].append(px[x,y])
            
                
                if(columncount == spSize):
                    superX = superX + 1
                    columncount = 1
                columncount = columncount + 1
                
                j = j + 1
                #print("x : " + str(x) + "-  SuperX: " + str(superX))
            #print(superpixelRow)
            with open('superpixel.json', 'w') as outfile:
                json.dump(superpixelRow, outfile)

            if(rowcount == spSize):
                #superpixelOBJ[superY] = []
                superpixelOBJ['' + str(superY)].append(superpixelRow)
                
                
        
                superY = superY + 1
                superpixelRow = []
                rowcount = 1
            rowcount = rowcount + 1
            i = i + 1

        with open('superpixel.json', 'w') as outfile:
            json.dump(superpixelOBJ, outfile)


    #def identPeriPixels()