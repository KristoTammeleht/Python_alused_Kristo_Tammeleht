#kristo Tammeleht it-21 02.02.22

'''
7. Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR.
	kuvatakse korrektne arusaadav küsimus ja vastus - 1p
	kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
	küsitakse valuuta kogust ja tehakse arvutused - 2p
	kood kommenteeritud - 1p+
'''
#inimene teb valiku raha vahetuse vahel
valik = int(input('Vajuta 1 et saada EUR->EEK ja vajuta 2 et saada EEK->EUR:'))
#kontrollib mis valiku tegi inimene
if valik >2 or valik<1:
    print('sellist valikut ei ole')
elif valik == 1:
    #küsib mis summa ta tahab teada
    eurcon = float(input('EUR->EEK:'))
    #vahetus summa arvutamine
    vast = eurcon * 15.64664
    #välja trükkimine
    print (eurcon ,'EUR on',vast ,'EEK')
    #kui inimene valis nr 2 siis ta tuuakse siia
    
else :
    #küsitakse summa vahetus üle
    eekcon = float(input('EEK->EUR:'))
    #vahetuse summa arvutamine
    evast = eekcon * 0.063911485
    #välja trükimine
    print (eekcon ,'EEK on',evast ,'EUR')
    



