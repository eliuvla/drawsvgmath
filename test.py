import drawsvgmath as drawmath
import math

escena = drawmath.Scene(width=640, height=480, id_prefix="test", palette=drawmath.palette.palette_dwm)

num = 100

p1 = drawmath.point.Point(-.5,-.5)
p2 = drawmath.point.Point(.5,.5)

line = drawmath.line.Line(p1,p2,size = 1)

escena.add_object(line)
#escena.add_object(p1)
escena.add_object(p2)

points = []

for i in range(0,2*num):
    paleta = drawmath.palette.Palette([(255*i/(2*num))%255,30,30])
    point = drawmath.point.Point(math.cos(10*math.pi*i/num)*(i/(2*num)),math.sin(10*math.pi*i/num)*(i/(2*num)),.2*(5*i/(num)),paleta)
    points.append(point)
    #escena.add_object(point)

s = points[0]

for p in points:
    escena.add_object(drawmath.line.Line(s,p))
    s = p

escena.draw()
escena.save()