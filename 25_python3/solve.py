#!/usr/bin/python3

import re

def main():
    
    beg_state = None
    steps_to_checksum = None
    parsing_state = None
    parsing_value = None
    
    procedures = {}
    
    #parse file to get procedures
    with open("input.txt") as f:
        for line in f:
            if "Begin in state " in line: #pomidor
                beg_state = re.findall(r'Begin in state ([A-Z]+)',line)[0]
            if "diagnostic checksum" in line:
                steps_to_checksum = int(re.findall(r'checksum after ([0-9]+) steps',line)[0])
            if "In state" in line:
                parsing_state = re.findall(r'In state ([A-Z]+):',line)[0]
                procedures[parsing_state] = procedures.get(parsing_state, {})
            if "If the current value" in line:
                parsing_value = int(re.findall(r'If the current value is ([0-9]+):',line)[0])
                procedures[parsing_state][parsing_value] = []
            if "Write the value" in line:
                val = int(re.findall(r'Write the value ([0-9]+).',line)[0])
                procedures[parsing_state][parsing_value].append(val)
            if "Move one slot" in line:
                move = re.findall(r'Move one slot to the ([a-z]+).',line)[0]
                procedures[parsing_state][parsing_value].append(move)
            if "Continue with state" in line:
                next_state = re.findall(r'Continue with state ([A-Z]+).',line)[0]
                procedures[parsing_state][parsing_value].append(next_state)
    
    #prepare the turing machinr
    
    tape = {}
    current_tape_pos = 0
    current_state = beg_state
    
    #run the turing machine
    
    for i in range(steps_to_checksum):
        current_value = tape.get(current_tape_pos, 0)
        (val, move, next_state) = procedures[current_state][current_value]            
        
        tape[current_tape_pos] = val
        if move == "right":
            current_tape_pos += 1
        elif move == "left":
            current_tape_pos -= 1
        current_state = next_state
        
    print (list(tape.values()).count(1))

if __name__ == "__main__":
    main() 
