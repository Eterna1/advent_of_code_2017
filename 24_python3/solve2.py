#!/usr/bin/python3
  
file_input = "input.txt"

pins = {} #dictionary containing pins
ports = {} #dictionary of various ports. it contains a list of names of pins with these ports
bridge = []
match_port = []
      
def add_pin(pin):
    if pin in pins:
        print ("all pins must be unique")
        exit(1)
    pins[pin] = "not_taken"            

def add_port(port, pin):
    ports[port] = ports.get(port, [])
    ports[port].append(pin)

def pin_strength(pin):
    return pin[0] + pin[1]

def other_port(pin, port):
    if pin[0] == port:
        return pin[1]
    else:
        return pin[0]

def bridge_points(bridge):
    points = 0
    for pin in bridge:
        points += pin[0] + pin[1]
    return points

def brut_longest_bridge():
    global match_port
    
    port_to_match = match_port[-1]
    pins_to_match = ports[port_to_match]
    
    longest_bridge = 0
    
    for pin in pins_to_match:
        if pins[pin] == "taken":
            continue
        pins[pin] = "taken"
        match_port.append(other_port(pin, port_to_match))
        
        bridge_length = 1 + brut_longest_bridge() 
        if bridge_length > longest_bridge:
            longest_bridge = bridge_length
            
        
        match_port.pop()
        pins[pin] = "not_taken"
    
    return longest_bridge
    

def brut_strongest_of_length(current_length, length):
    global match_port
    global bridge
    
    if current_length == length:
        return bridge_points(bridge)
    
    port_to_match = match_port[-1]
    pins_to_match = ports[port_to_match]
    
    strongest_bridge = 0
    
    for pin in pins_to_match:
        if pins[pin] == "taken":
            continue
        pins[pin] = "taken"
        match_port.append(other_port(pin, port_to_match))
        bridge.append(pin)
        
        bridge_strength = brut_strongest_of_length(current_length+1, length) 
        if bridge_strength > strongest_bridge:
            strongest_bridge = bridge_strength
            
        
        bridge.pop()
        match_port.pop()
        pins[pin] = "not_taken"
    
    return strongest_bridge
        
            
def main():
    global match_port
    
    with open(file_input, 'r') as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            pin = line.split("/")
            (a, b) = tuple(map(int, pin))
            pin = tuple(sorted((a,b)))
            #print(pin)
            add_pin(pin)
            add_port(a, pin)
            add_port(b, pin)
    
    #print ports        
    match_port = [0]
    longest_bridge = brut_longest_bridge()
    print ("longest bridge has %s length" % longest_bridge)
    strongest_bridge = brut_strongest_of_length(0, longest_bridge)
    print ("strongest bridge of the longests one has %s points" % strongest_bridge)
    
if __name__ == "__main__":
    main()
 
 
