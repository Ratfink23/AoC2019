
def clean_input():
    with open('Day6_input', 'r') as input:
        cleaned_data = []
        data = input.readlines()
        for orbit in data:
            cleaned_data.append(orbit.strip('\n').split(')'))
        return cleaned_data


def find_orbit_instances(orbit, orbit_list):
    all_orbits = []
    for i, orbit_pair in enumerate(orbit_list):
        if orbit_pair[0] == orbit:
            all_orbits.append(i)
    return all_orbits


def orbit_line(target='YOU'):
    tree = []
    while True:
        for orbx in cleaned_orbits:
            if orbx[1] == target:
                tree.append(orbx[0])
                target = orbx[0]
                if orbx[0] == 'COM':
                    return tree


cleaned_orbits = clean_input()
direct_orbits = len(cleaned_orbits)

orbit_distance = {}
orbit_distance['COM'] = 0

for x in range(1,1111):
    for orb in cleaned_orbits:
        if orb[0] in orbit_distance.keys():
            orbit_distance[orb[1]] = orbit_distance.get(orb[0]) + 1

count = 0
for val in orbit_distance:
    count += orbit_distance.get(val)
print(count)

you_tree = orbit_line('YOU')
san_tree = orbit_line('SAN')


def compare_trees(tree1,tree2):
    for x in tree1:
        for y in tree2:
            if y == x:
                return tree1.index(x), tree2.index(y)

print(compare_trees(you_tree,san_tree))