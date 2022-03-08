'''
fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:

    vastuvõetud.append(int(rida))
    
aasta = int(input('Sisesta aasta: '))
print(f'{aasta}.  {vastuvõetud (aasta[3])-1}')

fail.close()
'''
#3.2
'''
ring = int(input('sisesta mitu ringi '))
porgandid = 0
for i in range (1,ring+1):
    if i%2==0:
        porgandid+=i
print(f'porgantite saadav arv on: {porgandid}')
'''
#3.3
'''
fail = open("konto.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:
    srida = float(rida)
    if   srida > 0 :
        print (srida,end= '')

fail.close()
'''
#3.4
'''
nums =1
lugu=1
algfail = input('lisa faili nimi:')
fail = open(algfail , encoding="UTF-8")
num = 1
for i in fail:
    print (str(num)+'.'+str(i),end='')
    num += 1
    
    
print()
fail = open(algfail , encoding="UTF-8")
laul = int(input('Mis lugu tahad (numbrites):'))
for  i in fail:
    if lugu== laul:
        print (str(nums)+'.'+str(i),end='')
    nums += 1
    lugu +=1
  
fail.close()
'''
'''
#3.5
jrk = 1
fail = open('nimekiri.txt' , encoding="UTF-8")
from datetime import * 
kp = print(datetime.now().day)

for i in fail:
    if jrk == datetime.now().day:
        print(i)
    
    jrk += 1
    
'''

























































































































































































