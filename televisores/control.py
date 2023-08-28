class Control:
    def __init__(self):
        self.tv=None
    
    def setTv(self, tv):
        self.tv=tv
    
    def getTv(self):
        return self.tv
    
    def enlazar(self, tv):
        self.tv=tv
        tv.setControl(self)