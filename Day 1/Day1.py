def solve(input):
    prev = None
    increaseCount = 0
    for row in input:
        data = int(row)
        if prev == None:
            prev = data
            continue
        if data > prev:
            increaseCount += 1
        prev = data
    return increaseCount

def solve2(input):
    triplet = []
    for index in range((len(input)-2)):
        temp = []
        temp.append(int(input[index]))
        temp.append(int(input[(index + 1)]))
        temp.append(int(input[(index + 2)]))
        triplet.append(sum(temp))
    return solve(triplet)

input = [input for input in open('input.txt')]
solution = solve(input)
print(solution)
solution2 = solve2(input)
print(solution2)
