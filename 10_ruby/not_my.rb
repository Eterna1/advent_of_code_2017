def tie_knot(lengths, rounds = 1)
  list = (0..255).to_a
  skip = 0
  rotations = 0

  rounds.times do
    lengths.each do |length|
      list[0...length] = list[0...length].reverse

      list = list.rotate(length + skip)
      rotations += length + skip
      skip += 1
    end
  end

  list.rotate(-rotations)
end

file = File.new("input.txt")
INPUT = file.gets.strip()
file.close

result = tie_knot(INPUT.split(",").map(&:to_i))
knot_value = result[0] * result[1]

puts "The check value of the knot is:", knot_value, nil

MAGIC_NUMBERS = [17, 31, 73, 47, 23].freeze

a = INPUT.bytes + MAGIC_NUMBERS
puts a.join(",")

result = tie_knot(INPUT.bytes + MAGIC_NUMBERS, 64)
knot_hash = result.each_slice(16).map { |block| format("%02x", block.inject(:"^")) }.join

puts "The Knot Hash for the input is:", knot_hash 
