from collections import Counter

data = list(map(int, open('Day8_input', 'r').read()))

def lowest_zero_count(split_list, test=False):
    # finds the split number of a string with the lowest count of Zero's
    #split_list = split_the_string(input_list, split)
    output_layer = 0
    lowest_zero = 1000
    for x, layer in enumerate(split_list):
        n = Counter(layer)
        if test: print(f'Layer {x}: Zero {n[0]} One {n[1]} Two {n[2]} : {n[0]+n[1]+n[2]}')
        if n[0] < lowest_zero:
            lowest_zero = n[0]
            output_layer = x
    return output_layer


def split_the_string(input_list, split):
    # splits the input list into split pieces
    start_pointer = 0
    output_list = []
    split_count = int(len(input_list) / split)
    for layer in range(1, split_count+1):
        new_list = input_list[start_pointer:start_pointer+split]
        output_list.append(new_list)
        start_pointer += split
    return output_list


# look at pos[0] on each layer - first layer with 0 or 1 goes into the input
def layer_map(layer_list, split):
    layer_num = len(layer_list)
    layer_len = len(layer_list[0])
    # default out is layer 1
    outlayer = layer_list[0]
    for pos in range(0, layer_len):
        for layer in range(1,layer_num):
            if outlayer[pos] == 2:
                outlayer[pos] = layer_list[layer][pos]
    outlayer = split_the_string(outlayer, split)
    return outlayer


# Day 8 Part 1
split_list = split_the_string(data, (25*6))
zerolayer = lowest_zero_count(split_list)
layer_offset = zerolayer*(25*6)
best = Counter(data[0+layer_offset:150+layer_offset])
print(f'Lowest Zero Layer {zerolayer}: Zero {best[0]} One {best[1]} Two {best[2]}')
print(f'Day 8 Part 1: {best[1]*best[2]}')

# Day 8 Part 2
split_list2 = split_the_string(data, (25*6))
stacked_layer = layer_map(split_list2,25)
print('Day 8 Part 2:')
for row in stacked_layer:
    print(row)
