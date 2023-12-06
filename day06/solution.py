def s1():
    lines = []
    with open('input.txt', 'r') as file:
        for zeile in file:
            lines.append(zeile.strip())

    times = [int(i.strip()) for i in lines[0].split(':')[1].strip().split()]
    distances = [int(i.strip()) for i in lines[1].split(':')[1].strip().split()]
    print(times)
    solution = 1
    for i in range(len(times)):
        amount = 0
        wrong_count = 0
        for j in range(1, times[i], 1):
            #print(f"holding for {j}ms: the boat will travel {j}mm/ms * {times[i]-j}ms = {j*(times[i]-j)}mm and {distances[i]} is required")
            if j * (times[i] - j) > distances[i]:
                break
            else:
                wrong_count += 1
        amount = times[i]-1 - wrong_count*2
        if amount > 0:
            print(amount)
            solution *= amount
    print(solution)
s1()
