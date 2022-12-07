print('Starting Solution 5...')

#Read input file as lines
with open('input.txt') as inputFile:
    lines = inputFile.readlines()

# Initialize crateLists as a list of lists for the stacks of crates, some flags for checking if
# it is the first line, and an index
crateLists = []
first = True
firstMove = True
index = 0

# Start reading the file
for line in lines:
    if '[' in line:
        # Looking at the crate map. Build the list of lists to hold each of the stacks.
        line = line.replace('    ', '[-] ' )
        line = line.replace('[-]  ', ' [-] ')
        line = line.replace('][-] ', '] [-]')
        print(line)
        list = line.split(' ')
        if first:
            for i in range(len(list)):
                crateLists.append([])
            first = False
        index = 0
        for val in list:
            val = val.replace('\n', '')
            if '[-]' not in val:
                if index < len(crateLists):
                    crateLists[index].append(val.replace('[', '').replace(']', ''))
            index = index + 1
    elif 'move' in line:
        # This is a move command. Start operating on the crateLists based on the steps given.
        if firstMove:
            index = 0
            for list in crateLists:
                crateLists[index].reverse()
                index = index + 1
            firstMove = False
        line = line.replace('move ', '').replace(' from ', ',').replace(' to ', ',').replace ('\n', '')
        infoList = line.split(',')
        for i in range(int(infoList[0])):
            #movingObject = crateLists[int(infoList[1]) - 1]
            movingObject = crateLists[int(infoList[1]) - 1].pop()
            crateLists[int(infoList[2]) - 1].append(movingObject)


# Print Results
for i in range(len(crateLists)):
    print ('Row #' + str(i + 1))
    for j in crateLists[i]:
        print(j)