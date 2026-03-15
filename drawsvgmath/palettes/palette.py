
class Palette():
    def __init__(self, light: list[3] = [255,255,255], mid: list[3] = [230,230,230], dark: list[3]=[0,0,0]):
        self.light_l = light
        self.mid_l = mid
        self.dark_l = dark
        self.light = None
        self.mid = None
        self.dark = None
        self.convert()
        
    def convert(self):
        self.light = self.cfc(self.light_l)
        self.mid = self.cfc(self.mid_l)
        self.dark = self.cfc(self.dark_l)
        

    def cfc(self,x):
        return "rgb("+str(x[0])+","+str(x[1])+","+str(x[2])+")"


#default palettes:

palette_default = Palette()
palette_dwm = Palette([165,227,134], [255,255,255], [17,34,9])

palette_red = Palette([240,16,16], [100,100,100], [30,0,0])
