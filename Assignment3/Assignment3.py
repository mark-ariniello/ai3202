import sys 

with open(sys.argv[1], "r") as world:
    maze = []
    for line in world.readlines(): 
        maze.append(line.rstrip('\n').split(' ')) 
         
#print maze 

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
        self.start = Node(7,0, None, 0)
        self.end = Node(0, 9, None, 160)

    def astar(self): 
        curropen.append(start)
        closed = []
        currnode = start
        lowestnode = start
        x = 20
        while len(curropen) != 0:
            for node in curropen: 
                if node.toHere < x:
                    x = node.toHere + node.toGo
                open.remove
            curropen.remove(currnode)
            if currnode != end: 
                closed.append(currnode)
                for i in range (-1, 1): 
                    for j in range (-1, 1):
                        if (currnode.x + i) >= 0 and (currnode.x + i) <= 9 and (currnode.y + j) >= 0 and (currnode.y + j) <= 7 and (i !=0 and j !=0) and maze[currnode.x + i][currnode.y + j] != 2: 
                            node = Node(currnode.x + i, currnode.y + j, currnode, currnode.toHere + 0) 
                            if i == 0 or j == 0:
                                node = Node(currnode.x + i, currnode.y + j, currnode, currnode.toHere + 10)
                            if i != 0 and j != 0: 
                                node = Node(currnode.x + i, currnode.y + j, currnode, currnode.toHere + 14)
                            if maze[currnode.x + i][currnode.y + j] == 1: 
                                node.toHere = node.toHere + 10
                            if node.cost < lowestnode.cost and (node.x != 0 and node.y != 0): 
                                lowestnode = node
                open.append(node)
            else: 
                return closed        
        print closed 

x = Graph(maze)
x.astar()  
