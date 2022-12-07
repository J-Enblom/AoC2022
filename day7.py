import string

def input():
    with open('d7.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return lines


def part1(data):

    sizes = {}
    prev_dir = []
    current_dir = "/"
    for line in data:
        command = line.split()
        if command[1] == "cd":
            if command[2] == "..":
                current_dir = prev_dir.pop()
            elif command[2] == "/":
                prev_dir = []
                current_dir = "/"
            else:
                prev_dir.append(current_dir)
                current_dir = current_dir + "/" + command[2]
        elif command[0].isnumeric():
            if current_dir in sizes:
                sizes[current_dir] += int(command[0])
                
            else:
                sizes[current_dir] = int(command[0])
            for dir in prev_dir:
                    if dir in sizes:
                        sizes[dir] += int(command[0])
                    else:
                        sizes[dir] = int(command[0])
        
    sum = 0
    for value in sizes.values():
        if value <= 100000:
            sum += value
    print(sum)

def part2(data):
    sizes = {}
    prev_dir = []
    total_sum = 0
    current_dir = "/"
    for line in data:
        command = line.split()
        if command[1] == "cd":
            if command[2] == "..":
                current_dir = prev_dir.pop()
            elif command[2] == "/":
                prev_dir = []
                current_dir = "/"
            else:
                prev_dir.append(current_dir)
                current_dir = current_dir + "/" + command[2]
        elif command[0].isnumeric():
            if current_dir in sizes:
                sizes[current_dir] += int(command[0])
                
            else:
                sizes[current_dir] = int(command[0])
            for dir in prev_dir:
                    if dir in sizes:
                        sizes[dir] += int(command[0])
                    else:
                        sizes[dir] = int(command[0])
            total_sum += int(command[0])
    goal = 30000000 - (70000000 - total_sum)
    saved = []
    for value in sizes.values():
        if value > goal:
            saved.append(value)
    print(min(saved))
        
    

if __name__ == "__main__":
    data = input()
    part1(data)
    part2(data)