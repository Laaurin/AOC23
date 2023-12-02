

def s1():
    zeilen_array = []

    with open('testInput.txt', 'r') as file:
        for zeile in file:
            # Füge jede Zeile zum Array hinzu (strip entfernt führende und abschließende Leerzeichen und Zeilenumbrüche)
            zeilen_array.append(zeile.strip())
    solution = 0
    for line in zeilen_array:
        my_str = ""
        for i in range(len(line)):
            if line[i].isdigit():
                my_str += line[i]
                break
        for i in range(len(line)-1, 0, -1):
            if line[i].isdigit():
                my_str += line[i]
                break

        if len(my_str) == 1:
            my_str += my_str
        solution += int(my_str)
    # Gib das Array aus
    print(solution)


def s2():
    zeilen_array = []

    with open('testInput.txt', 'r') as file:
        for zeile in file:
            zeilen_array.append(zeile.strip())
    solution = 0
    for line in zeilen_array:
        num = find_numbers(line)
        solution += num
    print(solution)


def find_all_occurrences(main_string, substring):
    occurrences = []
    index = main_string.find(substring)

    while index != -1:
        occurrences.append(index)
        index = main_string.find(substring, index + 1)

    return occurrences

def find_numbers(line):
    words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
             "nine": "9"}
    numbers = {}

    for i in range(len(line)):
        if line[i].isdigit():
            numbers[i] = line[i]

    for word in words:
        occurrences = find_all_occurrences(line, word)
        for index in occurrences:
            if index != -1:
                numbers[index] = words[word]

    smallest = min(numbers, default=None)
    highest = max(numbers, default=None)
    print(numbers[smallest] + numbers[highest])
    return int(numbers[smallest] + numbers[highest])


s2()