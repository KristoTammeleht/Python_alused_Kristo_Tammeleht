#Harjutus02
#kristo tammeleht
#01.02.22
import math

#toodete hind
hind =36.75
soodus =0.4
kogus =3
summa =(hind-(hind*soodus))*kogus
print(kogus, "toote hind on",summa,"€" )


#kolmnurga ümbermäät
a,b,c =15,16,18
p=a+b+c
print("kolmnurga ümbermööt:",p)


kog = 12.90
inim = 3
joot = 0.1
jootraha =(kog/joot)
kogsum = (kog+jootraha)/inim
print ("iga inimene maksab ",kogsum,"€")


kiirus = 29.9
aeg = 0.4
vahemaa = (kiirus*aeg)
print('vahemaa on',vahemaa,'kilomeetrit tunnis')


a,b =16,9
hupo = pow(a,2)+pow(b,2)
kulg = math.sqrt(hupo)
print(kulg)


aeg = int(input("aeg minutites:"))
tund = aeg//60
minutid = aeg % tund
print (tund,'tundi',minutid,'minutid')


num = int(input("10 anrv:"))
print(bin(num),'binari',hex(num),'hex')

lit = int(input("mitu liitrit tankisid:"))
lab = int(input("läbitud kilo meetrid:"))
print(lit/lab*100,'l 100km kohta')


