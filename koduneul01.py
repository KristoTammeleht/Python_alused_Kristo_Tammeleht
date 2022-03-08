#Kristo Tammeleht 

# 1.1

def ter():
    print('Tere, maailm!')
ter()

#1.2
aa = 2020
liblikas = 'teelehe-mosaiikliblikas'
lause_keskosa = 'Aasta liblikas on '
lause = lause_keskosa+liblikas
print(lause)

#1.3
pilv = int(float(input("Sisesta pilvede kõrgus kilomeetrites: ")))
if pilv >= 6.0:
    print("Need on ülemised pilved.")
else:
    print("Need ei ole ülemised pilved.")

#1.4
koht = int(input('Inimeste arv: '))
buss = int(input('Bussikohtade arv: '))

last = koht%buss

if last == 0:
    buss = koht//buss
    last = buss
else:
    buss = koht//buss+1

print(f"Busse peab olema: {buss} \nViimases bussis on inimesi: {last}")