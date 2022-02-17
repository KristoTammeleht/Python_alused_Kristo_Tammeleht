#Kristo Tammeleht IT-21 17.02.22

class auto:
    #atribuudid
    nimi = 'teadmata'
    aasta = 0
    mark = 'teadmata'
    hind = 0
    varv = 'teadmata'
    kiirus = 0
    
    #meetodid
    def __init__(self,x,y,z):
        self.nimi = x
        self.aasta = y
        self.hind = z
        
    def kuva(self):
        print('Nimi: {} \nAasta: {} \nEurot: {}'.format(self.nimi, self.aasta, self.hind))
        
    def lisamark(self,x):
        self.mark = x
        
    def kuvamark(self):
        print('Mark: {}'.format(self.mark))
        
    def lisavarv(self,x):
        self.varv = x
        
    def kuvavarv(self):
        print('varv: {}'.format(self.varv))
        
    def lisakiirus(self,x):
        self.kiirus = x
        
    def kuvakiirus(self):
        print('km/h: {}'.format(self.kiirus))
        

uusObjekt = auto("ae36", 2006,50000)
uusObjekt.lisamark('bmw')
uusObjekt.lisavarv('sinine')
uusObjekt.lisakiirus(120)
uusObjekt.kuva()
uusObjekt.kuvamark()
uusObjekt.kuvavarv()
uusObjekt.kuvakiirus()
print('############################')
uusObjekt = auto("s13", 1959,556000)
uusObjekt.lisamark('nissan')
uusObjekt.lisavarv('valge')
uusObjekt.lisakiirus(367)
uusObjekt.kuva()
uusObjekt.kuvamark()
uusObjekt.kuvavarv()
uusObjekt.kuvakiirus()