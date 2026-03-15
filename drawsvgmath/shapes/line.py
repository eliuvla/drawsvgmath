from .shape import *
from .point import *
from ..palettes import *


import math
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

class StripLine(Shape):
    def __init__(self, points: list[Point], size: float = 1, palette : palette.Palette = None):
        self.palette = palette
        self.size = size
        self.points = points
        self.xy = []
        for point in self.points:
            x = point.center[0]
            y = point.center[1]
            self.xy.append(x)
            self.xy.append(y)


    def draw(self,scene):
        if self.palette == None:
            self.palette = scene.palette
        self.stripline = draw.Lines(*self.xy,stroke=self.palette.dark, stroke_linecap='round',
                                    stroke_width=self.point_scale*self.size, fill='none')
        self.inner_stripline = draw.Lines(*self.xy,stroke=self.palette.light, stroke_linecap='round',
                                          stroke_width=.5*self.point_scale*self.size, fill='none')
        scene.plane.append(self.stripline)
        scene.plane.append(self.inner_stripline)


class Arrow(Shape):
    def __init__(self, p1: Point=Point(0,0), p2: Point=Point(0,0), size : float =1, scale: float = 1,palette: palette.Palette = None):
        self.palette = palette
        self.size = size
        self.scale = scale
        self.p1 = p1
        self.p2 = p2
        self.scale_head = .5
        self.norm = self.scale*((self.p2.center[0]-self.p1.center[0])**2+(self.p2.center[1]-self.p1.center[1])**2)**.5
        self.angle = math.atan2(self.p2.center[1]-self.p1.center[1], self.p2.center[0]-self.p1.center[0])

    def draw(self,scene):
        if self.palette == None:
            self.palette = scene.palette
        x = (1-self.scale_head)*self.norm
        arrow = draw.Group(id='arrow')
        p = []
        p += [0,-self.point_scale*self.size]
        p += [x,-self.point_scale*self.size]
        p += [x,-2*self.point_scale*self.size]
        p += [self.norm, 0]
        p += [x,2*self.point_scale*self.size]
        p += [x,self.point_scale*self.size]
        p += [0,self.point_scale*self.size]
        p += [0,-self.point_scale*self.size]
        p += [x,-self.point_scale*self.size]
        arrow.append(draw.Lines(*p,stroke=self.palette.dark, fill = self.palette.light, stroke_linejoin='round', stroke_width=.25*self.point_scale*self.scale))
        rotation  = f" rotate({self.angle*(360/(2*math.pi))})"
        translation = f" translate({self.p1.center[0]}, {self.p1.center[1]})"
        scene.plane.append(draw.Use(arrow, 0, 0, transform=translation+rotation))