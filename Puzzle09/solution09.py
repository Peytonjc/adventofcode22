print('Starting Solution 9...')

# Read input file as lines
with open('/workspaces/adventofcode22/Puzzle09/input.txt') as inputFile:
    lines = inputFile.readlines()

# Initialize dictionaries
locationDict = {
    'H': [0, 0],
    'T': [0, 0]
}
visitedLocations = [[0, 0]]

# I think we are going to make a state machine...

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


def returnTailLocation(hLocation, tLocation, hMovement):
    hOrientation = returnHOrientation(hLocation, tLocation)
    if hOrientation == 'On':
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
        
for line in lines:
    line = line.replace('\n', '')
    instruction = line.split(' ')[0]
    steps = line.split(' ')[1]
    i = 0
    while i < int(steps):
        locationDict['T'] = returnTailLocation(locationDict['H'], locationDict['T'], instruction)
        if instruction == 'R':
            locationDict['H'][0] = locationDict['H'][0] + 1
        elif instruction == 'L':
            locationDict['H'][0] = locationDict['H'][0] - 1
        elif instruction == 'U':
            locationDict['H'][1] = locationDict['H'][1] + 1
        elif instruction == 'D':
            locationDict['H'][1] = locationDict['H'][1] - 1
        i += 1
        if locationDict['T'] not in visitedLocations:
            visitedLocations.append(locationDict['T'])

print(visitedLocations)
print(len(visitedLocations))
