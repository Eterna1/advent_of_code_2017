#!/usr/bin/ruby -w

require 'scanf'

class Particle
    def initialize(pX, pY, pZ, vX, vY, vZ, aX, aY, aZ)
        @pX = pX
        @pY = pY
        @pZ = pZ
        @vX = vX
        @vY = vY
        @vZ = vZ
        @aX = aX
        @aY = aY
        @aZ = aZ
        @removed = false
    end
    def distance()
        return @pX.abs + @pY.abs + @pZ.abs
    end
    def go()
        
        if @removed
            return
        end
        
        @vX += @aX
        @vY += @aY
        @vZ += @aZ
        @pX += @vX
        @pY += @vY
        @pZ += @vZ
    end
    def get_position()
        return [@pX, @pY, @pZ]
    end
    def removed
        return @removed
    end
    def mark_removed()
        @removed = true
    end
end

particles_ = STDIN.read.split("\n")
particles = Array.new

for particle in particles_
    #puts particle
    (pX, pY, pZ, vX, vY, vZ, aX, aY, aZ) = particle.scanf("p=<%d,%d,%d>, v=<%d,%d,%d>, a=<%d,%d,%d>")
    particles.push( Particle.new(pX, pY, pZ, vX, vY, vZ, aX, aY, aZ) )
        
end

for _ in 1...10000
    
    hash = Hash.new
    
    for p in 0..(particles.length-1)
        next if particles[p].removed
        pos = particles[p].get_position
        if hash.has_key?(pos)
            particles[p].mark_removed
            particles[hash[pos]].mark_removed
        else
            hash[pos] = p
        end
    end

    for p in 0..particles.length-1
        particles[p].go
    end
end

#count number of alive particles

alive_count = 0

for p in 0..(particles.length-1)
    if particles[p].removed == false
        alive_count += 1
    end
end

puts alive_count
