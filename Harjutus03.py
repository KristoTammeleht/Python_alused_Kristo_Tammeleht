#Kristo Tammeleht It-21 28.02.22


nim = input("Sisesta oma nimi: ")
nim = nim.strip().capitalize()

print("Tere",nim+"!")


tekst = input("Sisesta tekst: ")
vanne = tekst.lower().replace("kurat","*****")
print(vanne)



email = input("Kirjuta oma email: ")
print('@' in email)


alg = input("Sisesta tundide algus: ")
lop = input("Sisesta tundide lõpp: ")
h1, min1 = alg.split(":")
h2, min2 = lop.split(":")
minutid1 = int(h1)*60+int(min1)
minutid2 = int(h2)*60+int(min2)
aeg = abs(minutid1-minutid2)
aegH = aeg // 60
aegM = aeg % 60
print(f"Kool kestis {aegH}:{aegM}")



palin = input("Sisesta palindroom: ")
pal = palin.lower()
rev_pal = reversed(pal)
if list(pal) == list(rev_pal):
    print("Tekst on palindroom.")
else:
    print("Tekst ei ole palindroom.")