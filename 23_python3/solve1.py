#!/usr/bin/python3
  
file_input = "input.txt"

        
class Instruction:
    def __init__(self, op, reg, val):
        self.op = op
        self.reg = reg
        self.val = val

class CPU:
    
    operations = {}
    operations['set'] = lambda a, b : b
    #operations['mul'] = lambda a, b : a * b
    operations['add'] = lambda a, b : a + b
    operations['sub'] = lambda a, b : a - b
    operations['mod'] = lambda a, b : a % b
    
    def reset(self):
        self.registers = {}
        self.mul_invoked_count = 0
    
    def __init__(self, instructions = []):
        self.reset()
        self.instructions = instructions
    
    def eval(self, w):
        if w.isalpha():
            return self.registers.get(w, 0)
        else:
            return int(w)
        
    def execute(self):
        
        self.pc = 0
        
        while self.pc < len(self.instructions):
            instr = self.instructions[self.pc]
            
            if instr.op in self.operations:
                op = self.operations[instr.op]
                self.registers[instr.reg] = op(self.eval(instr.reg), self.eval(instr.val))
                self.pc += 1
            elif instr.op == "mul":
                self.registers[instr.reg] = (self.eval(instr.reg) * self.eval(instr.val))
                self.mul_invoked_count += 1
                self.pc += 1
                
            elif instr.op == "jnz":
                if self.eval(instr.reg) != 0:
                    self.pc += self.eval(instr.val)
                else:
                    self.pc += 1
                
            else:
                print ("that instruction is not implemented")
                exit()
            
        
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
    
    cpu = CPU(instructions)  
    cpu.execute()
    print(cpu.mul_invoked_count)
    
if __name__ == "__main__":
    main()
 
