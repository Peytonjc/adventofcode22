print('Starting Solution 2...')

#Read input file as lines
with open('input.txt') as inputFile:
    lines = inputFile.readlines()
    
# Initialize a variable to store the final score
score = 0

# Define a dictionary that maps tuples of the form (A,X) to a score value
scoreDict = {
    'A X': 4, #Rock Rock
    'A Y': 8, #Rock Paper
    'A Z': 3, #Rock Scisors
    'B X': 1, #P R 
    'B Y': 5, #P P 
    'B Z': 9, #P S 
    'C X': 7, #S R 
    'C Y': 2, #S P 
    'C Z': 6 #S S 
    }
    
# Define another dictionary that maps tuples of the form (A,X) to a different tuple (This is for part two)
scoreDict2 = {
    'A X': 'A Z', #Rock lose
    'A Y': 'A X', #Rock draw
    'A Z': 'A Y', #Rock Win
    'B X': 'B X', #P lose 
    'B Y': 'B Y', #P draw 
    'B Z': 'B Z', #P win 
    'C X': 'C Y', #S lose 
    'C Y': 'C Z', #S draw 
    'C Z': 'C X' #S win 
    }

for line in lines:
    # Use the value in scoreDict2 to look up a value in scoreDict,
    # then add that value to the final score
    score = score + scoreDict[scoreDict2[line.replace('\n','')]]
    
# Print final score on screen
print('Final score is: ' + str(score))