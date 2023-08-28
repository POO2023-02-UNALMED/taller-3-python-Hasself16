from televisores.tv import TV

class Control:
    nControl=0
    def __init__(self):
        Control.nControl += 1
    
    def setTv(self, tv):
        self.tv=tv
    
    def getTv(self):
        return self.tv
    
    def enlazar(cls, self, tv):
        self.tv=tv
        TV.setControl(cls.nControl)
