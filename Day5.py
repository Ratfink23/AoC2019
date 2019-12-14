def opcode_data(instruction):
    instruction = str(instruction).zfill(5)
    p3_mode = int(instruction[0])
    p2_mode = int(instruction[1])
    p1_mode = int(instruction[2])
    opcode = int(instruction[-2:])
    directions_list = [opcode, p1_mode, p2_mode, p3_mode]
    return directions_list


class Intcode:
    def __init__(self, memory, input1=0, address=0):
        self.memory = memory
        self.input1 = input1
        self.address = address
        self.output = None

    def run(self):
        halt = False
        while not halt:
            directions = opcode_data(self.memory[self.address])
            opcode = directions[0]
            elements = []
            if opcode == 99:
                halt = True
            for i in range(1, 4):
                if directions[i] == 0:
                    elements.append(self.memory[self.address+i])
                else:
                    elements.append(self.address + i)
            if opcode == 1:
                # Add
                self.memory[elements[2]] = self.memory[elements[0]] + self.memory[elements[1]]
                self.address += 4
            elif opcode == 2:
                # Multiply
                self.memory[elements[2]] = self.memory[elements[0]] * self.memory[elements[1]]
                self.address += 4
            elif opcode == 3:
                # Insert
                self.memory[elements[0]] = self.input1
                self.address += 2
            elif opcode == 4:
                # Output
                self.address += 2
                self.output = self.memory[elements[0]]
                halt = True
            elif opcode == 5:
                # jump-if-true
                if self.memory[elements[0]] != 0:
                    self.address = self.memory[elements[1]]
                else:
                    self.address += 3
            elif opcode == 6:
                # jump-if-false
                if self.memory[elements[0]] == 0:
                    self.address = self.memory[elements[1]]
                else:
                    self.address += 3
            elif opcode == 7:
                # less than
                if self.memory[elements[0]] < self.memory[elements[1]]:
                    self.memory[elements[2]] = 1
                else:
                    self.memory[elements[2]] = 0
                self.address += 4
            elif opcode == 8:
                # equals
                if self.memory[elements[0]] == self.memory[elements[1]]:
                    self.memory[elements[2]] = 1
                else:
                    self.memory[elements[2]] = 0
                self.address += 4
            else:
                pass


data = list(map(int, open('Day5_input', 'r').read().split(',')))

Day5 = Intcode(data, input1=5)
Day5.run()
print(Day5.output)