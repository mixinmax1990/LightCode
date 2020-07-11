import json


def runit():
    x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

    #y = json.loads(x)
    #print(json.dumps(x["cars"][0]["mpg"]))

#runit()
prevR = 0
prevG = 0
prevB = 0
isPrev = False
trendChangeR = 0
trendChangeG = 0
trendChangeB = 0

barrier = 10

def setTrend(R, G, B):
  global trendChangeR, trendChangeG, trendChangeB
  trendChangeR = R + trendChangeR
  trendChangeG = G + trendChangeG
  trendChangeB = B + trendChangeB

  #print("R-Shift : " + str(trendChangeR) + " ; G-Shift : " + str(trendChangeG) + " ; B-Shift : " + str(trendChangeB))

  if(trendChangeB > barrier or trendChangeG > barrier or trendChangeR > barrier):
    #print("R-Shift : " + str(trendChangeR) + " ; G-Shift : " + str(trendChangeG) + " ; B-Shift : " + str(trendChangeB))
    trendChangeR = 0
    trendChangeG = 0
    trendChangeB = 0

    


def setPrevRGB(R, G, B):
    global prevR, prevG, prevB, isPrev
    prevR = R
    prevG = G
    prevB = B
    isPrev = True

    


def rbgChange(R, G, B):
    global prevR, prevG, prevB, isPrev
    if(isPrev == True):

        rshift = prevR - R
        gshift = prevG - G
        bshift = prevB - B

        setTrend(rshift, gshift, bshift)

    setPrevRGB(R, G, B)

