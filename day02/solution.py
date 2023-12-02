def s1():
    colors = {
        "red": 12,
        "green": 13,
        "blue": 14

    }
    lines = []
    solution = 0

    with open('input.txt', 'r') as file:
        for zeile in file:
            lines.append(zeile.strip())

    for line in lines:
        line = line.strip()
        a = line.split(':')
        id = int(a[0].split(' ')[1])
        pulls = a[1].split(';')
        valid = True
        for pull in pulls:
            pull = pull.strip()
            cube_amounts = pull.split(',')
            for cube_amount in cube_amounts:
                cube_amount = cube_amount.strip()
                temp = cube_amount.split(' ')
                amount = int(temp[0])
                color = temp[1]
                if amount > colors[color]:
                    valid = False
                    break

        if valid:
            print(id)
            solution += int(id)

    print(solution)

def s2():
    lines = []
    solution = 0

    with open('input.txt', 'r') as file:
        for zeile in file:
            lines.append(zeile.strip())

    for line in lines:
        colors = {
            "red": 0,
            "green": 0,
            "blue": 0

        }
        line = line.strip()
        a = line.split(':')
        id = int(a[0].split(' ')[1])
        pulls = a[1].split(';')
        for pull in pulls:
            pull = pull.strip()
            cube_amounts = pull.split(',')
            for cube_amount in cube_amounts:
                cube_amount = cube_amount.strip()
                temp = cube_amount.split(' ')
                amount = int(temp[0])
                color = temp[1]
                if amount > colors[color]:
                    colors[color] = int(amount)

        power = 1
        for key in colors:
            power *= colors[key]
        solution += power
    print(solution)
s1()