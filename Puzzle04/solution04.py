print('Starting Solution 4...')

#Read input file as lines
with open('input.txt') as inputFile:
    lines = inputFile.readlines()
score = 0
scoreTwo = 0
for line in lines:
    firstElf = line.split(',')[0]
    secondElf = line.split(',')[1].replace('\n','')
    fLow = int(firstElf.split('-')[0])
    fHigh = int(firstElf.split('-')[1])
    sLow = int(secondElf.split('-')[0])
    sHigh = int(secondElf.split('-')[1])
    if ((fLow <= sLow) & (fHigh >= sHigh)) | ((sLow <= fLow) & (sHigh >= fHigh)):
        #print(line)
        #print(str(fLow) + ' ' + str(fHigh) + ' ' + str(sLow) + ' ' + str(sHigh))
        score = score + 1

for line in lines:
    firstElf = line.split(',')[0]
    secondElf = line.split(',')[1].replace('\n','')
    fLow = int(firstElf.split('-')[0])
    fHigh = int(firstElf.split('-')[1])
    sLow = int(secondElf.split('-')[0])
    sHigh = int(secondElf.split('-')[1])
    if ((fLow <= sLow) & (fHigh >= sLow)) | ((fLow <= sHigh) & (fHigh >= sHigh) | (fLow <= sLow) & (fHigh >= sHigh)) | ((sLow <= fLow) & (sHigh >= fHigh)):
        #print(line)
        #print(str(fLow) + ' ' + str(fHigh) + ' ' + str(sLow) + ' ' + str(sHigh))
        scoreTwo = scoreTwo + 1
    else:
        print (line)

print('Score for Part 1: ' + str(score))
print('Score for Part 2: ' + str(scoreTwo))