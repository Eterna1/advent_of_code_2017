#!/usr/bin/python3
  
file_input = "input.txt"

pins = {} #dictionary containing pins
ports = {} #dictionary of various ports. it contains a list of names of pins with these ports
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

def brut():
    global match_port
    
    port_to_match = match_port[-1]
    pins_to_match = ports[port_to_match]
    
    strongest_bridge = 0
    
    for pin in pins_to_match:
        if pins[pin] == "taken":
            continue
        pins[pin] = "taken"
        match_port.append(other_port(pin, port_to_match))
        
        bridge_strength = pin_strength(pin) + brut() 
        if bridge_strength > strongest_bridge:
            strongest_bridge = bridge_strength
        
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
    strongest_bridge = brut()
    print ("the points of the strongest_bridge is %s" % strongest_bridge)
    
    
if __name__ == "__main__":
    main()
 
 
