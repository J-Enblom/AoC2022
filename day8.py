from aocd.models import Puzzle
from aocd import submit

def part1(data):
    #print(data)
    visible = 0
    borderx = len(data[0])
    bordery = len(data)
    for y in range(bordery):
        for x in range(borderx):
            if y == 0 and x or y == bordery-1 or x == 0 or x == borderx-1:
                visible +=1
            else:
                tree = data[y][x]
                up = data[:y]
                down = data[y+1:]
                left = data[y][:x]
                right = data[y][x+1:]
                vis = True
                while True:
                    for i in up:
                        if i[x] >= tree:
                            vis = False
                    if vis:
                        visible += 1
                        break
                    else:
                        vis = True
                    for i in down:
                        if i[x] >= tree:
                            vis = False
                            break
                    if vis:
                        visible += 1
                        break
                    else:
                        vis = True
                    for i in left:
                        if i >= tree:
                            vis = False
                            break
                    if vis:
                        visible += 1
                        break
                    else:
                        vis = True
                    for i in right:
                        if i >= tree:
                            vis = False
                    if vis:
                        visible += 1
                    break


    return visible
        
def part2(data):
    borderx = len(data[0])
    bordery = len(data)
    best = 0 
    for y in range(bordery):
        for x in range(borderx):
            if y == 0 and x or y == bordery-1 or x == 0 or x == borderx-1:
                pass
            else:
                tree = data[y][x]
                up = data[:y]
                down = data[y+1:]
                left = data[y][:x]
                right = data[y][x+1:]
                scenic = 0
                temp = 0
                while True:
                    for i in up[::-1]:
                        if i[x] < tree:
                            scenic += 1
                        else:
                            scenic += 1
                            break
                    for i in down:
                        if i[x] < tree:
                            temp += 1
                        else:
                            temp += 1
                            break
                    scenic *= temp
                    temp = 0
                    for i in left[::-1]:
                        if i < tree:
                            temp += 1
                        else:
                            temp += 1
                            break
                    scenic*=temp
                    temp = 0
                    for i in right:
                        if i < tree:
                            temp += 1
                        else:
                            temp += 1
                            break
                    scenic*=temp
                    break

                if scenic > best:
                    best = scenic


    return best

if __name__ == "__main__":
    test = ["30373","25512","65332","33549","35390"]
    YEAR = int('2022')
    DAY = int('08')
    puzzle = Puzzle(day=DAY, year=YEAR)
    data = puzzle.input_data.split("\n")
    #p1_answer = part1(data)
    #print("part 1:", p1_answer)
    #submit(p1_answer, part="a", day=DAY, year=YEAR)
    p2_answer = part2(data)
    print("part 2:", p2_answer)
    submit(p2_answer, part="b", day=DAY, year=YEAR)