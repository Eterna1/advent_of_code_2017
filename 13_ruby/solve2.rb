#!/usr/bin/ruby -w

$max_layer = nil
$firewall = Hash.new

STDIN.read.split("\n").each do |line|
   layer, deep = line.split(":").map{|x| x.to_i}
   $max_layer = layer
   $firewall[layer] = deep
end 

def will_caught?(delay)

    for step in 0..$max_layer
        
        #skip if there is no scanner in this layer
        next if not $firewall.key?(step)

        deepth = $firewall[step]
        #count the position of the scanner in this layer    
        pos = (step + delay) % ((deepth - 1) * 2)
        if pos >= deepth
            pos = pos - pos%deepth - 1
        end
        
        if pos == 0
            return true
        end
    end
    return false
end


for i in 0..1000000000
    if will_caught?(i) == false
        puts i
        break
    end
end
