def input():
    with open('d6.txt', 'r') as file:
        text = file.read().strip("\n")
    return text


def part1():
    file = input()
    iteration = 0
    seq = []
    for letter in file:
        iteration += 1
        seq.append(letter)
        if len(seq) == 4:
            if 4 == len(set(seq)):
                print(iteration, set(seq))
                break
            else:
                seq.pop(0)

def part2():
    file = input()
    iteration = 0
    seq = []
    for letter in file:
        iteration += 1
        seq.append(letter)
        if len(seq) == 14:
            if 14 == len(set(seq)):
                print(iteration, set(seq))
                break
            else:
                seq.pop(0)

if __name__ == "__main__":
    part1()
    part2()