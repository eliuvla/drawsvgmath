from .shape import *
from .point import *
from ..palettes import *



import drawsvg as draw 


class Line(Shape):
    def __init__(self, p1: Point = Point(0,0), p2: Point=Point(0,0), size : float = 1, palette : palette.Palette = None):
        self.palette = palette
        self.size = size
        self.p1 = p1
        self.p2 = p2


    def draw(self,scene):
        if self.palette == None:
            self.palette = scene.palette
        sx = self.p1.center[0]
        sy = self.p1.center[1]
        ex = self.p2.center[0]
        ey = self.p2.center[1]
        self.line = draw.Line(sx,sy,ex,ey, stroke=self.palette.dark, stroke_linecap='round',
                              stroke_width=self.point_scale*self.size)
        self.inner_line = draw.Line(sx,sy,ex,ey, stroke=self.palette.light, stroke_linecap='round',
                                    stroke_width=.5*self.point_scale*self.size)
        scene.plane.append(self.line)
        scene.plane.append(self.inner_line)

