with open("artists.txt","r") as file:
    my_list=[]
    for line in file:
        stripped=line.strip()
        splitted=stripped.split(";")
        my_list.append(splitted)

def opener(a):
    with open(a,"r") as dosya:
        sacma=[]
        for eleman in dosya:
            stripped1=eleman.strip()
            splitted1=stripped1.split(";")
            sacma.append(splitted1)
    return sacma

sarkilar=[]
for deger in range(len(my_list)):
    sarkilar.append(opener(my_list[deger][1]))

for san in range(len(sarkilar)):
    for ben in range(len(sarkilar[san])):
        sarkilar[san][ben].append(my_list[san][0])

sortsartki=[]
for karakter in range(len(sarkilar)):
    for sarki in range(len(sarkilar[karakter])):
        sortsartki.append(sarkilar[karakter][sarki])

dates=[]
for character in range(len(sarkilar)):
    for element in range(len(sarkilar[character])):
        if (sarkilar[character][element][0]) not in dates:
            dates.append(sarkilar[character][element][0])

sorted_dates=sorted(dates)
a=0
while a<5:
    print(sorted_dates[a],":")
    for eleman in range(len(sortsartki)):
        if sorted_dates[a]==sortsartki[eleman][0]:
            print(sortsartki[eleman][1],"   ",sortsartki[eleman][2])
    a+=1










