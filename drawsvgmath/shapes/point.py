from .shape import *
from ..palettes import *


import drawsvg as dw 

class Point(Shape):
    def __init__(self, x: int = 0, y: int=0, size : float = .01, palette : palette.Palette = palette.palette_default):
        self.center = [x,y]
        self.palette = palette
        self.radius = size

    def draw(self,scene):
        self.circle = dw.Circle(self.center[0],self.center[1],self.radius,
                                fill= self.palette.light, stroke=self.palette.dark, stroke_width=.7*scene.scale)
        scene.plane.append(self.circle)

    def projection(self,camera):
        pass
