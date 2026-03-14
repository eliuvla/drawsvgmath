from .shape import *
from ..palettes import *


import drawsvg as draw 


class Point(Shape):
    def __init__(self, x: float = 0, y: float = 0, size : float = 1, palette : palette.Palette = None): 
        self.center = [x,y]
        self.palette = palette
        self.size = size
        self.radius = size*self.point_scale

        


    def draw(self,scene):
        if self.palette == None:
            self.palette = scene.palette
        self.circle = draw.Circle(self.center[0],self.center[1],self.radius,
                                fill= self.palette.light, stroke=self.palette.dark, stroke_width=.25*self.point_scale*self.size)
        scene.plane.append(self.circle)

    def projection(self,camera):
        pass
