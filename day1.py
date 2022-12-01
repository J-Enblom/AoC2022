with open('d1.txt', 'r') as file:
    lines = file.readlines()

"""Part 1"""
highest = 0
current = 0
for line in lines:
    if line == "\n":
        if current > highest:
            highest = current
        current = 0
    else:
        current += int(line.strip("\n"))

print(highest)

"""Part 2"""
highest = [0,1,2]
current = 0
for line in lines:
    if line == "\n":            
        if current > min(highest):
            index = highest.index(min(highest))
            highest[index] = current
        current = 0
    else:
        current += int(line.strip("\n"))

print(highest, sum(highest))
