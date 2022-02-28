#kristo Tammeleht IT-21 28.02.22

print("Kas su kujund on ruut või ei.")
a = int(input("Kujundi esimene külg: "))
b = int(input("Kujundi teine külg: "))
if a == b:
    print ("On ruut.")
else:
    print("Ei ole ruut.")


c = int(input("Esimene täisarv: "))
d = int(input("Teine täisarv: "))
tehe = input("Mis tehte soovid teha (+-*/): ")

if tehe=="+":
    v = c+d
elif tehe=="-":
    v = c-d
elif tehe=="*":
    v = c*d
else:
    v = c/d
print(f"{c}{tehe}{d}={v}")


syn = int(input("Sisesta oma sünniaasta: "))
yer = 2022
van = yer-syn
van = van/5
if van == int(van):
    print("Juubel.")
else:
    print("Ei ole juubel.")


hind = int(input("Sisesta toote hind täisarvuna: "))
soodus1 = hind-(hind*0.1)
soodus2 = hind-(hind*0.2)
if (hind <= 10):
    print(f"Toote lõpphind on {soodus1}€")
else:
    print(f"Toote lõpphind on {soodus2}€")

sugu = input("Sisesta oma sugu (m/n): ")
sugu = sugu.lower()
if sugu == "m":
    vanus = int(input("Sisesta oma vanus: "))
    if (vanus >= 16 and vanus <= 18):
        print("Õnnitlen, oled tiimis!")
    else:
        print("Vanus ei sobi!")
else:
    print("Ei sobi kuna sa oled naine.")

for i in range(1,6):
    for j in range(1,6):    
        print('* ', end='')
    print()
print("----------")
for k in range(0,5):
    for l in range(0,k+1):
        print("*",end="")
    print()
print("----------")
for m in range(5,0,-1):
    for n in range(0,m):
        print("*",end="")
    print()

import random
random = random.randint(10000,99999)
print(f"Sinu suvaline number on: {random}")


arv = int(input("Sisesta täisarv 1-100: "))
jaak = arv%2
 
if jaak==0:
    print('Paaris')
else:
    print('Paaritu')


for p in range(1,11):
    for q in range(5,6):
        print(p, "x", q, "=", p*q)


for a in range(1,21):
    for b in range(5,6):
        print(a*b)


print("Arva ära number 1-10ni.")

nr = 7
loop = 1
kordade_arv = 0

while loop == 1:
    
    arva= int(input("Sisesta täisarv: "))
    
    if kordade_arv >= 2:
        kordade_arv += 1
        loop = 3
        print(f"GAME OVER!! Sinu kordade arv {kordade_arv}")
    elif arva == nr:
        kordade_arv += 1
        print("said õige arvu, pakkumiste arv:",kordade_arv)
        loop = 2
    elif arva > nr:
        kordade_arv += 1
        print("Arv on väiksem.")
    elif arva < nr:
        kordade_arv += 1
        print("Arv on suurem.")


moni = float(input("Sisesta raha: "))
konto = 0
intress = 0.05
konto = konto + moni
print("Aasta | Algsumma | Intress | Aasta lõpuks")
for c in range(1,6):
    kasum = konto*intress
    print(f" {c}: {round(konto,2):10},{round(kasum,2):10},{round(konto+kasum,2):10}")
    konto = konto + kasum


print("Arv |Ruut |Kuup |")
print("----------------")
for c in range(1,11):
    print(f"{c:3} | {c*c:3} | {c*c*c:3}")
