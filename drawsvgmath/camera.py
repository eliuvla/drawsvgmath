import numpy as np
import math

class Camera():
    def __init__(self):
        self.position = [20,20,10]
        self.target = [0,0,0]
        self.projection()

        


    def projection(self):
        r = normalize(np.array(self.target)-np.array(self.position))
        x,y,z = r
        row_0 = [0,-z,y]
        row_1 = [-z,0,x]
        row_2 = [x,y,z]

        self.row_0 = row_0
        self.row_1 = row_1
        
        self.transform = np.row_stack((row_0,row_1,row_2))

        print(self.transform)

        

def normalize(x):
    sum = 0
    for x_i in x:
        sum += x_i**2

    sum = (sum)**(.5)

    if sum == 0:
        sum = 1
    else:
        sum = 1/sum

    return sum*x
