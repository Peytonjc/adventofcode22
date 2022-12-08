print('Starting Solution 8...')

#Read input file as lines
with open('/workspaces/adventofcode22/Puzzle08/input.txt') as inputFile:
    lines = inputFile.readlines()

# Initialize score
score = 0
yIndex = 0
xIndex = 0

for line in lines:
    line = line.replace('\n', '')
    if (yIndex == 0) | (yIndex == len(lines) - 1):
        #   This is the first or last row of trees
        score = score + len(line)
    else:
        # Inside the forest
        xIndex = 0
        for tree in line:
            isVisibleLeft = True
            isVisibleRight = True
            isVisibleUp = True
            isVisibleDown = True
            if (xIndex == 0) | (xIndex == len(line) - 1):
                # First or last tree
                score += 1
            else:
                yCheck = 0
                for checkLine in lines:
                    checkLine = checkLine.replace('\n', '')
                    if (int(checkLine[xIndex]) >= int(tree)) & (yCheck < yIndex):
                        isVisibleUp = False
                    if (int(checkLine[xIndex]) >= int(tree)) & (yCheck > yIndex):
                        isVisibleDown = False
                    yCheck += 1
                    xCheck = 0
                    for checkTree in line:
                        if (int(checkTree) >= int(tree)) & (xCheck < xIndex):
                            isVisibleLeft = False
                        if (int(checkTree) >= int(tree)) & (xCheck > xIndex):
                            isVisibleRight = False
                        xCheck += 1
                if (isVisibleUp | isVisibleDown | isVisibleLeft | isVisibleRight):
                    score += 1
                    print(score)
            xIndex += 1
    yIndex += 1

print(score)