print('Starting Solution 5...')

#Read input file as lines
with open('input.txt') as inputFile:
    lines = inputFile.readlines()

crateLists = []
newCrateLists = []
first = True
firstMove = True
index = 0
for line in lines:
    if '[' in line:
        # Looking at the crate map.
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
        # This is a move command
        if firstMove:
            index = 0
            for list in crateLists:
                crateLists[index].reverse()
                index = index + 1
            firstMove = False
        line = line.replace('move ', '').replace(' from ', ',').replace(' to ', ',').replace ('\n', '')
        infoList = line.split(',')
        movingObject = []
        for i in range(int(infoList[0])):
            #movingObject = crateLists[int(infoList[1]) - 1]
            movingObject.append(crateLists[int(infoList[1]) - 1].pop())
        for j in range(int(infoList[0])):
            crateLists[int(infoList[2]) - 1].append(movingObject.pop())



for i in range(len(crateLists)):
    print ('Row #' + str(i + 1))
    for j in crateLists[i]:
        print(j)