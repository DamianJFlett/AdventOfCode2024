f = open("input.txt", "r")

file = [l for l in f]
program = file[4][9:-1].split(",")



class assembly():
    def __init__(self):
        self.A = int(file[0][12:-1])
        self.B = int(file[1][12:-1])
        self.C = int(file[2][12:-1])
        self.index = 0
        self.output = []
        self.program = [int(x) for x in file[4][9:-1].split(",")]
        self.instructions  = [int(x) for (i, x) in enumerate(self.program) if i % 2 == 0]
        self.inputs = [int(x) for (i, x) in enumerate(self.program) if i % 2 == 1]
    #opcode 0
    def adv(self, input):
        input = self.get_combo(input)
        self.A = self.A // 2 ** input
    #1
    def bxl(self, input):
        self.B = self.B ^ input
        
    #2
    def bst(self, input):
        input  = self.get_combo(input)
        self.B = input % 8

    #3
    def jnz(self, input):
        if self.A == 0:
            self.index += 1 
            return
        self.index = input // 2

    #4
    def bxc(self, input):
        self.B = self.B ^ self.C

    #5
    def out(self, input):
        input = self.get_combo(input)
        self.output.append(input % 8)

    #6
    def bdv(self, input):
        input = self.get_combo(input)
        self.B = self.A // 2 ** input

    #7
    def cdv(self, input):
        input = self.get_combo(input)
        self.C = self.A // 2 ** input

    def get_combo(self, input):
        if 0 <= input <= 3:
            return input
        if input == 4:
            return self.A  
        if input == 5:
            return self.B
        if input == 6:
            return self.C
        else:
            raise ValueError(input)                                                    

    def run(self):
        while self.index < len(self.instructions):
            opcode = self.instructions[self.index]
            input = self.inputs[self.index]
            if opcode == 0:
                self.adv(input)
            elif opcode == 1:
                self.bxl(input)
            elif opcode == 2:
                self.bst(input)
            elif opcode == 3:
                self.jnz(input)
            elif opcode == 4:
                self.bxc(input)
            elif opcode == 5:
                self.out(input)
            elif opcode ==6:
                self.bdv(input)
            elif opcode ==7:
                self.cdv(input)
            else:
                raise ValueError(opcode)
            if opcode != 3:
                self.index += 1
    
    def get_output(self):
        return self.output

    def aoc_output(self):
        returner = ""
        for i in self.output:
            returner += str(i)
            returner += ","
        return returner[:-1]

    def search_A(self):
        test = -1
        while self.program != self.output:
            test += 1
            self.A = test
            self.output = []
            self.index = 0
            self.run()
        return test

    
my_assembly = assembly()
print(my_assembly.instructions, my_assembly.inputs, my_assembly.A, my_assembly.B, my_assembly.C)
my_assembly.run()
print(my_assembly.aoc_output())

#part 2
new = assembly()
print("part 2 is", new.search_A())