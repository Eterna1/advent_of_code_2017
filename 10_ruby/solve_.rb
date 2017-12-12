#!/usr/bin/ruby

file_input = "input2.txt"
list_size = 256

list = 0.upto(list_size - 1).to_a

file = File.new(file_input)
line = file.gets
file.close

lengths = line.strip().split('').map{|x| x.ord } + [17, 31, 73, 47, 23]

puts lengths.join(',')

skip_size = 0

for i in 1..64
    #puts(lengths.join(","))

    moved = 0

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
        
    end
end

while (moved % list_size) != 0
    list = list[1..-1] + [list[0]]
    moved += 1
end

#change this hash to sparse hash

puts("--------------")

for i in 0..15
    block = list[i*16, 16]
    puts block.join(",")
    xor_sum = block.reduce(:^)
    puts xor_sum
end
