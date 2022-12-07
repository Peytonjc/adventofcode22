print('Starting Solution 4...')

#Read input file as lines
with open('input.txt') as inputFile:
    lines = inputFile.readlines()

# Initialize score vals
score = 0
scoreTwo = 0

# Loop for part one.
for line in lines:
    # Split a line into two separate elves ane remove junk chars.
    firstElf = line.split(',')[0]
    secondElf = line.split(',')[1].replace('\n','')

    # Split each of the elves into the two parts of their values.
    fLow = int(firstElf.split('-')[0])
    fHigh = int(firstElf.split('-')[1])
    sLow = int(secondElf.split('-')[0])
    sHigh = int(secondElf.split('-')[1])

    #Check to see if either elf contains the other and add to score if so.
    if ((fLow <= sLow) & (fHigh >= sHigh)) | ((sLow <= fLow) & (sHigh >= fHigh)):
        #print(line)
        #print(str(fLow) + ' ' + str(fHigh) + ' ' + str(sLow) + ' ' + str(sHigh))
        score = score + 1

# Loop for part two
for line in lines:
    # See first loop for more info on this.
    firstElf = line.split(',')[0]
    secondElf = line.split(',')[1].replace('\n','')
    fLow = int(firstElf.split('-')[0])
    fHigh = int(firstElf.split('-')[1])
    sLow = int(secondElf.split('-')[0])
    sHigh = int(secondElf.split('-')[1])
    # In additon to checking if an elf contains another elf, check for overlaps.
    if ((fLow <= sLow) & (fHigh >= sLow)) | ((fLow <= sHigh) & (fHigh >= sHigh) | (fLow <= sLow) & (fHigh >= sHigh)) | ((sLow <= fLow) & (sHigh >= fHigh)):
        #print(line)
        #print(str(fLow) + ' ' + str(fHigh) + ' ' + str(sLow) + ' ' + str(sHigh))
        scoreTwo = scoreTwo + 1

print('Score for Part 1: ' + str(score))
print('Score for Part 2: ' + str(scoreTwo))