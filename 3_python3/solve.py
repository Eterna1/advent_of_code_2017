#!/usr/bin/python3

num = int(input())
 
offset_horizontal = 0; #poziomo
offset_vertical = 0; #pionowo

max_vertical = max_horizontal = 1
min_vertical = min_horizontal = -1

i = 1


#find offsets
while True:
    if i == num:
        break
    
    #go horizontally right
    while offset_horizontal != max_horizontal:
        
        if i == num:
            break
        
        offset_horizontal += 1
        i += 1
    max_horizontal += 1

    #go vertically up
    while offset_vertical != min_vertical:
        
        if i == num:
            break
        
        offset_vertical -= 1
        i += 1
    min_vertical -= 1

    #go horizontally left
    while offset_horizontal != min_horizontal:
        
        if i == num:
            break
        
        offset_horizontal -= 1
        i += 1
    min_horizontal -= 1

    #go vertically down
    while offset_vertical != max_vertical:
        
        if i == num:
            break
        
        offset_vertical += 1
        i += 1
    max_vertical += 1

print ("offset_horizontal %d" % offset_horizontal)
print ("offset_vertical %d" % offset_vertical)
print ("steps %d" % (abs(offset_vertical) + abs(offset_horizontal)))
