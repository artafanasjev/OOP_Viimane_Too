class Karakterid:
    def __init__(self, nimi, elud, tugevus):
        self.nimi = nimi
        self.elud = elud
        self.tugevus = tugevus
        
    def kaotaElusi(self, kogus):
        self.elud -= kogus
        if self.elud < 0:
            self.elud += 0
            
    def lisaElusi(self, kogus):
        self.elud += kogus
        
class Vaenlane:
    def __init__(self, elud, tugevus):
        self.elud = elud
        self.tugevus = tugevus
        
    def kaotaElusi(self, kogus):
        self.elud -= kogus
        if self.elud < 0:
            self.elud += 0