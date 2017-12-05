from pwn import *

num = read("data")
s = 0

num = num.strip()
l= len(num)
forward = l/2

for i in range(l):
    if num[i] == num[(i+forward) %l ]:
        s+=int(num[i])
        print int(num[i])
        

print s
