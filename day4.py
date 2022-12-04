def input():
    with open('d4.txt', 'r') as file:
        lines = file.read().split("\n")
    return lines


def part1():
    lines = input()
    overlaps = 0
    for line in lines:
        pairs = line.split(",")
        first = pairs[0].split("-")
        second = pairs[1].split("-")
        if int(first[0]) > int(second[0]):
            if int(first[1]) <= int(second[1]):
                overlaps += 1
        elif int(first[0]) < int(second[0]):
            if int(first[1]) >= int(second[1]):
                overlaps += 1 
        else:
            if int(first[1]) <= int(second[1]) or int(first[1]) >= int(second[1]):
                overlaps += 1
    print("task 1: ", overlaps)    

def part2():
    lines = input()
    overlaps = 0
    for line in lines:
        pairs = line.split(",")
        first = pairs[0].split("-")
        second = pairs[1].split("-")
        if int(first[0]) > int(second[0]):
            if int(first[0]) <= int(second[1]):
                overlaps += 1
        elif int(first[0]) < int(second[0]):
            if int(first[1]) >= int(second[0]):
                overlaps += 1 
        else:
            overlaps += 1
            
                
    print("task 2: ", overlaps)   

if __name__ == "__main__":
    part1()
    part2()