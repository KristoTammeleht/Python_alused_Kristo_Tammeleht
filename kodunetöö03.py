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



fail = input('lisa faili nimi:')
fail = open(fail , encoding="UTF-8")
num = 1
for i in fail:

    print (num, i)
    num += 1


fail.close()


























































































































































































