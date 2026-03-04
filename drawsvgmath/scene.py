import drawsvg as dw 
#from shapes.shape import *


class Scene():
    def __init__(self, width = 256, height = 256 , id_prefix = 'unique_name', camera = None):

        self.width = width
        self.height = height
        self.id = id_prefix
        self.name = "example"
        self.camera = camera 

        #self.objects: list[Shape] = []
        self.objects = []

        self.origin = (-self.width/2, -self.height/2)

        self.canvas = dw.Drawing(width, height, origin= self.origin, id_prefix= self.id)

    def draw(self):
        for object in self.objects:
            object.draw(self)

    def save(self):
        self.canvas.save_svg(self.name+".svg")

