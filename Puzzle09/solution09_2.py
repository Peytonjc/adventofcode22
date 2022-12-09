print('Starting Solution 9...')

# Read input file as lines
with open('/workspaces/adventofcode22/Puzzle09/input.txt') as inputFile:
    lines = inputFile.readlines()

# Initialize dictionaries
locationDict = {
    'H': [0, 0],
    '1': [0, 0],
    '2': [0, 0],
    '3': [0, 0],
    '4': [0, 0],
    '5': [0, 0],
    '6': [0, 0],
    '7': [0, 0],
    '8': [0, 0],
    '9': [0, 0]
}
visitedLocations = [[0, 0]]
visitedEndLocations = [[0, 0]]
instructionHolder = []

# I think we are going to make a state machine...

# Function to return the orientation of H in relation to T
# NW N NE
#  W T E
# SW S SE
def returnHOrientation(hLocation, tLocation):
    if tLocation == hLocation:
        return 'On'
    elif (tLocation[1] == hLocation[1]) & (tLocation[0] < hLocation[0]):
        return 'E'
    elif (tLocation[1] < hLocation[1]) & (tLocation[0] < hLocation[0]):
        return 'NE'
    elif (tLocation[1] < hLocation[1]) & (tLocation[0] == hLocation[0]):
        return 'N'
    elif (tLocation[1] < hLocation[1]) & (tLocation[0] > hLocation[0]):
        return 'NW'
    elif (tLocation[1] == hLocation[1]) & (tLocation[0] > hLocation[0]):
        return 'W'
    elif (tLocation[1] > hLocation[1]) & (tLocation[0] > hLocation[0]):
        return 'SW'
    elif (tLocation[1] > hLocation[1]) & (tLocation[0] == hLocation[0]):
        return 'S'
    elif (tLocation[1] > hLocation[1]) & (tLocation[0] < hLocation[0]):
        return 'SE'

# Function to return the Tail location from the location of H and T and a movement.
# I think the movement results could be changed to just the current position of
# H (for when it's changed) but, I haven't tested that yet...
# I added locations for new movements: UR, UL, DR, DL
def returnTailLocation(hLocation, tLocation, hMovement):
    hOrientation = returnHOrientation(hLocation, tLocation)
    if (hOrientation == 'On') | (hMovement == 'NONE'):
        return tLocation
    elif hMovement == 'R':
        if (hOrientation == 'E'):
            return [tLocation[0] + 1, tLocation[1]]
        elif (hOrientation == 'NE'):
            return [tLocation[0] + 1, tLocation[1] + 1]
        elif (hOrientation == 'N'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'NW'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'W'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'SW'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'S'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'SE'):
            return [tLocation[0] + 1, tLocation[1] - 1]
    elif hMovement == 'U':
        if (hOrientation == 'E'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'NE'):
            return [tLocation[0] + 1, tLocation[1] + 1]
        elif (hOrientation == 'N'):
            return [tLocation[0], tLocation[1] + 1]
        elif (hOrientation == 'NW'):
            return [tLocation[0] - 1, tLocation[1] + 1]
        elif (hOrientation == 'W'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'SW'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'S'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'SE'):
            return [tLocation[0], tLocation[1]]
    elif hMovement == 'D':
        if (hOrientation == 'E'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'NE'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'N'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'NW'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'W'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'SW'):
            return [tLocation[0] - 1, tLocation[1] - 1]
        elif (hOrientation == 'S'):
            return [tLocation[0], tLocation[1] - 1]
        elif (hOrientation == 'SE'):
            return [tLocation[0] + 1, tLocation[1] - 1]
    elif hMovement == 'L':
        if (hOrientation == 'E'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'NE'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'N'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'NW'):
            return [tLocation[0] - 1, tLocation[1] + 1]
        elif (hOrientation == 'W'):
            return [tLocation[0] - 1, tLocation[1]]
        elif (hOrientation == 'SW'):
            return [tLocation[0] - 1, tLocation[1] - 1]
        elif (hOrientation == 'S'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'SE'):
            return [tLocation[0], tLocation[1]]
    elif hMovement == 'UR':
        if (hOrientation == 'E'):
            return [tLocation[0] + 1, tLocation[1] + 1]
        elif (hOrientation == 'NE'):
            return [tLocation[0] + 1, tLocation[1] + 1]
        elif (hOrientation == 'N'):
            return [tLocation[0] + 1, tLocation[1] + 1]
        elif (hOrientation == 'NW'):
            return [tLocation[0], tLocation[1] + 1]
        elif (hOrientation == 'W'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'SW'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'S'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'SE'):
            return [tLocation[0] + 1, tLocation[1]]
    elif hMovement == 'DR':
        if (hOrientation == 'E'):
            return [tLocation[0] + 1, tLocation[1] - 1]
        elif (hOrientation == 'NE'):
            return [tLocation[0] + 1, tLocation[1]]
        elif (hOrientation == 'N'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'NW'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'W'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'SW'):
            return [tLocation[0], tLocation[1] - 1]
        elif (hOrientation == 'S'):
            return [tLocation[0] + 1, tLocation[1] - 1]
        elif (hOrientation == 'SE'):
            return [tLocation[0] + 1, tLocation[1] - 1]
    elif hMovement == 'UL':
        if (hOrientation == 'E'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'NE'):
            return [tLocation[0], tLocation[1] + 1]
        elif (hOrientation == 'N'):
            return [tLocation[0] - 1, tLocation[1] + 1]
        elif (hOrientation == 'NW'):
            return [tLocation[0] - 1, tLocation[1] + 1]
        elif (hOrientation == 'W'):
            return [tLocation[0] - 1, tLocation[1] + 1]
        elif (hOrientation == 'SW'):
            return [tLocation[0] - 1, tLocation[1]]
        elif (hOrientation == 'S'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'SE'):
            return [tLocation[0], tLocation[1]]
    elif hMovement == 'DL':
        if (hOrientation == 'E'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'NE'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'N'):
            return [tLocation[0], tLocation[1]]
        elif (hOrientation == 'NW'):
            return [tLocation[0] - 1, tLocation[1]]
        elif (hOrientation == 'W'):
            return [tLocation[0] - 1, tLocation[1] - 1]
        elif (hOrientation == 'SW'):
            return [tLocation[0] - 1, tLocation[1] - 1]
        elif (hOrientation == 'S'):
            return [tLocation[0] - 1, tLocation[1] - 1]
        elif (hOrientation == 'SE'):
            return [tLocation[0], tLocation[1] - 1]

# Returns the movement of a knot based on its old and new positions.
def getMovement(oldPos, newPos):
    if (oldPos[0] == newPos[0]) & (oldPos[1] == newPos[1]):
        return 'NONE'
    elif (oldPos[0] < newPos[0]) & (oldPos[1] == newPos[1]):
        return 'R'
    elif (oldPos[0] < newPos[0]) & (oldPos[1] < newPos[1]):
        return 'UR'
    elif (oldPos[0] == newPos[0]) & (oldPos[1] < newPos[1]):
        return 'U'
    elif (oldPos[0] > newPos[0]) & (oldPos[1] < newPos[1]):
        return 'UL'
    elif (oldPos[0] > newPos[0]) & (oldPos[1] == newPos[1]):
        return 'L'
    elif (oldPos[0] > newPos[0]) & (oldPos[1] > newPos[1]):
        return 'DL'
    elif (oldPos[0] == newPos[0]) & (oldPos[1] > newPos[1]):
        return 'D'
    elif (oldPos[0] < newPos[0]) & (oldPos[1] > newPos[1]):
        return 'DR'

# The main loop. Iterates through the steps and assigns locations to the locationDict.
# Also moves H and keeps track of the locations visited by the 9th square. The code simulates
# each knot's path individually, stores the commands, and then uses those commands on the next
# knot simulation.    
for line in lines:
    line = line.replace('\n', '')
    instruction = line.split(' ')[0]
    steps = line.split(' ')[1]
    i = 0
    startCount = 0

    while i < int(steps):
        oneLoc = returnTailLocation(locationDict['H'], locationDict['1'], instruction)
        if instruction == 'R':
            locationDict['H'][0] = locationDict['H'][0] + 1
        elif instruction == 'L':
            locationDict['H'][0] = locationDict['H'][0] - 1
        elif instruction == 'U':
            locationDict['H'][1] = locationDict['H'][1] + 1
        elif instruction == 'D':
            locationDict['H'][1] = locationDict['H'][1] - 1
        i += 1
        instructionHolder.append(getMovement(locationDict['1'], oneLoc))

        locationDict['1'] = oneLoc
        if locationDict['1'] not in visitedLocations:
            visitedLocations.append(locationDict['1'])

j = 2
while j < 10:
    print(j)
    instructionList = instructionHolder
    instructionHolder = []
    locationDict[str(j - 1)] = [0,0]
    for instruct in instructionList:
        newLoc = returnTailLocation(locationDict[str(j - 1)], locationDict[str(j)], instruct)
        if instruct == 'R':
            locationDict[str(j - 1)][0] = locationDict[str(j - 1)][0] + 1
        elif instruct == 'L':
            locationDict[str(j - 1)][0] = locationDict[str(j - 1)][0] - 1
        elif instruct == 'U':
            locationDict[str(j - 1)][1] = locationDict[str(j - 1)][1] + 1
        elif instruct == 'D':
            locationDict[str(j - 1)][1] = locationDict[str(j - 1)][1] - 1
        elif instruct == 'UR':
            locationDict[str(j - 1)][0] = locationDict[str(j - 1)][0] + 1
            locationDict[str(j - 1)][1] = locationDict[str(j - 1)][1] + 1
        elif instruct == 'UL':
            locationDict[str(j - 1)][0] = locationDict[str(j - 1)][0] - 1
            locationDict[str(j - 1)][1] = locationDict[str(j - 1)][1] + 1
        elif instruct == 'DR':
            locationDict[str(j - 1)][0] = locationDict[str(j - 1)][0] + 1
            locationDict[str(j - 1)][1] = locationDict[str(j - 1)][1] - 1
        elif instruct == 'DL':
            locationDict[str(j - 1)][0] = locationDict[str(j - 1)][0] - 1
            locationDict[str(j - 1)][1] = locationDict[str(j - 1)][1] - 1
        instructionHolder.append(getMovement(locationDict[str(j)], newLoc))
        locationDict[str(j)] = newLoc
        if j == 9:
            if locationDict['9'] not in visitedEndLocations:
                visitedEndLocations.append(locationDict['9'])
    j += 1


# Print results
print(visitedLocations)
print(len(visitedLocations))
print('Part Two:')
print(visitedEndLocations)
print(len(visitedEndLocations))
