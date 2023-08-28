from televisores.tv import TV

class Control:
    def setTv(self, tv):
        self.tv=tv
    
    def getTv(self):
        return self.tv
    
    def enlazar(self, tv):
        self.tv=tv
        TV.setControl(Control)
