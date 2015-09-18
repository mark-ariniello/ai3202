#Mark Ariniello 
#python 2.7.6

#Queue 

import Queue 

# create Queue
q = Queue.Queue() 
q.put(48) 
q.put(1)
q.put(2)
q.put(3) 
q.put(4)
q.put(5) 
q.put(6) 
q.put(7)
q.put(8) 
q.put(9)
q.put(10)

#print and dequeue each item in the Queue 

print("dequeuing: ") 
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())


#stack 

class Stack:
 
    def __init__(self):
        self.list = []
        self.size = 0
 
    def push(self, item):
        self.list.append(item)
        self.size = self.size + 1  

    def pop(self): 
        self.list.pop()
        self.size = self.size - 1
 
    def checkSize(self):
        return self.size 

#test 

#Create and push the stack
x = Stack()
x.push(5)
x.push(54)
x.push(3)
x.push(9)
x.push(27)
x.push(81)
x.push(243)
x.push(729)
x.push(2187)
x.push(6561)

#print and pop each value in the stack 
print("The stack is now: ")
print(x.list)
print("The Stack has size: ")
print(x.checkSize())
print("Popping") 
x.pop()
print(x.list) 
print("Popping")
x.pop()
print(x.list)
print("Popping")
x.pop()
print(x.list)
print("Popping")
x.pop()
print(x.list)
print("Popping")
x.pop()
print(x.list)
print("Popping")
x.pop()
print(x.list)
print("Popping")
x.pop()
print(x.list)
print("Popping")
x.pop()
print(x.list)
print("Popping") 
x.pop() 
print(x.list)
print("Popping")
x.pop()
print(x.list)

#binary tree 

class Node: 
   
    def __init__ (self, parentValue, value):
        self.parentValue = parentValue  
        self.right = None 
        self.left = None 
        self.value = value

class BinaryTree:
   
    def __init__ (self, value):
       self.root = Node(None, value)
      
    def add (self, value, parentValue):
        if parentValue == self.root.value:        
            if self.root.left == None:
                self.root.left = Node(self.root, value)
                return None     
            if self.root.right == None: 
                self.root.right = Node(self.root, value)
                return None
            else: 
                print("Node already has 2 children")
                return None 
        else: 
            self.target = self.find(self.root, parentValue)
            
            if self.target == None: 
                print("target value not in graph")
                return None 
            if self.target.left == None: 
                self.target.left = Node(self.target, value) 
                return None
            if self.target.right == None: 
                self.target.right = Node(self.target, value) 
                return None
            else: 
                print("Node already has 2 children")
                return None

    def find (self, parentNode, targetValue): 
        if parentNode.value == targetValue: 
            print("targetValue is: ")
            print(targetValue)
            print("parentNode value is: ") 
            print(parentNode.value) 
            return parentNode 
        if parentNode.left != None:
            self.find(parentNode.left, targetValue)
            return None
        if parentNode.right != None: 
            self.find(parentNode.right, targetValue)
            return None 
        else : 
            print ("Target Value not Found")
            return None 
    
#    def goleft (self, i
            
        
y = BinaryTree(0)
y.add(1,0) 
y.add(2,0) 
y.add(3,1)
y.add(4,1)
y.add(5,1)
print y.root.left.value
print y.root.right.value 
print y.root.left.left.value
#graph  

class Graph: 
    
    def __init__ (self): 
        self.graph = {};

    def addVertex (self, value): 
        if self.graph.get(value) == None:
            self.graph[value] = []

    def addEdge (self, value1, value2): 
        if self.graph.has_key(value1) and self.graph.has_key(value2): 
            self.graph[value1].append(value2) 
            self.graph[value2].append(value1)
        else:
            print("One or more vertices not found")

    def findVertex(self, value): 
        print(self.graph[value])

#create and populate all the verticies 

g = Graph()
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addVertex(8)
g.addVertex(9)
g.addVertex(10)

#make sure all verticies are added

print("All Verticies in the graph")
print(g.graph.keys())  
             
#populate all edges 

g.addEdge(1, 2) 
g.addEdge(1, 3) 
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(1, 6) 
g.addEdge(1, 7) 
g.addEdge(1, 8) 
g.addEdge(1, 9) 
g.addEdge(1, 10) 
g.addEdge(2, 10) 
g.addEdge(2, 3) 
g.addEdge(3, 4) 
g.addEdge(3, 7) 
g.addEdge(4, 7) 
g.addEdge(5, 7)
g.addEdge(6, 5)
g.addEdge(6, 2)
g.addEdge(7, 6)
g.addEdge(8, 9)
g.addEdge(9, 10)

#make sure all edges have been added 

print("all edges and verticies in the graph:")
print(g.graph.items())         

#print the Conections for verticie 1 

print("findVertex test: ")
g.findVertex(1)
