def main():
    print("Start")
    input = getInput()
    solution1 = puzzle1(input)
    print(solution1)
    solution2 = puzzle2(input)
    print(solution2)
    print("Ende")

def puzzle1(input):
    depth = 0
    pos = 0
    for line in input:
        command = line.split(" ")
        if command[0] == "forward":
            pos += int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])
    return pos * depth

def puzzle2(input):
    depth = 0
    aim = 0
    pos = 0
    for line in input:
        command = line.split(" ")
        if command[0] == "forward":
            pos += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])
    return pos * depth

def getInput():
    return [line for line in open("input.txt")]

main()