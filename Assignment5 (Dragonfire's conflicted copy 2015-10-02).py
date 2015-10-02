import sys
import numpy

#help from http://artint.info/html/ArtInt_227.html

with open(sys.argv[1], "r") as maze:
    world = []
    for line in maze.readlines():
        world.append(line.rstrip('\n').split(' '))

#print world

epsilon = sys.argv[2] 
discount = 0.9
gamma = .9 #(epsilon*(1-discount))/discount 	
                                           
class MDP: 
	def __init__(self, world):
	    self.world = world
	    self.policy = [[[0,'nodirection'] for x in range(10)] for x in range(10)] 
	    self.reward = 50 
	
	def solve(self):
	    for i in range(0, 7):
		    for j in range(9, 0): 
			    newstate = reward(i, j)
			
	#def transition(self, s, action):
		
	def reward(self, row, column ):
		
		sum = []
		
		for i in range(-1, 1):
		    if row + i >= 0 and row + i <=7 and i != 0: 
				obstacle = world[row + i][column]
				reward = 0
				if obstacle != 2: 
					if obstacle == 1: 
					    reward = -1.0
					if obstacle == 3:
						reward = -2.0
					if obstacle == 4: 
						reward = 1
					if reward * gamma < policy[row][column][0]:
						policy[row][column][0] = reward * gamma
						if i == 1 : 
							policy[row][column][1] = 'left'
						else : 
						    policy[row][column][0] = 'right' 
					print policy 
		
			
maze = MDP(world)
maze.solve()		
print maze.policy
	
			
