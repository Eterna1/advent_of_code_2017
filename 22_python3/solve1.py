#!/usr/bin/python3 

FNAME = "input.txt"
BURSTS = 10000

def get_grid_from_file(fname):
    lines = []
    with open(fname) as f:
        for line in f:
            line = line.strip()
            lines.append(line)
    
    grid_size = len(lines[0])
    grid = {}
    for i in range(grid_size):
        for ii in range(grid_size):
            grid[(i-grid_size//2,ii-grid_size//2)] = lines[i][ii]
    return grid

def is_infected(grid, position):
    return grid.get(position, '.') == '#'
    
def clean_infection(grid, position):
    grid[position] = '.'
    
def set_infection(grid, position):
    grid[position] = '#'

def go(position, direction):
    return (position[0]+direction[0], position[1]+direction[1])

def turn_left(direction):
    if direction == (-1, 0):
        return (0, -1)
    if direction == (1, 0):
        return (0, 1)
    if direction == (0, 1):
        return (-1, 0)
    if direction == (0, -1):
        return (1, 0)
    
def turn_right(direction):
    if direction == (-1, 0):
        return (0, 1)
    if direction == (1, 0):
        return (0, -1)
    if direction == (0, 1):
        return (1, 0)
    if direction == (0, -1):
        return (-1, 0)

def main():
    grid = get_grid_from_file(FNAME)
    current_direction = (-1, 0)
    current_position = (0, 0)
    total_infections = 0
    for i in range(BURSTS):
        #print (current_position)
        if is_infected(grid, current_position):
            #print ("infected")
            clean_infection(grid, current_position)
            current_direction = turn_right(current_direction)
            current_position = go(current_position, current_direction)
        else:
            #print ("not infected")
            set_infection(grid, current_position)
            total_infections += 1
            current_direction = turn_left(current_direction)
            current_position = go(current_position, current_direction)
    
    print(total_infections)

if __name__ == "__main__":
    main()
