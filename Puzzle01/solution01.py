import time

print('Starting Solution 1...')

#Read input file as lines
with open('input.txt') as inputFile:
    lines = inputFile.readlines()
#Initialize largest as 0. This will hold the index of the currently largest elf.
largest = 0
#Initialize largestVal as 0. This will hold the num of cal of the currently largest elf.
largestVal = 0
#Initialize elfCal. This will be the calories of an individual elf.
elfCal = 0
#Initialize elfCounter.
elfCounter = 0
#Initialize first, second, and third for the three greatest calories
first = 0
second = 0
third = 0

#Major loop that checks for the greatest values
for line in lines:
    if line != '\n':
        elfCal += int(line)
    else:
        elfCounter += 1
        if elfCal > third:
            if elfCal > second:
                if elfCal > first:
                    first = elfCal
                    largestVal = elfCal
                    largest = elfCounter
                else:
                    second = elfCal
            else:
                third = elfCal
        elfCal = 0
        print('Largest Elf: ' + str(largest) + ' - ' + str(largestVal))

#One the check one final time since the input doesn't end with a /n.
elfCounter += 1
print('end')
if elfCal > largestVal:
    largestVal = elfCal
    largest = elfCounter
    elfCal = 0
    print('Largest Elf: ' + str(largest) + ' - ' + str(largestVal))
        
#Print results
print('Finished, Top three sum: ' + str(first + second + third))