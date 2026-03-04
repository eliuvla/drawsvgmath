from .shape import *
#from scene import *

import numpy as np

import drawsvg as dw 

class Sphere(Shape):
    def __init__(self):
        self.center = (0,0,0)
        self.color_stroke = (0,0,0)
        self.color_fill = (255,255,255)
        self.radius = 1

        self.color_stroke_format = "rgb({},{},{})".format(*self.color_stroke)
        self.color_fill_format = "rgb({},{},{})".format(*self.color_fill)

        print(self.color_stroke_format)


    def draw(self, scene ):
        self.circle = dw.Circle(self.center[0], self.center[1], self.radius, fill = self.color_fill_format, stroke = self.color_stroke_format)
        scene.canvas.append(self.circle)

    def projection(self, camera):
        self.radius = 1
        self.point = np.array([0,0,0,1])
        self.point = self.point.reshape(4,1)

        self.point = camera.transform*self.point


        self.center = np.ravel(self.point)

