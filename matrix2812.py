import array

from ws2812 import WS2812

#my setup of a matrix for my neopixel matrix
"""
I want the matrix to be created at a set length/width.

Assuming a matrix of strip lights connected end to end, not in a parallel-style config.

length is how long each cut strip of LEDs is
height is how many strips are attached together.

"""

class matrix2812():
    
    def __init__(self, length, height):
        #My guess of how this works is I'm just taking the inputs and figuring out what to do with them.
        self.strip_size = length
        self.num_strips = height
        
    def nameLED(self, x, y):
        #x is the number on each strip
        #y is which strip we're talking about
        #is the RBG color to light.
        if y % 2 == 0:
            #on an even numbered strip
            #print(x, ",", y, "is on an even strip")
            LEDnum = y*(self.strip_size+1)+x
        elif y % 2 == 1:
            #on an odd numbered strip
            #print(x, ",", y, "is on an odd strip")
            LEDnum = (y+1)*(self.num_strips+1)-(x+1)
        #else:
            #print("oops case:", x, "", y)
        #print("LEDnum for ", x, ",", y, "is", LEDnum)
        return LEDnum
        
