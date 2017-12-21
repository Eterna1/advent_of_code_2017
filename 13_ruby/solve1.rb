#!/usr/bin/ruby -w

firewall = Hash.new
max_layer = nil
trip_severity = 0

STDIN.read.split("\n").each do |line|
   layer, deep = line.split(":").map{|x| x.to_i}
   max_layer = layer
   firewall[layer] = deep
end 

for step in 0..max_layer
    
    #skip if there is no scanner in this layer
    next if not firewall.key?(step)

    deepth = firewall[step]
    #count the position of the scanner in this layer    
    pos = step % ((deepth-1)*2)
    if pos >= deepth
        pos = pos - pos%deepth - 1
    end
    
    if pos == 0
        puts "caught at #{step}"
        trip_severity += deepth*step
    end
end

puts "the trip severity is #{trip_severity}"
