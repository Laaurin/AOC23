def is_symbol(lines, x, y):
    if not lines[y][x].isdigit() and lines[y][x] != '.':
        return True
    return False


def check_adjacent(lines, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= y + i < len(lines) and 0 <= x + j < len(lines[y]):
                if is_symbol(lines, x+j, y+i):
                    return True
    return False

def get_number(lines, x, y):
    number = ""
    while x > 0 and lines[y][x-1].isdigit():
        x-=1
    while True:
        if lines[y][x].isdigit():
            number += lines[y][x]
        else:
            if number == "":
                return None
            return int(number)
        if x + 1 >= len(lines[y]):
            return int(number)
        x+=1

def get_numbers(lines, x, y):
    numbers = []
    for i in range(-1, 2):
        new_number = True
        for j in range(-1, 2):
            if i == 0 and j == 0:
                new_number = True
            if 0 <= y + i < len(lines) and 0 <= x + j < len(lines[y]):
                if lines[y+i][x+j] not in "1234567890":
                    new_number = True
                if lines[y+i][x+j].isdigit() and new_number:
                    numer = get_number(lines, x+j, y+i)
                    if numer is not None:
                        numbers.append(numer)
                    new_number = False
    return numbers
def s12():
    lines = []
    with open('input.txt', 'r') as file:
        for zeile in file:
            lines.append(zeile.strip())
    solution = 0
    signs = "0123456789."
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] not in signs:
                numbers = get_numbers(lines, j, i)
                for number in numbers:
                    if number is not None:
                        print(number)
                        solution += number
    print(solution)

def s2():
    lines = []
    with open('input.txt', 'r') as file:
        for zeile in file:
            lines.append(zeile.strip())
    solution = 0
    signs = "0123456789."
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '*':
                numbers = get_numbers(lines, j, i)
                if len(numbers) == 2:
                    solution += numbers[0] * numbers[1]
    print(solution)

def s1():
    lines = []
    with open('input.txt', 'r') as file:
        for zeile in file:
            lines.append(zeile.strip())
    solution = 0
    for i in range(len(lines)):
        #neue zeile -> alles zurücksetzen
        is_valid = False
        current_number = ""
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                current_number += lines[i][j]
                if check_adjacent(lines, j, i):
                    is_valid = True
            else:
                if is_valid:
                    print(current_number)
                    solution += int(current_number)
                    is_valid = False
                current_number = ""


    print(solution)


s2()


#too high 1487370704195
#too high  877132067926
#too low 527626
#        570376