class NoArvoreBinaria:
    def __init__(self, info, esq=None, dir=None):
        self.info = info
        self.esq = esq
        self.dir = dir

    def setInfo(self, info):
        self.info = info

    def getInfo(self):
        return self.info

    def setEsq(self, esq):
        self.esq = esq

    def getEsq(self):
        return self.esq

    def setDir(self, dir):
        self.dir = dir

    def getDir(self):
        return self.dir

    def toString(self):
        return str(self.info)
