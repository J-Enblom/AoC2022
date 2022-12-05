import re
import string

def input():
    with open('d5.txt', 'r') as file:
        text = file.read().split("\n\n")
    return text


def part1():
    data = input()
    positions = list(reversed(data[0].split("\n")))
    moves = data[1].split("\n")
    crates = []
    for row in positions[1:]:
        for i in range(len(row)):
            if row[i] in string.ascii_uppercase:
                crates.append([i, row[i]])
    positions = positions[0]
    new_crates = []
    for i in range(len(positions)):
        if positions[i] in string.digits:
            new_crates.append([])
            for crate in crates:
                if crate[0] == i:
                    new_crates[-1].append(crate[1])

    i = []
    for move in moves:
        i.append([int(n) for n in re.findall(r'\d+', move)])
    print(i)
    for move in i:
        for i in range(move[0]):
            to_move = new_crates[move[1] - 1].pop()
            new_crates[move[2] - 1].append(to_move)
    str = ""
    for column in new_crates:
        str += (column[-1])

    print(str)
    
def part2():
    data = input()
    positions = list(reversed(data[0].split("\n")))
    moves = data[1].split("\n")
    crates = []
    for row in positions[1:]:
        for i in range(len(row)):
            if row[i] in string.ascii_uppercase:
                crates.append([i, row[i]])
    positions = positions[0]
    new_crates = []
    for i in range(len(positions)):
        if positions[i] in string.digits:
            new_crates.append([])
            for crate in crates:
                if crate[0] == i:
                    new_crates[-1].append(crate[1])

    i = []
    for move in moves:
        i.append([int(n) for n in re.findall(r'\d+', move)])
    print(i)
    for move in i:
        if move[0] == 1:
            to_move = new_crates[move[1] - 1].pop()
            new_crates[move[2] - 1].append(to_move)
        else:
            to_move = []
            for i in range(move[0]):
                to_move.append(new_crates[move[1] - 1].pop())
            to_move = list(reversed(to_move))
            for crate in to_move:
                new_crates[move[2] - 1].append(crate)
    str = ""
    for column in new_crates:
        str += (column[-1])

    print(str)

if __name__ == "__main__":
    part1()
    part2()