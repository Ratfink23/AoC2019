
day2testdata = [1,3,6,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0]


def Intcode(memory):
    address = 0
    while True:
        if memory[address] == 1:
            memory[memory[address + 3]] = memory[memory[address + 1]] + memory[memory[address + 2]]
        elif memory[address] == 2:
            memory[memory[address + 3]] = memory[memory[address + 1]] * memory[memory[address + 2]]
        elif memory[address] == 99:
            return memory
        else:
            pass
        address += 4


for noun in range(0,100):
    for verb in range(0,100):
        new_list = [1,noun,verb,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0]
        if Intcode(new_list)[0] == 19690720:
            print(100*noun+verb)
            print(f'Noun: {noun} Verb: {verb}')
