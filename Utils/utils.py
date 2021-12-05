def getInput(path):
    data = open(path)
    input = [row for row in data]
    data.close()
    return input