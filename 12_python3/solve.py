#!/usr/bin/python3

def parse():
    
    pipes = {}
    
    try:
        while True:
            line = input()
            if not line.strip():
                break
            #print(line)
            (pipe, connections) = line.split(" <-> ")
            pipe = int(pipe)
            connections = list(map(lambda x: int(x.strip()), connections.split(",")))
            
            pipes[pipe] = connections
            
    except EOFError:
        pass
    return pipes

def connected_to(pipes, pipe_id):
    
    stack = [pipe_id]
    pipes_connected = set()
    pipes_visited = set()
    
    while stack:
        visiting = stack.pop()
        if visiting in pipes_visited:
            continue
        
        pipes_visited.add(visiting)
        
        pipes_connected.add(visiting)
        
        for connected in pipes[visiting]:
            stack.append(connected)
    
    return pipes_connected

def count_groups(pipes):
    
    pipes_visited = set()
    groups = 0
    for visiting in pipes.keys():
        if not visiting in pipes_visited:
            groups += 1
            pipes_visited |= connected_to(pipes, visiting) # or set.union
            #print (connected_to(pipes, visiting))
    return groups

if __name__ == "__main__":
    pipes = parse()
    connected = len(connected_to(pipes,0))
    groups = count_groups(pipes)
    print (connected, groups)
