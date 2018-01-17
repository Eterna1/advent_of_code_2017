#!/usr/bin/python3
#this script runs for ~20 minutes on my laptop. it was enough for me 
  
file_input = "input.txt"

        
class Instruction:
    def __init__(self, op, reg, val, str):
        self.op = op
        self.reg = reg
        self.val = val
        self.str = str

class CPU:
    
    operations = {}
    operations['set'] = lambda a, b : b
    #operations['mul'] = lambda a, b : a * b
    operations['add'] = lambda a, b : a + b
    operations['sub'] = lambda a, b : a - b
    operations['mod'] = lambda a, b : a % b
    
    def reset(self):
        self.registers = {'a':1}
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
            #print (instr.str)
            if instr.str == "sub e -1":
                #optimization on this instruction
                b = self.registers['b']
                d = self.registers['d']
                self.registers['e'] = self.registers['b'] - 1
                #check whether f has ever been equal to 0 in this loop
                if b == 0 and d == 0:
                    self.registers['f'] = 0
                if (b % d == 0) and 2<=(b / d)<=b:
                    self.registers['f'] = 0
            if instr.str == "sub g c":
                print ("g="+str(self.registers['g']))
                print ("c="+str(self.registers['c']))

            if instr.str == "jnz 1 -23":
                print ("**************************")
                print ("h="+str(self.registers['h']))
                #exit(0)
            
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
    str = str.strip()
    try:
        (op, reg, val) = str.split() #should be without ( and ) because of the convention. meh. for me the code is more readable with them.
    except ValueError:
        (op, reg) = str.split()
        val = None
    return Instruction(op, reg, val, str)
    
        
def main():
    instructions = []
    with open(file_input, 'r') as f:
        for line in f:
            instr = parse_instruction(line)
            instructions.append(instr)
    
    cpu = CPU(instructions)  
    cpu.execute()
    print(cpu.registers['h'])
    
if __name__ == "__main__":
    main()
 
