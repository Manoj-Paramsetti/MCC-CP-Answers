a = input("").lower()
#removing unwanted symbols
a = a.replace(".","")
a = a.replace(",","")
a = a.replace("?","")
a = a.replace("!"," ")
l = len(a)
n = a[:l-1]
splitted=[]
#splitting words
for i in n.split(" "):
    splitted.append(i)
#duplicating
dup=splitted
length = len(dup)
#removing rep. using set
splitted=set(splitted)
#converting to list to sort and to have order
splitted = list(splitted)
splitted.sort()
idx=""
i=0
for j in splitted:
    for x in range(0,length):
        if(j==dup[x]):
            #appending position and printing with the resp. word
            idx += " " +str(x)
    print(splitted[i]+idx)
    idx=""
    i+=1