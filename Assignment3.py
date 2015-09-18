import sys 

with open(sys.argv[1], "r") as world:
    maze = []
    for line in world.readlines(): 
        maze.append(line.rstrip('\n').split(' ')) 
         
print maze 

class Node: 

    def __init__(self, x, y):
        self.parent = None 
        self.toHere = None 
        self.toGo = None 
        self.x = x
        self.y = y 
        self.cost = None 

class Graph: 

    def __init__(self, maze):
        self.maze = maze
        self.start = Node(7,0)
        self.end = Node(0, 7)

    def astar(self, graph, start, end): 
        curropen.append(start)
        closed = []
        while len(curropen) != 0: 
        
