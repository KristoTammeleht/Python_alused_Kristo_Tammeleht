#Kristo Tammeleht IT-21 16.02.22
era = []

with open('S6.txt','r') as fail:   
    for i in fail:
        rida = i.split(" ")
        
        print(f"{rida[0]:11} {rida[1]:11} {rida[2]:11} {rida[3]:11}")
        if rida[2] not in era:
            era.append(rida[2])
            
        print(f"{rida[0]:11} {rida[1]:11}", file=open("output.txt", "a"))

with open("S6.txt") as f:
    contents = f.read()
    count = contents.count("RE")
    count2 = contents.count("KE")
    print ('Reformikaid:',count)
    print ('Kesikud:',count2)


        
er = set(era)
kokku = len(er)
print(kokku)
