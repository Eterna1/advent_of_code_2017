#!/usr/bin/python3
file_input = "input.txt"

import queue
        
class Instruction:
    def __init__(self, op, reg, val):
        self.op = op
        self.reg = reg
        self.val = val

class CPU:
    
    operations = {}
    operations['set'] = lambda a, b : b
    operations['mul'] = lambda a, b : a * b
    operations['add'] = lambda a, b : a + b
    operations['mod'] = lambda a, b : a % b
    
    def reset(self):
        self.registers = {'p': self.cpu_id}
        self.queue = queue.Queue()
        self.sent_values_count = 0
        self.pc = 0
    
    def __init__(self, instructions, cpu_id, the_other_cpu = None):
        self.instructions = instructions
        self.cpu_id = cpu_id
        self.the_other_cpu = the_other_cpu
        self.reset()
    
    def eval(self, w):
        if w.isalpha():
            return self.registers.get(w, 0)
        else:
            return int(w)
        
    def execute(self):
        """
        It returns False on rcv instruction and the queue is empty
        Otherwise True is returned
        """
        
        if self.pc >= len(self.instructions):
            return False
        
        instr = self.instructions[self.pc]
        
        if instr.op in self.operations:
            op = self.operations[instr.op]
            self.registers[instr.reg] = op(self.eval(instr.reg), self.eval(instr.val))
            self.pc += 1
        elif instr.op == "jgz":
            if self.eval(instr.reg) > 0:
                self.pc += self.eval(instr.val)
            else:
                self.pc += 1
                
        elif instr.op == "rcv":
            if not self.queue.empty():
                self.registers[instr.reg] = self.queue.get()
                self.pc += 1
            else:
                return False
            
        elif instr.op == "snd":
            self.the_other_cpu.queue.put(self.eval(instr.reg))
            self.sent_values_count += 1
            self.pc += 1
        else:
            print ("that instruction is not implemented")
            exit()
        return True

            
        
def parse_instruction(str):
    try:
        (op, reg, val) = str.split() #should be without ( and ) because of the convention. meh. for me the code is more readable with them.
    except ValueError:
        (op, reg) = str.split()
        val = None
    return Instruction(op, reg, val)
    
        
def main():
    instructions = []
    with open(file_input, 'r') as f:
        for line in f:
            instr = parse_instruction(line)
            instructions.append(instr)
    
    cpu0 = CPU(instructions, 0)
    cpu1 = CPU(instructions, 1, cpu0)
    cpu0.the_other_cpu = cpu1
    
    a = True
    b = True
    while a or b:
        a = cpu0.execute()
        b = cpu1.execute()
    print (cpu1.sent_values_count)
    
if __name__ == "__main__":
    main()
