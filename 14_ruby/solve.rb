#!/usr/bin/ruby -w

def knot_hash_bin(input)
    list_size = 256
    list = 0.upto(list_size - 1).to_a

    lengths = input.split('').map{|x| x.ord } + [17, 31, 73, 47, 23]
    skip_size = 0


    moved = 0

    for i in 1..64
        lengths.each do |length|

            if length != 0
                reversed = list[0..length-1].reverse
                list = reversed + list[length..-1]
            end
            
            1.upto(length).each do |i|
                list = list[1..-1] + [list[0]]
                moved += 1
            end
            
            1.upto(skip_size).each do |i|
                list = list[1..-1] + [list[0]]
                moved += 1
            end
            
            skip_size += 1
            if skip_size == list_size
                skip_size = 0
            end
        end
    end


    while (moved % list_size) != 0
        list = list[1..-1] + [list[0]]
        moved += 1
    end

    hash = ""

    for i in 0..15
        block = list[i*16,16]
        xorsum = block.reduce(:^)
        hash += "%08b" % xorsum
    end

    return hash
end 

input = ARGV[0]

used = 0

grid = Array.new

for i in 0..127
    row = knot_hash_bin("%s-%d" % [input, i])
    used += row.count("1")
    grid.push(row)
end

puts(used)

GRID_MAX = 127

#count regions
regions = 0
for i in 0..GRID_MAX
    for ii in 0..GRID_MAX
        if grid[i][ii] == "1"
            regions += 1
            #zero the whole region
            stack = [[i,ii]]
            while stack.length!=0
                v_x, v_y = stack.pop() #currently visiting
                next if v_x < 0 || v_y < 0 || v_x > GRID_MAX || v_y > GRID_MAX
                next if grid[v_x][v_y] == "0"
                grid[v_x][v_y] = "0"
                stack.push([v_x+1, v_y])
                stack.push([v_x-1, v_y])
                stack.push([v_x, v_y+1])
                stack.push([v_x, v_y-1])
            end
        end
    end
end



puts (regions)
