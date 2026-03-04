from .shape import *

import numpy as np
import drawsvg as dw 

class Point(Shape):
    def __init__(self):
        self.center = [0,0,0]
        self.color_stroke = [0,0,0]
        self.color_fill = [255,255,255]
        self.radius = 1


        self.center_2D = [0,0]

    def draw(self,scene):
        self.circle = dw.Circle(self.center_2D[0],self.center_2D[1],self.radius)
        scene.canvas.append(self.circle)

    def projection(self,camera):
        self.point = np.array(self.center)
        self.point = camera.transform @ self.point
        self.center_2D = self.point
        print(self.center_2D)

        self.point = np.array(self.center)

        x = self.point[0]*camera.row_0[0]+self.point[1]*camera.row_0[1]+self.point[2]*camera.row_0[2]
        y = self.point[0]*camera.row_1[0]+self.point[1]*camera.row_1[1]+self.point[2]*camera.row_1[2]

        self.center_2D = np.array([x,y])
        print(self.center_2D)
