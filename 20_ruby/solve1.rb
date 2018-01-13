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
    end
    def distance()
        return @pX.abs + @pY.abs + @pZ.abs
    end
    def go()
        @vX += @aX
        @vY += @aY
        @vZ += @aZ
        @pX += @vX
        @pY += @vY
        @pZ += @vZ
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
    for p in 0..particles.length-1
        particles[p].go
    end
end

closest_particle = 0
closest_distance = particles[0].distance
for p in 0..particles.length-1
    d = particles[p].distance
    if d < closest_distance
        closest_distance = d
        closest_particle = p
    end
    particles[p].go
end

puts closest_particle
