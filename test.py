import drawsvgmath as dwm
import math

escena = dwm.Scene(width=640, height=480, id_prefix="test")

num = 100

for i in range(0,2*num):
    paleta = dwm.palette.Palette([(255*i/(2*num))%255,30,30])
    escena.add_object(dwm.point.Point(math.cos(10*math.pi*i/num)*(i/(2*num)),math.sin(10*math.pi*i/num)*(i/(2*num)),.01*(i/2000*num),paleta))

escena.draw()
escena.save()