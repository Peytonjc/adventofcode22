
print('Starting Solution 7...')

#Read input file as lines
with open('/workspaces/adventofcode22/Puzzle07/input.txt') as inputFile:
    lines = inputFile.readlines()

filesystem = [['', ' /', 'dir']]
fileObjectList = []
filePath = []
isDisplay = False
dirList = ''
lsLine = ''
currentDir = ''
placeholder = ''
solutionDict = {'/': 0}
checkedFiles = []

for line in lines:
    line = line.replace('\n', '')
    if '$ ls' in line:
        continue
    elif '$ cd' in line:
        if '..' not in line:
            filePath.append(str(filePath).replace('[', '').replace(']', '').replace(',', '').replace(' ', '').replace('\'', '') + line.replace('$ cd ', ''))
            if (str(filePath).replace('[', '').replace(']', '').replace(',', '').replace(' ', '').replace('\'', '') + line.replace('$ cd ', '') not in solutionDict):
                solutionDict[line.replace('$ cd ', '')] = 0
        else:
            filePath.pop()
        isDisplay = False
    else:#if isDisplay:
        # Looking at a file or dir
        if 'dir ' in line:
            # Looking at dir
            #filesystem.append([filePath[-1], line.replace('dir ', ''), 'dir'])
            if (str(filePath).replace('[', '').replace(']', '').replace(',', '').replace(' ', '').replace('\'', '') + line.replace('dir ', '') not in solutionDict):
                solutionDict[str(filePath).replace('[', '').replace(']', '').replace(',', '').replace(' ', '').replace('\'', '') + line.replace('dir ', '')] = 0
        else:
            # Looking at file
            #filesystem.append([filePath[-1], line.split(' ')[1], int(line.split(' ')[0])] )
            if (str(filePath).replace('[', '').replace(']', '').replace(',', '').replace(' ', '').replace('\'', '') + line not in checkedFiles):
                for file in filePath:
                    solutionDict[file] = solutionDict[file] + int(line.split(' ')[0])
                checkedFiles.append(str(filePath).replace('[', '').replace(']', '').replace(',', '').replace(' ', '').replace('\'', '') + line)
    #elif '$' in line:
    #    isDisplay = False

#print (filesystem)
#print(checkedFiles)


#for file in solutionDict:
    #fileSize = getFileSize
    #print(file.name + ' ' + str(getFileSize(file)))
smallFiles = [k for k, v in solutionDict.items() if v <= 100000]
bigFiles = [k for k, v in solutionDict.items() if v >= 4274331]
print(smallFiles)
solution = 0
solTwo = 0
for val in smallFiles:
    print(val + ' ' + str(solutionDict[val]))
    solution = solution + solutionDict[val]
print(solution)
for val in bigFiles:
    print(val + ' ' + str(solutionDict[val]))