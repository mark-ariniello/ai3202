import sys 

with open(sys.argv[1], "r") as world:
    maze = []
    for line in world.readlines(): 
        maze.append(line.rstrip('\n').split(' ')) 
         
print maze 

class Node: 

    def __init__(self, x, y, parent, toHere):
        self.parent = parent
        self.toHere = toHere 
        self.toGo = (9 - x + 7 - y) * 10  
        self.x = x
        self.y = y 
        self.cost = toHere + toGo

class Graph: 

    def __init__(self, maze):
        self.maze = maze
        self.start = Node(7,0)
        self.end = Node(0, 9)

    def astar(self, graph, start, end): 
        curropen.append(start)
        closed = []
        currnode = start
        while len(curropen) != 0:
            for node in curropen: 
                if node.toHere < x:
                    x = node.toHere + node.toGo
            curropen.remove(currnode)
            if currnode != end: 
                closed.append(currnode)
                for i = -1 to i = 1: 
                    for j = -1 to j = 1:
                        if (currnode.x + i) >= 0 and (currnode.x + i) <= 9 and (currnode.y + j) >= 0 and (currnode.y + j) <= 7 and (i !=0 and j !=0) and maze[currnode.x + i][currnode.y + j] != 2: 
                            node = Node(currnode.x + i, currnode.y + j, currnode, currnode.toHere + 0) 
                            if i == 0 or j == 0: 
