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

# The main loop. Iterates through the steps and assigns locations to the locationDict.
# Also moves H and keeps track of the locations visited by T    
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

# Print results
print(visitedLocations)
print(len(visitedLocations))
