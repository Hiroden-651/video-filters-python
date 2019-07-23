"""
    The "Cool-Filter" object.
"""

import cv2 as cv
import numpy as np

class CoolWarmFilter:
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def apply(self, img):
        img[:,:,0] = img[:,:,0] + self.blue
        img[:,:,1] = img[:,:,1] * self.green
        img[:,:,2] = img[:,:,2] * self.red
        return img
    #end

    def adjust(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b
    #end
    

#end class

cooling = CoolWarmFilter(0.75,0.75, 0)
test_img = cv.imread("ChickenFriend.png")
cv.imshow("Original Image", test_img)
cv.imshow("Filtered Image", cooling.apply(test_img))
cv.waitKey(0)
cv.destroyAllWindows()