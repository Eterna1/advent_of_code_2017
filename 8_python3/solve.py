#!/usr/bin/python3
  
file_input = "input.txt"

class Condition:
    
    conditions = {}
    conditions['<'] = lambda a, b: a < b
    conditions['>'] = lambda a, b: a > b
    conditions['<='] = lambda a, b: a <= b
    conditions['>='] = lambda a, b: a >= b
    conditions['=='] = lambda a, b: a == b
    conditions['!='] = lambda a, b: a != b
    
    def __init__(self, reg, cond_op, val):
        self.reg = reg
        self.val = val
        self.cond_op = cond_op
    def is_true(self, registers):
        print (self.cond_op, self.reg, self.val)
        return self.conditions[self.cond_op](registers.get(self.reg,0), self.val)
        
class Instruction:
    def __init__(self, reg, op, val, condition):
        self.reg = reg
        self.op = op
        self.val = val
        self.condition = condition

class CPU:
    
    operations = {}
    operations['dec'] = lambda a, b : a - b
    operations['inc'] = lambda a, b : a + b
    
    def __init__(self):
        self.registers = {}
        self.max_even_held = -float("inf") #nice trick
        
    def execute(self, instr):
        """
        instr -- instance of Instruction
        """
        if instr.condition.is_true(self.registers):
            print ("cond is true")
            op = self.operations[instr.op]
            self.registers[instr.reg] = op(self.registers.get(instr.reg, 0), instr.val)
            if self.registers[instr.reg] > self.max_even_held:
                self.max_even_held = self.registers[instr.reg]
        else:
            print ("cond is false")
            
    def find_largest_reg_value(self):
        return max(self.registers.values()) # nice trick

def parse_condition(str):
    (a, cond_op, b) = str.split()
    return Condition(a, cond_op, int(b))
        
def parse_instruction(str):
    cond_str = str.split('if')[1]
    condition = parse_condition(cond_str)
    
    (reg, op, val) = str.split('if')[0].split()
    return Instruction(reg, op, int(val), condition)
    
        
def main():
    cpu = CPU()
    with open(file_input, 'r') as f:
        for line in f:
            instr = parse_instruction(line)
            cpu.execute(instr)
    print (cpu.find_largest_reg_value())
    print (cpu.max_even_held)
if __name__ == "__main__":
    main()
