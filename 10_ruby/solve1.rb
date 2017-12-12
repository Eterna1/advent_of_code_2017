#!/usr/bin/ruby

file_input = "input.txt"
list_size = 256

list = 0.upto(list_size - 1).to_a

file = File.new(file_input)
line = file.gets
file.close

lengths = line.split(",").map{|x| x.to_i}
skip_size = 0


#puts(lengths)

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


while (moved % list_size) != 0
    list = list[1..-1] + [list[0]]
    moved += 1
end


puts(list[0]*list[1])
