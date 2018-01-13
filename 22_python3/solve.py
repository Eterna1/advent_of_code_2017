#!/usr/bin/python3 

FNAME = "input.txt"
BURSTS = 10000000

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
    
def is_clean(grid, position):
    return grid.get(position, '.') == '.'
    
def is_weakened(grid, position):
    return grid.get(position, '.') == 'W'
    
def is_flagged(grid, position):
    return grid.get(position, '.') == 'F'
    
def set_clean(grid, position):
    grid[position] = '.'
    
def set_infected(grid, position):
    grid[position] = '#'
    
def set_weakened(grid, position):
    grid[position] = 'W'
    
def set_flagged(grid, position):
    grid[position] = 'F'

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
        
def turn_reverse(direction):
    return turn_right(turn_right(direction))

def main():
    grid = get_grid_from_file(FNAME)
    current_direction = (-1, 0)
    current_position = (0, 0)
    total_infections = 0
    for i in range(BURSTS):
        #print (current_position)
        if is_clean(grid, current_position):
            set_weakened(grid, current_position)
            current_direction = turn_left(current_direction)
            current_position = go(current_position, current_direction)
        elif is_weakened(grid, current_position):
            set_infected(grid, current_position)
            total_infections += 1
            current_position = go(current_position, current_direction)
        elif is_infected(grid, current_position):
            set_flagged(grid, current_position)
            current_direction = turn_right(current_direction)
            current_position = go(current_position, current_direction)
        elif is_flagged(grid, current_position):
            set_clean(grid, current_position)
            current_direction = turn_reverse(current_direction)
            current_position = go(current_position, current_direction)
        else:
            print ("this should not happend, 1")    
    
    print(total_infections)

if __name__ == "__main__":
    main()
