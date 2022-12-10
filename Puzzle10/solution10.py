print('Starting Solution 10...')

#Read input file as lines
with open('/workspaces/adventofcode22/Puzzle10/input.txt') as inputFile:
    lines = inputFile.readlines()

# Initialize final score val, current cycle, X register, and the rows of the CRT for part two
score = 0
currentCycle = 0
XRegister = 1
rowOne = []
rowTwo = []
rowThree = []
rowFour = []
rowFive = []
rowSix = []
currentRow = [rowOne, rowTwo, rowThree, rowFour, rowFive, rowSix]
currentRowIndex = 0

def getCurrentRowIndex(currentCycle):
    if currentCycle <= 40:
        return 0
    elif currentCycle <= 80:
        return 1
    elif currentCycle <= 120:
        return 2
    elif currentCycle <= 160:
        return 3
    elif currentCycle <= 200:
        return 4
    elif currentCycle <= 240:
        return 5

def getCycleToCRT(currentCycle):
    if currentCycle <= 40:
        return 0
    elif currentCycle <= 80:
        return 40
    elif currentCycle <= 120:
        return 80
    elif currentCycle <= 160:
        return 120
    elif currentCycle <= 200:
        return 160
    elif currentCycle <= 240:
        return 200

# Start major loop
for line in lines:
    line = line.replace('\n', '')
    # Start of cycle
    if 'noop' in line:
        # No change to register
        currentCycle += 1
        if (currentCycle == 20) | (currentCycle == 60) | (currentCycle == 100) | (currentCycle == 140) | (currentCycle == 180) | (currentCycle == 220): #((currentCycle - 20)%40 == 0):
            score += XRegister * currentCycle
        # Print out CRT value.
        if (currentCycle - getCycleToCRT(currentCycle) >= XRegister) & (currentCycle - getCycleToCRT(currentCycle) <= XRegister + 2):
            currentRow[getCurrentRowIndex(int(currentCycle))].append('#')
        else:
            currentRow[getCurrentRowIndex(int(currentCycle))].append('.')
        # End of cycle
        continue
    elif 'addx' in line:
        # Change to register (there will be two cycles)
        # End of cycle
        currentCycle += 1
        if (currentCycle == 20) | (currentCycle == 60) | (currentCycle == 100) | (currentCycle == 140) | (currentCycle == 180) | (currentCycle == 220): #((currentCycle - 20)%40 == 0):
            score += XRegister * currentCycle
        # Print out CRT value.
        if (currentCycle - getCycleToCRT(currentCycle) >= XRegister) & (currentCycle - getCycleToCRT(currentCycle) <= XRegister + 2):
            currentRow[getCurrentRowIndex(int(currentCycle))].append('#')
        else:
            currentRow[getCurrentRowIndex(int(currentCycle))].append('.')
        # Start of cycle
        # Modify Register
        # The cycle officially ends before the change to the XRegister happens
        currentCycle += 1
        # End of cycle
        if (currentCycle == 20) | (currentCycle == 60) | (currentCycle == 100) | (currentCycle == 140) | (currentCycle == 180) | (currentCycle == 220): #((currentCycle - 20)%40 == 0):
            score += XRegister * currentCycle
        # Print out CRT value.
        if (currentCycle - getCycleToCRT(currentCycle) >= XRegister) & (currentCycle - getCycleToCRT(currentCycle) <= XRegister + 2):
            currentRow[getCurrentRowIndex(int(currentCycle))].append('#')
        else:
            currentRow[getCurrentRowIndex(int(currentCycle))].append('.')
        XRegister += int(line.split(' ')[1])
        continue

# Print results to console
print("Answer to Part 1:")
print(score)
print("CRT Output for Part 2:")
for line in currentRow:
    holderString = ''
    print(holderString.join(line))

