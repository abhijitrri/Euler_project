#Generating the fibonacci seq
s = 2
flist = [1,2]
term = flist[1]
i=2
n=4000000
while(term<n):
    term = flist[i-1] + flist[i-2]

    if term < n and term%2==0:
        s+=term
    i+=1
    flist.append(term)

#print(flist)
print(s)