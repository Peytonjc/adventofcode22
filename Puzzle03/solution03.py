print('Starting Solution 3...')

#Read input file as lines
with open('input.txt') as inputFile:
    lines = inputFile.readlines()

# Initialize score
score = 0
scoreTwo = 0

# Loop through all lines of input
for line in lines:
    line = line.replace('\n', '')
    # Split rucksacks into two parts
    ruckOne = line[:len(line)//2]
    ruckTwo = line[len(line)//2:]
    # Loop through ruckOne and find any dupes inside of ruckTwo. Find the val of that dupe and add it to the score.
    for i in ruckOne:
        if i in ruckTwo:
            # Dupe found
            if ord(i) < 91:
                score = score + ord(i) - 38
            else:
                score = score + ord(i) - 96
            break

# New loop for part two. Need to break them up into groups of three and check for dupes.
index = 1
for line in lines:
    if (index == 1):
        lineOne = line
        index = 2
    elif (index == 2):
        lineTwo = line
        index = 3
    elif (index == 3):
        for i in line:
            if (i in lineOne) & (i in lineTwo):
                # Dupe found
                if ord(i) < 91:
                    scoreTwo = scoreTwo + ord(i) - 38
                else:
                    scoreTwo = scoreTwo + ord(i) - 96
                break
        index = 1

print('Score: ' + str(score))
print('Score for part two: ' + str(scoreTwo))
        