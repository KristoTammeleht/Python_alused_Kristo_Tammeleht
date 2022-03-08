import random

#2.1
"""
a = int(input('Sisestage mitu korda äratada: '))
print('Tõuse ja sära!\n'*a)

"""

'''
#2.2
ring = int(input('mitu ringi '))
porgandid = 0
i = 1
while i <= ring:
    if i%2==0:
        porgandid+=i
        print(i)
    i += 1
print(f'porgantite arv on {porgandid}')
'''
#2.3
"""
tar = int(input('Täringute arv: '))

for i in range(tar):
    print(random.randint(1,6), end="\n")
""" 

'''
#2.4
risng = int(input('sisesta arv'))
i = 1
nisu = 1
while i < risng:
    nisu*=2
    i += 1
    print (f'nisu teri on {risng} ruudu eest: {nisu}')
    '''
#2.5
'''
vmees = int(input('mitu õuna:'))
võun = 14
for i in range(vmees):
    oun = random.randint(1,2)
    lumi = võun -oun 
    print(oun)
print (f'lumivakekesel jäi {lumi}')
'''

    
    