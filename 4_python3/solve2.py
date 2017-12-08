#!/usr/bin/python3

def read(fname):
    with open(fname,"r") as f:
        return f.read()

data = read("input.txt")

valid_count = 0

for line in data.split("\n"):
    if line.strip() == "":
        continue
    s = set()
    is_valid = True
    
    for t in line.split():
        t = t.strip()
        t=tuple(sorted(t))
        if t in s:
            is_valid = False
            break
        s.add(t)
        
    valid_count += int(is_valid)

print (valid_count)
