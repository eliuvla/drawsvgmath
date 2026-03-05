import drawsvg as dw 

from .camera import * 


class Scene():
    def __init__(self, width = 256, height = 256 , id_prefix = 'unique_name', camera = Camera()):

        self.width = width
        self.height = height
        self.id = id_prefix
        self.name = "example"
        self.camera = camera
        self.min_dim = min(self.width,self.height)
        self.scale = min(self.camera.width/self.min_dim,self.camera.width/self.min_dim)
        self.plane = self.calculate_plane()
        self.objects = []

        self.origin = (0,0)
        
        self.canvas = dw.Drawing(width, height, origin= self.origin, id_prefix= self.id)
        self.canvas.append(dw.Rectangle(0, 00, self.width, self.height,fill='rgb(10,10,10)'))

    def draw(self):
        for object in self.objects:
            object.draw(self)
        self.canvas.append(self.plane)

    def calculate_plane(self):
        t2 = 'translate('+str(1/self.scale+(self.width-self.min_dim)/2)+','+str(1/self.scale+(self.height-self.min_dim)/2)+') '
        s = 'scale('+str(1/self.scale)+',-'+str(1/self.scale)+') '
        t1 = 'translate('+str(self.camera.target[0])+','+str(self.camera.target[1])+')'
        return dw.Group(transform= t2+s+t1)


    def add_object(self, obj):
        self.objects.append(obj)

    def save(self):
        self.canvas.save_svg(self.name+".svg")


