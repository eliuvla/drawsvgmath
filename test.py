import drawsvgmath as drawmath
import math

escena = drawmath.Scene(width=640, height=480, id_prefix="test", palette=drawmath.palette.palette_dwm)

num = 10

p1 = drawmath.point.Point(0,0)
p2 = drawmath.point.Point(.1,.4)

line = drawmath.line.Line(p1,p2,size = 1)

#escena.add_object(line)
#escena.add_object(p1)
#escena.add_object(p2)

points = []

for i in range(0,2*num):
    paleta = drawmath.palette.Palette([(255*i/(2*num))%255,30,30])
    x = math.cos(10*math.pi*i/num)*(i/(2*num))
    y = math.sin(10*math.pi*i/num)*(i/(2*num))
    x = 2*i/(2*num)-1
    y = math.sin(2*2*math.pi*x)
    size = .2*(5*i/(num))
    point = drawmath.point.Point(x,y,size,paleta)
    points.append(point)
    #escena.add_object(point)

s = points[0]

for i in range(-num,num):
    for j in range(-num,num):
        x = (i/num) 
        y = (j/num)
        p = drawmath.point.Point(x,y)
        fp = drawmath.point.Point(x+math.cos(5*x),y+math.sin(5*y))
        escena.add_object(drawmath.line.Arrow(p,fp,size = .5,scale=.1))
flecha = drawmath.line.Arrow(p1,p2,size = 1)

#escena.add_object(flecha)
#escena.add_object(drawmath.line.StripLine(points))




escena.draw()
escena.save()