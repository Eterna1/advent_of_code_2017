from pwn import *

num = read("data")
s = 0

num = num.strip()
l= len(num)

for i in range(l):
    if num[i] == num[(i+1) %l ]:
        s+=int(num[i])
        print int(num[i])
        

print s
