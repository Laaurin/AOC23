def convert(map, number):
    for set in map:
        if set[1] <= number < set[1] + set[2]:
            return number + (set[0] - set[1])
    return number
def convert_ranges(map, seeds):
    if map == [[88, 18, 7], [18, 25, 70]]:
        a = 1
    ranges = []
    for map_set in map:
        seed_start = seeds[0]
        seed_range = seeds[1]
        seed_end = seed_start + seed_range - 1

        input_start = map_set[1]
        destination_start = map_set[0]

        map_range = map_set[2]
        map_end = input_start + map_range - 1

        if input_start <= seed_start <= map_end:
            new_seed_start = seed_start + (destination_start - input_start)
            #seed range kann komplett converted werden
            if seed_end <= map_end:
                ranges.append([new_seed_start, seed_range])
                return ranges

            else:
                new_seed_range = map_end - seed_start + 1
                ranges.append([new_seed_start, new_seed_range])
                other = convert_ranges(map, [map_end + 1, seed_range - new_seed_range])
                for i in other:
                    ranges.append(i)
                return ranges
    return [seeds]

def simplify_ranges(seed_ranges):
    seed_ranges = sorted(seed_ranges)
    current_index = 0
    next_index = 1
    while next_index < len(seed_ranges):
        current_range = seed_ranges[current_index]
        follow_range = seed_ranges[next_index]
        if current_range[0] + current_range[1] - 1 < follow_range[0]:
            current_index += 1
            next_index += 1
            continue

        range_end = follow_range[0] + max(current_range[0] + current_range[1] - 1 - follow_range[0],
                                          follow_range[1])
        current_range[1] = range_end - current_range[0]
        seed_ranges.pop(next_index)
        print("updated range: ", current_range)
    return seed_ranges

def s1():
    lines = []
    with open('input.txt', 'r') as file:
        for zeile in file:
            lines.append(zeile.strip())

    seeds = [int(i) for i in lines[0].split(':')[1].strip().split(' ')]
    lines.pop(0)
    lines.pop(0)

    maps = []
    map_index = 0
    for line in lines:
        if line == '':
            map_index += 1
        elif not line[0].isdigit():
            maps.append([])
        elif line[0].isdigit():
            maps[map_index].append([int(i) for i in line.split()])
    solutions = []
    for seed in seeds:
        print("seed: ", seed)
        num = seed
        for mmap in maps:
            num = convert(mmap, num)
            print(num)
        solutions.append(num)

    print(min(solutions))

def s2():
    lines = []
    with open('input.txt', 'r') as file:
        for zeile in file:
            lines.append(zeile.strip())

    seeds = [int(i) for i in lines[0].split(':')[1].strip().split(' ')]
    lines.pop(0)
    lines.pop(0)
    seed_ranges = [[seeds[i], seeds[i + 1]] for i in range(0, len(seeds), 2)]
    maps = []
    map_index = 0
    for line in lines:
        if line == '':
            map_index += 1
        elif not line[0].isdigit():
            maps.append([])
        elif line[0].isdigit():
            maps[map_index].append([int(i) for i in line.split()])
    solutions = []
    for i in range(len(maps)):
        current_map = maps[i]
        if current_map == [[88, 18, 7], [18, 25, 70]]:
            a = 1
        #seed_ranges = sorted(seed_ranges)
        print(seed_ranges)
        copy = []
        for j in range(len(seed_ranges)):
            current_range = seed_ranges[j]
            new_ranges = convert_ranges(current_map, current_range)
            for new_range in new_ranges:
                copy.append(new_range)
        seed_ranges = copy
        #print(simplify_ranges(seed_ranges))

    print(simplify_ranges(seed_ranges))

s2()
