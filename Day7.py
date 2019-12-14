from itertools import permutations

data = list(map(int, open('Day7_input', 'r').read().split(',')))

def opcode_data(instruction):
    instruction = str(instruction).zfill(5)
    p3_mode = int(instruction[0])
    p2_mode = int(instruction[1])
    p1_mode = int(instruction[2])
    opcode = int(instruction[-2:])
    directions_list = [opcode, p1_mode, p2_mode, p3_mode]
    return directions_list


def Intcode(memory, input1=0, input2=0, address=0):
    while True:
        directions = opcode_data(memory[address])
        opcode = directions[0]
        elements = []
        if opcode == 99:
            print('Halt')
            print(address)
            return memory[elements[0]], address
        for i in range(1, 4):
            if directions[i] == 0:
                elements.append(memory[address+i])
            else:
                elements.append(address + i)
        if opcode == 1:
            memory[elements[2]] = memory[elements[0]] + memory[elements[1]]
            address += 4
        elif opcode == 2:
            memory[elements[2]] = memory[elements[0]] * memory[elements[1]]
            address += 4
        elif opcode == 3:
            memory[elements[0]] = input1
            input1 = input2
            address += 2
        elif opcode == 4:
            address += 2
            return memory[elements[0]], address
        elif opcode == 5:
            # jump-if-true
            if memory[elements[0]] != 0:
                address = memory[elements[1]]
            else:
                address += 3
        elif opcode == 6:
            # jump-if-false
            if memory[elements[0]] == 0:
                address = memory[elements[1]]
            else:
                address += 3
        elif opcode == 7:
            # less than
            if memory[elements[0]] < memory[elements[1]]:
                memory[elements[2]] = 1
            else:
                memory[elements[2]] = 0
            address += 4
        elif opcode == 8:
            # equals
            if memory[elements[0]] == memory[elements[1]]:
                memory[elements[2]] = 1
            else:
                memory[elements[2]] = 0
            address += 4
        else:
            pass


class Incode2:
    def __init__(self, memory, input1=0, input2=0, address=0):
        self.memory = memory
        self.input1 = input1
        self.input2 = input2
        self.address = address

    def run(self):
        while True:
            directions = opcode_data(self.memory[self.address])
            opcode = directions[0]
            elements = []
            if opcode == 99:
                print('Halt')
                return self.memory[elements[0]], self.address
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
                self.input1 = self.input2
                self.address += 2
            elif opcode == 4:
                # Output
                self.address += 2
                return self.memory[elements[0]], self.address
            elif opcode == 5:
                # jump-if-true
                if self.memory[elements[0]] != 0:
                    address = memory[elements[1]]
                else:
                    address += 3
            elif opcode == 6:
                # jump-if-false
                if memory[elements[0]] == 0:
                    address = memory[elements[1]]
                else:
                    address += 3
            elif opcode == 7:
                # less than
                if memory[elements[0]] < memory[elements[1]]:
                    memory[elements[2]] = 1
                else:
                    memory[elements[2]] = 0
                address += 4
            elif opcode == 8:
                # equals
                if memory[elements[0]] == memory[elements[1]]:
                    memory[elements[2]] = 1
                else:
                    memory[elements[2]] = 0
                address += 4
            else:
                pass




def amp_arrange(data, start_input, inputA, inputB, inputC, inputD, inputE):
    AmpA = Intcode(data, input1=inputA, input2=start_input)
    AmpB = Intcode(data, input1=inputB, input2=AmpA[0])
    AmpC = Intcode(data, input1=inputC, input2=AmpB[0])
    AmpD = Intcode(data, input1=inputD, input2=AmpC[0])
    AmpE = Intcode(data, input1=inputE, input2=AmpD[0])
    return AmpE


def amp_arrange2(data, start_input, inputA, inputB, inputC, inputD, inputE, address):
    address_A, address_B, address_C, address_D, address_E = address
    AmpA, address_A = Intcode(data, input1=inputA, input2=start_input, address=address_A)
    print(AmpA, address_A)
    AmpB, address_B = Intcode(data, input1=inputB, input2=AmpA, address=address_B)
    print(AmpB, address_B)
    AmpC, address_C = Intcode(data, input1=inputC, input2=AmpB, address=address_C)
    print(AmpC, address_C)
    AmpD, address_D = Intcode(data, input1=inputD, input2=AmpC, address=address_D)
    print(AmpD, address_D)
    AmpE, address_E = Intcode(data, input1=inputE, input2=AmpD, address=address_E)
    print(AmpE, address_E)
    address_return = [address_A, address_B, address_C, address_D, address_E]
    print(address_return)
    return AmpE, address_return

def all_perm_array(option_list):
    perm = permutations(option_list[1:])
    output = []
    for i in perm:
        output.append(amp_arrange(data, option_list[0], i[0], i[1], i[2], i[3], i[4]))
    return output


# Day7 part 1
# thrusts = all_perm_array([0, 0, 1, 2, 3, 4])
#print(max(thrusts))

input = 0
address = [0,0,0,0,0]
phase = [input, address]

for x in range(1,30):
    print(phase[1])
    phase = amp_arrange2(data, phase[0], 9, 8, 7, 6, 5, phase[1])
    #print(phase)
