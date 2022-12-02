def input():
    with open('d2.txt', 'r') as file:
        text = file.read()
        lines = text.split("\n")
    return text, lines


def part1():
    file, lines = input()
    score = 0
    score += 1 * file.count("X")
    score += 2 * file.count("Y")
    score += 3 * file.count("Z")
    for line in lines:
        match line:
            case "A Y":
                score += 6
            case "B Z":
                score += 6
            case "C X":
                score += 6
            case "B Y":
                score += 3
            case "A X":
                score += 3
            case "C Z":
                score += 3

    print(score)



def part2():
    file, lines = input()
    score = 0
    score += 3 * file.count("Y")
    score += 6 * file.count("Z")
    for line in lines:
        match line:
            case "A Y":
                score += 1
            case "A X":
                score += 3
            case "A Z":
                score += 2
            case "B Z":
                score += 3
            case "B Y":
                score += 2
            case "B X":
                score += 1
            case "C X":
                score += 2
            case "C Y":
                score += 3
            case "C Z":
                score += 1
    print(score)

if __name__ == "__main__":
    part1()
    part2()