print('Starting Solution 8...')

#Read input file as lines
with open('/workspaces/adventofcode22/Puzzle08/input.txt') as inputFile:
    lines = inputFile.readlines()

# Initialize score
score = 0
yIndex = 0
xIndex = 0
scoreTable = []

for line in lines:
    line = line.replace('\n', '')
    #if (yIndex == 0) | (yIndex == len(lines) - 1):
        #   This is the first or last row of trees
    #    score = score + len(line)
    #else:
        # Inside the forest
    xIndex = 0
    for tree in line:
        leftScore = 0
        rightScore = 0
        upScore = 0
        downScore = 0
        isVisibleLeft = True
        isVisibleRight = True
        isVisibleUp = True
        isVisibleDown = True
        xLine = list(line)
        yLine = []
        yCheck = 0
        for checkLine in lines:
            checkLine = checkLine.replace('\n', '')
            # build y line
            yLine.append(checkLine[xIndex])
        if xIndex == 0:
            leftLine = []
        else:
            leftLine = list(xLine)[0:xIndex]
        if xIndex == len(xLine) - 1:
            rightLine = []
        else:
            rightLine = list(xLine)[xIndex + 1:len(xLine)]
        if yIndex == 0:
            upLine = []
        else:
            upLine = yLine[0:yIndex]
        if yIndex == len(yLine) - 1:
            downLine = []
        else:
            downLine = yLine[yIndex + 1:len(yLine)]

        if leftLine == []:
            leftScore = 0
        else:
            for val in reversed(leftLine):
                if int(val) < int(tree):
                    leftScore += 1
                else:
                    leftScore += 1
                    break
        if rightLine == []:
            rightScore = 0
        else:
            for val in rightLine:
                if int(val) < int(tree):
                    rightScore += 1
                else:
                    rightScore += 1
                    break
        if upLine == []:
            upScore = 0
        else:
            for val in reversed(upLine):
                if int(val) < int(tree):
                    upScore += 1
                else:
                    upScore += 1
                    break
        if downLine == []:
            downScore = 0
        else:
            for val in downLine:
                if int(val) < int(tree):
                    downScore += 1
                else:
                    downScore += 1
                    break
        scoreTable.append(rightScore * leftScore * upScore * downScore)
        print(str(rightScore * leftScore * upScore * downScore))
        xIndex += 1
    yIndex += 1

print(max(scoreTable))