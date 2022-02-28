#Kristo Tammeleht IT-21 28.02.22
import random

suv = []
for n in range(5):
    suv.append(random.randint(1,10))
for n in range(len(suv)):
    print("*"*suv[n])


van = []
for m in range(5):
    van.append(random.randint(1,99))
print(f"Ages: {van}")
print("Max:",max(van))
print("Min:",min(van))
print("Sum:",sum(van))
print("Avg:",sum(van)/len(van))


nimed = ['Juhan','Kati','Mario','Mario','Mati','Mati']
for l in nimed:
    if nimed.count(l) > 1:
        nimed.remove(l)
print(nimed)


opilane = ['mati','kalle','pille','sille','tille']
for j in range(len(opilane)):
    print(j+1,opilane[j])


nr = int(input("Vali number (1-5): "))
del opilane[nr-1]
add = input("Sisesta muudatused: ")
opilane.insert(nr-1, add)

for k in range(len(opilane)):
    print(opilane[k])


arvud = []
for i in range(5):
    arvud.append(random.randint(1,20))
for n in range(len(arvud)):
    print("*"*arvud[n])