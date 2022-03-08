#kristo tammeleht 
#4.2
'''
def mahlapakkide_arv(kogus):
    mahlapakidearv = round(kogus*0.4/3,0)
    return mahlapakidearv
kg = int(input('Sisesta õunade kogus: '))
print(mahlapakkide_arv(kg))
'''
#4.3
'''
def eelarve(a):
    summa = (a*10+55)
    return summa
kutsutud = int(input('Mitu inimest on kutsutud : '))
tuleb = int(input('Mitu inimest on tuleb : '))
print('maximaalne eelarve: ',eelarve(kutsutud),'eurot')
print('minimaalne eelarve: ',eelarve(tuleb),'eurot')
'''
#4.4
'''
kulalised = int(input('mitu külalist tuleb?: '))
def tervitus(q):
    for i in range(q):
        print('võõrustaja: "Tere!"')
        print(f"täna on{i+1}.kord tervitada ")
        
tervitus(kulalised)
'''
#4.5
'''
def pkarv(a):
    summa = 0
    fail = open(a , encoding="UTF-8")
    for i in fail:
        if int(i)<6:
            summa +=int(i)
    return summa
print(pkarv('mundid.txt'))
'''
#4.6

def kuu_nimi(a):
    kuud=[' ' ,' jaan','veeb','mär','apr']
    return kuud[a]
print(kuu_nimi(1))


def kuupaev(b):
    dd,mm,yyyy =b.split('.')
    print(dd,kuu_nimi (int(mm)),yyyy)
    
kuupaev('24.02.1918')
