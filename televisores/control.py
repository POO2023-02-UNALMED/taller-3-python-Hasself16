from televisores.tv import TV

class Control:
    def __init__(self):
        self.tv=TV
    
    def setTv(self, tv):
        self.tv=tv
    
    def getTv(self):
        return self.tv