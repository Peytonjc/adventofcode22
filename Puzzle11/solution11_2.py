print('Starting Solution 11...')

#Read input file as lines
with open('/workspaces/adventofcode22/Puzzle11/input.txt') as inputFile:
    lines = inputFile.readlines()

# Dictonary for the operators provided from input strings
op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y}

# Initialize global val for the modulo trick
finalProduct = 1

# Start by defining a monkey object
class Monkey:
    def __init__(self, name, items, operation, test, trueOption, falseOption):
        self.name = name.replace('Monkey ', '').replace(':','')
        self.items = items.replace('  Starting items: ','').split(', ')
        self.operation = operation.replace('  Operation: new = ','').split(' ')
        self.test = test.replace('  Test: divisible by ','')
        self.trueOption = trueOption.replace('    If true: throw to monkey ','')
        self.falseOption = falseOption.replace('    If false: throw to monkey ', '')
    # Function to add an item to a monkey
    def addItem(self, item):
        self.items.append(item)
    # Function to run a test. Removes the item from monkey and returns the monkey that will recieve the object
    def runTest(self):
        if int(self.items[0])%int(self.test) == 0:
            # Divisible
            self.items.pop(0)
            return int(self.trueOption)
        else:
            self.items.pop(0)
            return int(self.falseOption)
    # Function to run an operation, change the item within the monkey, and return the resulting value.
    def runOperation(self):
        if self.operation[0] == 'old':
            firstVal = self.items[0]
        else:
            firstVal = self.operation[0]
        if self.operation[2] == 'old':
            secondVal = self.items[0]
        else:
            secondVal = self.operation[2]
        newItem = op[self.operation[1]] (int(firstVal), int(secondVal))
        self.items[0] = newItem
        return newItem
    # Function to keep worry value down
    def boredItemChange(self):
        #self.items[0] = str(int(self.items[0])//3)
        # Some modulo business to keep the numbers down. Found this, and it's pretty cool
        # if a ≡ b mod m then a / n ≡ (b / n) mod (m / n) as long as a, b, and m are divisible by n
        self.items[0] = str(int(self.items[0])%finalProduct)
        return int(self.items[0])


# Build the list of monkeys.
monkeys = []
monkeyBusinessList = []
count = 0
for line in lines:
    if line == '\n':
        continue
    line = line.replace('\n','')
    if count == 0:
        nameHolder = line
    elif count == 1:
        itemsHolder = line
    elif count == 2:
        operationHolder = line
    elif count == 3:
        testHolder = line
    elif count == 4:
        trueHolder = line
    elif count == 5:
        falseHolder = line
        monkeys.append(Monkey(nameHolder, itemsHolder, operationHolder, testHolder, trueHolder, falseHolder))
        monkeyBusinessList.append(0)
        count = 0
        continue
    count += 1

# Get the product of all the divisors
for monkey in monkeys:
    finalProduct = int(monkey.test) * finalProduct

# Run the loop for 10000 iterations
i = 0
for i in range(10000):
    print(i)
    for monkey in monkeys:
        itemCount = len(monkey.items)
        j = 0
        for j in range(itemCount):
            monkey.runOperation()
            newItem = monkey.boredItemChange()
            monkeys[monkey.runTest()].items.append(newItem)
            monkeyBusinessList[int(monkey.name)] += 1
            

print('finished')
mostMonkeyBusiness = max(monkeyBusinessList)
monkeyBusinessList.remove(mostMonkeyBusiness)
secondMostMonkeyBusiness = max(monkeyBusinessList)
print(mostMonkeyBusiness * secondMostMonkeyBusiness)
    
