print('Starting Solution 6...')

# Define function to check for dupes within a list
def checkForDupes(listOfElems):
    ''' Check if given list contains any duplicates '''    
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)         
    return False

#Read input file as lines
with open('input.txt') as inputFile:
    lines = inputFile.readlines()

# Define list for char buffer and a counter for the answer
charList = []
counter = 0

# For each char, after building the initial buffer, check for dupes and keep modifying the buffer.
# Keep track of the index with 'counter'
for char in lines[0]:
    # For part two, I changed this value from 3 to 13
    if counter <= 13:
        charList.append(char)
        counter = counter + 1
    elif (checkForDupes(charList)):
        charList.remove(charList[0])
        charList.append(char)
        counter = counter + 1
    else:
        break

# Print results
print (charList)
print (str(counter))

