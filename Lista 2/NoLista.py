class NoLista:
    def __init__(self, info, prox):
        self.info = info
        self.prox = prox
    
    def setInfo(self, info):
        self.info = info
        
    def getInfo(self):
        return self.info
    
    def setProx(self, prox):
        self.prox = prox
    
    def getProx(self):
        return self.prox
    
    def __str__(self):
        return str(self.info)