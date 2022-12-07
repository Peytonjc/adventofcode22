print('Starting Solution 7...')

#Read input file as lines
with open('input.txt') as inputFile:
    lines = inputFile.readlines()
dirList = ''
lsLine = ''
cdLine = ''
placeholder = ''
for line in lines:
    cdLine = lsLine
    lsLine = placeholder
    placeholder = line
    if 'dir ' in line:
        if 'ls' in lsLine:
            line = line.replace('dir', cdLine.replace('cd ', ''))
        dirList = dirList + '\n' + line
        

print(dirList)