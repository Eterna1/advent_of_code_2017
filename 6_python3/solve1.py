#!/usr/bin/python3

def read(fname):
    with open(fname,"r") as f:
        return f.read()


banks =  list(map(int, read("input.txt").split()))
print (banks)


s = set()
redistributions = 0

l = len(banks)

#go

while True:
    tbanks = tuple(banks)
    if tbanks in s:
        break
    s.add(tbanks)

    #redistribute
    m = max(banks)
    mi = banks.index(m)
    
    banks[mi] = 0
    
    #optimization
    full = m // l
    rest = m % l
    
    for i in range(l):
        banks[i] += full
        
    m = rest
    #end of optimization
    
    i = (mi + 1) % l
    while m!=0:
        banks[i] += 1
        m -= 1
        i = (i + 1) % l
    
    redistributions += 1

print ("redistributions to find a loop - %d" % redistributions)
