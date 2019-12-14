def opcode_data(instruction):
    instruction = str(instruction).zfill(5)
    p3_mode = int(instruction[0])
    p2_mode = int(instruction[1])
    p1_mode = int(instruction[2])
    opcode = int(instruction[-2:])
    directions_list = [opcode, p1_mode, p2_mode, p3_mode]
    return directions_list

def Intcode(memory, input=1):
    address = 0
    while True:
        directions = opcode_data(memory[address])
        opcode = directions[0]
        elements = []
        if opcode == 99: return memory
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
            memory[elements[0]] = input
            address += 2
        elif opcode == 4:
            print(memory[elements[0]])
            address += 2
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

data = list(map(int, open('Day5_input', 'r').read().split(',')))
print(data)

Intcode(data, input=5)