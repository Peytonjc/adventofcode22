print('Starting Solution 12...')

#Read input file as lines
with open('/workspaces/adventofcode22/Puzzle12/input.txt') as inputFile:
    lines = inputFile.readlines()

# Looks like today's deals with path algorithms. I'm quite rusty on those.
# Initialize variables to hold everything
height = len(lines)
width = len(lines[0].replace('\n',''))
heightMap = []
startPos = []
endPos = []
unvisitedNodes = []
visitedNodes = []
travelDict = dict()
startingNodes = []
shortestPaths = []

# Get start and ending positions. Conver the input from letters to numbers.
for i in range(height):
    line = lines[i].replace('\n', '')
    heightLine = []
    for j in range(width):
        char = line[j]
        if char == 'S':
            startPos = (i, j)
            char = 'a'
        elif char == 'E':
            endPos = (i, j)
            char = 'z'
        heightLine.append(ord(char) - ord('a'))
        unvisitedNodes.append((i, j))
        if char == 'a':
            startingNodes.append((i,j))
    heightMap.append(heightLine)

def resetAlgorithmVariables(unvisitedNodes, visitedNodes):
    unvisitedNodes = []
    visitedNodes = []
    for i in range(height):
        line = lines[i].replace('\n', '')
        heightLine = []
        for j in range(width):
            char = line[j]
            if char == 'S':
                startPos = (i, j)
                char = 'a'
            elif char == 'E':
                endPos = (i, j)
                char = 'z'
            heightLine.append(ord(char) - ord('a'))
            unvisitedNodes.append((i, j))

# Build the dictionary to hold the nodes that can be traveled to from a node, taking into account
# height of adjacent nodes
for i in range(height):
    for j in range(width):
        visitableNodes = []
        for m in [-1, 0, 1]:
            for n in [-1, 0, 1]:
                if 0 <= i+m < height and 0 <= j+n < width and abs(n)+abs(m) == 1:
                    if heightMap[i+m][j+n] - heightMap[i][j] <= 1:
                        visitableNodes.append((i+m, j+n))
        travelDict[(i, j)] = visitableNodes

# I found a class for Dijkstra's algorithm
class Dijkstra:
    def __init__(self, unvisited, visited, start_node, end_node, node_map):
        self.unvisited = unvisited
        self.visited = visited
        self.start_node = start_node
        self.end_node = end_node
        self.node_map = node_map
        # zip puts two lists together in a list of touples
        self.node_distance = dict(zip(unvisitedNodes, [999]*(height*width)))
        self.node_distance[start_node] = 0

    def visit_node(self, current_node):
        for node in self.node_map[current_node]:
            if node not in self.visited:
                if self.node_distance[current_node] + 1 < self.node_distance[node]:
                    self.node_distance[node] = self.node_distance[current_node] + 1
        self.unvisited.remove(current_node)
        self.visited.append(current_node)

    def run_dijkstras(self):
        while self.end_node not in self.visited:
            current_node = min(self.unvisited, key=self.node_distance.get)
            self.visit_node(current_node)
        return self.node_distance[self.end_node]

print("Running for " + str(len(startingNodes)) + " starting nodes...")
graphTwo = Dijkstra(unvisitedNodes, visitedNodes, startPos, endPos, travelDict)
shortestPaths.append(graphTwo.run_dijkstras())

graph = Dijkstra(unvisitedNodes, visitedNodes, startPos, endPos, travelDict)
print('Solution for Part 1:')
print(graph.run_dijkstras())
print('Solution for Part 2:')
print(min(shortestPaths))
