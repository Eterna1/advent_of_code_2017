#!/usr/bin/ruby -w 
#this is my first ruby program so....

require 'set'

$hash = Hash.new # dollar means a global variable
$weights = Hash.new
$summaric_weights = Hash.new
$file_input = "input.txt"

def parse_line(line)
    array = line.split('->')
    length = array.length
    
    weight = line.split('(')[1].split(')')[0].to_i
    
    name = array[0].split(" ")[0]
    
    $hash[name] = Array.new
    $weights[name] = weight
    $summaric_weights[name] = nil
    
    if length >= 2
       
        holded_discs = array[1].split(',')
       
        holded_discs.each do |disc|
            disc = disc.strip
            $hash[name].push(disc)
        end
        
    end
    
end

def find_root()
    while $hash.length > 1
        #remove empty discs and holding discs that have been removed
        
        $hash.each do |key, discs|
            if discs == []
                $hash.delete(key)
                if $hash.length == 1
                    break
                end
            else
                
                discs.each do |disc|
                    if ! $hash.key?(disc)
                        #remove from array
                        discs.delete(disc)
                    end
                end
                
            end
        end
        
    end
end

def print_root()
    
    $hash.each do |key, discs|
        puts("root: #{key}")
    end
end

def count_weights()
    changed = true
    while changed do
        changed = false
        
        $hash.each do |key, discs|
            
            next if $summaric_weights[key]
            if discs == []
                $summaric_weights[key] = $weights[key]
                changed = true
            else
                sum = 0
                
                discs.each do |disc|
                    if $summaric_weights[disc] == nil
                        sum = nil
                        break
                    else
                        sum += $summaric_weights[disc]
                    end
                end
                if sum != nil
                    changed = true
                    $summaric_weights[key] = sum + $weights[key]
                end
            end
            
        end
    end
end

def print_balance()
    $hash.each do |key, discs|
        puts "balance #{key} #{$summaric_weights[key]}"
    end
end

def find_unbalanced()

    min_balance = nil
    min_name = nil
    min_repaired_weight = nil
    
    $hash.each do |key, discs|
        
        weights = []
        discs.each do |disc|
            weights.push($summaric_weights[disc])
        end
        
        unique_weights = Set.new(weights)
        if unique_weights.length == 2
            
            a = unique_weights.to_a[0] #convert set to array
            b = unique_weights.to_a[1]
            
            unbalanced_summaric_weight = nil
            
            if weights.count(a) == 1
                unbalanced_summaric_weight = a
                balanced_summaric_weight = b
            else
                unbalanced_summaric_weight = b
                balanced_summaric_weight = a
            end
            index  = weights.index(unbalanced_summaric_weight)
            index2 = weights.index(balanced_summaric_weight)
            name_unbalanced = discs[index]
            name_balanced = discs[index2]
            
            unproper_sweight = $summaric_weights[name_unbalanced]
            proper_sweight = $summaric_weights[name_balanced] 
            
            diff = proper_sweight - unproper_sweight
            
            repaired_weight = $weights[name_unbalanced] + diff
            
            
            if min_balance == nil
                min_balance = weights[0]
                min_name = name_unbalanced
                min_repaired_weight = repaired_weight
            elsif weights[0] < min_balance
                min_balance = weights[0]
                min_name = name_unbalanced
                min_repaired_weight = repaired_weight
            end
        end
    end
    
    puts "name of unproper disc: #{min_name}"
    puts "should have weight: #{min_repaired_weight}"
end

#read the file
counter = 1
file = File.new($file_input, "r")
while (line = file.gets)
    parse_line(line)
    counter = counter + 1
end
file.close

count_weights
#print_balance
find_unbalanced
find_root
print_root

