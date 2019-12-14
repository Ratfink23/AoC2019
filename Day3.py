import csv

testset1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
testset2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

def wire_path(path):
    path_set = {(0,0)}
    pos_x = 0
    pos_y = 0
    for command in path:
        dir_x, dir_y = directions[command[0]]
        steps = int(command[1:])
        for step in range(steps):
            pos_x += dir_x
            pos_y += dir_y
            path_set.add((pos_x , pos_y))
    return path_set


def wire_distance(path, pos):
    pos_x = 0
    pos_y = 0
    total_steps = 0
    for command in path:
        dir_x, dir_y = directions[command[0]]
        steps = int(command[1:])
        for step in range(steps):
            pos_x += dir_x
            pos_y += dir_y
            total_steps += 1
            if (pos_x,pos_y) == pos:
                return total_steps


def union_distance(set1,set2):
    z = wire_path(set1).intersection(wire_path(set2))
    z.discard((0,0))
    distance = 10000000
    for xy in z:
        x,y = xy
        val = abs(x) + abs(y)
        if val < distance:
            distance = val
    return distance


def union_distance_step(set1,set2):
    z = wire_path(set1).intersection(wire_path(set2))
    z.discard((0,0))
    distance = 10000000
    for xy in z:
        val = wire_distance(set1,xy) + wire_distance(set2,xy)
        if val < distance:
            distance = val
    return distance


def data_import():
    with open("day3_input.txt", 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    print(union_distance_step(data[0],data[1]))


#print(union_distance_step(testset1,testset2))
data_import()
