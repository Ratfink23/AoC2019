from itertools import permutations
from copy import deepcopy

data = list(map(int, open('Day7_input', 'r').read().split(',')))

def opcode_data(instruction):
    instruction = str(instruction).zfill(5)
    p3_mode = int(instruction[0])
    p2_mode = int(instruction[1])
    p1_mode = int(instruction[2])
    opcode = int(instruction[-2:])
    directions_list = [opcode, p1_mode, p2_mode, p3_mode]
    return directions_list


class Intcode:
    def __init__(self, memory, phase=0, input1=0, address=0):
        self.memory = memory
        self.phase = phase
        self.input1 = input1
        self.address = address
        self.stopped = False
        self.output = None

    def update_input(self, new_input):
        # Update phase and input to be new_input Day 7 Part2
        self.input1 = new_input

    def run(self):
        halt = False
        while not halt:
            directions = opcode_data(self.memory[self.address])
            opcode = directions[0]
            elements = []
            if opcode == 99:
                halt = True
                self.stopped = True
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
                # Input the phase first
                if self.phase is not None:
                    self.memory[elements[0]] = self.phase
                    self.phase = None
                else:
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


def amp_controller(data, start_input, phaseA, phaseB, phaseC, phaseD, phaseE):
    AmpA = Intcode(data, phase=phaseA, input1=start_input)
    AmpA.run()
    AmpB = Intcode(data, phase=phaseB, input1=AmpA.output)
    AmpB.run()
    AmpC = Intcode(data, phase=phaseC, input1=AmpB.output)
    AmpC.run()
    AmpD = Intcode(data, phase=phaseD, input1=AmpC.output)
    AmpD.run()
    AmpE = Intcode(data, phase=phaseE, input1=AmpD.output)
    AmpE.run()
    return AmpE.output


def amp_controller2(data, start_input, phaseA, phaseB, phaseC, phaseD, phaseE):
    # first round, startup
    AmpA = Intcode(data, phase=phaseA, input1=start_input)
    AmpA.run()
    AmpB = Intcode(data, phase=phaseB, input1=AmpA.output)
    AmpB.run()
    AmpC = Intcode(data, phase=phaseC, input1=AmpB.output)
    AmpC.run()
    AmpD = Intcode(data, phase=phaseD, input1=AmpC.output)
    AmpD.run()
    AmpE = Intcode(data, phase=phaseE, input1=AmpD.output)
    AmpE.run()
    while True:
        if AmpE.stopped is True:
            #return AmpE.output
            return AmpE.output
        else:
            AmpA.update_input(AmpE.output)
            AmpA.run()
            AmpB.update_input(AmpA.output)
            AmpB.run()
            AmpC.update_input(AmpB.output)
            AmpC.run()
            AmpD.update_input(AmpC.output)
            AmpD.run()
            AmpE.update_input(AmpD.output)
            AmpE.run()

def all_perm_array(start_input, option_list):
    perm = permutations(option_list)
    output = []
    for i in perm:
        output.append(amp_controller(data, start_input, i[0], i[1], i[2], i[3], i[4]))
    return output

def all_perm_array2(start_input, option_list):
    perm = permutations(option_list)
    output = []
    for i in perm:
        output.append(amp_controller2(testdata4, start_input, i[0], i[1], i[2], i[3], i[4]))
    return output

#Day7 part 1
testdata1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
print(f'Day 7 Part 1 Test 1: {amp_controller(testdata1, 0, 4, 3, 2, 1, 0)}')

testdata2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
print(f'Day 7 Part 1 Test 2: {amp_controller(testdata2, 0, 0, 1, 2, 3, 4)}')

testdata3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
print(f'Day 7 Part 1 Test 3: {amp_controller(testdata3, 0, 1, 0, 4, 3, 2)}')

thrusts = all_perm_array(0, [0, 1, 2, 3, 4])
print(f'Day 7 Part 1: {max(thrusts)}')

testdata4 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
print(f'Day 7 Part 2 Test 1: {amp_controller2(testdata4, 0, 9, 7, 7, 5, 6)}')

# Day 7 Part 2 not working. Need to visit.