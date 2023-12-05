
def to_integer_list(list):
    numbers = []
    list = list.split()
    for num in list:
        numbers.append(int(num))
    return numbers


def scratch_card(lines, index, cards):
    cards[index] -= 1
    line = lines[index].split(':')
    nums = line[1].strip()
    winning_own = nums.split('|')
    winning_nums = winning_own[0].strip()
    winning_nums = to_integer_list(winning_nums)
    own_nums = winning_own[1].strip()
    own_nums = to_integer_list(own_nums)
    copy_index = index

    for num in own_nums:
        if num in winning_nums:
            copy_index += 1
            cards[copy_index] += 1

    return cards

def s2():
    lines = []
    with open('input.txt', 'r') as file:
        for zeile in file:
            lines.append(zeile.strip())

    cards = [1 for i in range(len(lines))]
    index = 0
    solution = 0
    while index < len(lines):
        solution += 1
        cards = scratch_card(lines, index, cards)
        if cards[index] == 0:
            index+=1
            print(index)
    print(solution)
def s1():
    lines = []
    with open('input.txt', 'r') as file:
        for zeile in file:
            lines.append(zeile.strip())

    solution = 0
    for line in lines:
        print("-----")
        line = line.split(':')
        nums = line[1].strip()
        winning_own = nums.split('|')
        winning_nums = winning_own[0].strip()
        winning_nums = to_integer_list(winning_nums)
        own_nums = winning_own[1].strip()
        own_nums = to_integer_list(own_nums)
        occurrences = 0
        for num in own_nums:
            if num in winning_nums:
                print(num)
                occurrences += 1
        if occurrences == 0:
            continue
        score = pow(2, occurrences-1)
        print(f"score: {score}")
        solution += score
    print(solution)

s2()
