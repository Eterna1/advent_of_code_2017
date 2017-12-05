#!/usr/bin/python3

num = int(input())
 
offset_horizontal = 0; #poziomo
offset_vertical = 0; #pionowo

max_vertical = max_horizontal = 1
min_vertical = min_horizontal = -1

i = 1

tab = {}

def set_item(off_h, off_v, value):
    """
    off_h -- horizontal offset
    off_v -- vertical offset
    """
    
    if off_h not in tab:
        tab[off_h] = {}
    
    tab[off_h][off_v] = value
    
def count_neighbors(off_h, off_v):
    sum = 0
    
    
    for off_h_ in range(off_h-1, off_h+2):
        for off_v_ in range(off_v-1, off_v+2):
            if (off_h_, off_v_) == (off_h, off_v):
                continue
            
            if off_h_ in tab:
                if off_v_ in tab[off_h_]:
                    sum += tab[off_h_][off_v_]
            
    return sum


#find offsets
while True:
    if i > num: 
        break
        
    
    #go horizontally right
    while offset_horizontal != max_horizontal:
        
        if i == 1:
            set_item(offset_horizontal, offset_vertical, i)
            offset_horizontal += 1
            break
        
        i = count_neighbors(offset_horizontal, offset_vertical)
        if i > num:
            break
            
        
        set_item(offset_horizontal, offset_vertical, i)
        offset_horizontal += 1
        
    max_horizontal += 1

    #go vertically up
    while offset_vertical != min_vertical:
        
        i = count_neighbors(offset_horizontal, offset_vertical)
        if i > num:
            break
        
        set_item(offset_horizontal, offset_vertical, i)
        offset_vertical -= 1
        
    min_vertical -= 1

    #go horizontally left
    while offset_horizontal != min_horizontal:
        
        i = count_neighbors(offset_horizontal, offset_vertical)
        if i > num:
            break
        
        set_item(offset_horizontal, offset_vertical, i)
        offset_horizontal -= 1
        
    min_horizontal -= 1

    #go vertically down
    while offset_vertical != max_vertical:
        
        i = count_neighbors(offset_horizontal, offset_vertical)
        if i > num:
            break
        
        set_item(offset_horizontal, offset_vertical, i)
        offset_vertical += 1
        
    max_vertical += 1
    

print ("offset_horizontal %d" % offset_horizontal)
print ("offset_vertical %d" % offset_vertical)
print ("steps %d" % (abs(offset_vertical) + abs(offset_horizontal)))
print ("larger value written - %d" % i)
