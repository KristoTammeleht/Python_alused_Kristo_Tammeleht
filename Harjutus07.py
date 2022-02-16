#Kristo Tammeleht IT-21 16.02.22
import math

def nimi(nim,kl='ger'):
    if kl == 'est':
        print(nim,'tere')
    elif kl == 'eng':
        print(nim,'hello')
    else:
        print(nim,'tere saksa keeles')
    
nimi('Kristo','')
############################
def kuupp(kulg):
    v = kulg**3
    return v
def kera(raadius):
    v= (4/3*math.pi*r**2)
    return v

def kon(r,h):
    v = round(1/3*math.pi*r**2*h,2)
    return v

def sil(r,h):
    v = round(math.pi*r**2*h,2)
    return v
##################################
print('********** LEIAME RUUMALA **********')
print('Vali kujund')
print('1 Kuup')
print('2 Kera')
print('3 Koonus')
print('4 Silinder')
numb = int(input('Sisesta soovitud kujundi number:'))

if numb == 1 :
    kub = int(input('siseta kuubi uks kulg: '))
    print('kuubi pindala on:' , kuupp(kub))
    
elif numb == 2 :
    r = int(input('siseta kra raadius: '))
    print('kera pindala on:' , kera(r))
    
elif numb == 3 :
    r = int(input('siseta  raadius: '))
    h = int(input('siseta  kõrgus: '))
    print('koonuse pindala on:' , kon(r,h))
    
else :
    r = int(input('siseta  raadius: '))
    h = int(input('siseta  kõrgus: '))
    print('silindri pindala on:' , sil(r,h))

    
