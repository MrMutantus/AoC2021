import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from Utils import utils

def main():
    input = utils.getInput("input.txt")
    solution1 = puzzle1(input)
    print(solution1)
    solution2 = puzzle2(input)
    print(solution2)

def puzzle1(input):
    height = len(input)
    length = len(input[0])
    count = [0 for x in range(length-1)]
    for row in input:
        for i in range(length-1):
            count[i] += int(row[i])
    
    gamma = [1 if x*2 > height else 0 for x in count]
    epsilon = [1 if x == 0 else 0 for x in gamma]
    gamma = toString(gamma)
    epsilon = toString(epsilon)
    gamma = toInt(gamma)
    epsilon = toInt(epsilon)
    return gamma*epsilon

def puzzle2(input):
    return "to do"

def toString(list):
    return "".join(str(char) for char in list)

def toInt(binary):
    return int(binary, 2)

main()