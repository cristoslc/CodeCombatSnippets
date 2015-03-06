# Obey user override flags

def obeyUserFlags():
    f = self.findFlag()
    if f:
        fColor = f.color
        self.pickUpFlag(f)
        if fColor == 'black':
            if self.isReady('cleave'):
                e = self.findNearest(self.findEnemies())
                self.cleave(e)
