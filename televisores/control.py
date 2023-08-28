from televisores.tv import TV

class Control:
    nControl=0
    def __init__(self):
        Control.nControl += 1
    
    def setTv(self, tv):
        self.tv=tv
    
    def getTv(self):
        return self.tv
    
    def enlazar(self, tv):
        x=Control.nControl
        self.tv=tv
        TV.setControl(x)
