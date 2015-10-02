#Mark Ariniello

import sys
import numpy

#help from http://artint.info/html/ArtInt_227.html

#import the world
with open(sys.argv[1], "r") as maze:
    world1 = []
    for line in maze.readlines():
        world1.append(line.rstrip('\n').split(' '))

#print world

#import epsilon
epsilon = sys.argv[2] 
discount = 0.9
gamma = .9 #(epsilon*(1-discount))/discount 	
                     
#class for Markov Decisiocon Process                       
class MDP: 
	def __init__(self, world):
	    self.world = world
	    self.policy = [[[0,'nodirection'] for x in range(10)] for x in range(8)] 
	
	def reward(self, row, column):
		#print "called reward!"
		sum = []
		for i in range(-1, 2):
			if row + i >= 0 and row + i <= 9 and i != 0 : 
				obstacle = int(self.world[row + i][column])
				reward = 0
				if obstacle != 2: 
					if obstacle == 1:
						reward = -1.0
					if obstacle == 3:
						reward = -2.0
					if obstacle == 4: 
						reward = 1
					if obstacle == 50:
						reward = 50
					if reward * gamma > self.policy[row][column][0] or self.policy[row][column][0] == 0:
						self.policy[row][column][0] = reward * gamma
						if i == 1 : 
							self.policy[row][column][1] = 'left'
						else : 
						    self.policy[row][column][1] = 'right' 
						    
			if column + i >= 0 and column + i <=9 and i != 0: 
				obstacle = int(self.world[row][column + i])
				reward = 0
				if obstacle != 2: 
					if obstacle == 1: 
					    reward = -1.0
					if obstacle == 3:
						reward = -2.0
					if obstacle == 4: 
						reward = 1
					if obstacle == 50:
						reward = 50
					if reward * gamma > self.policy[row][column][0] or self.policy[row][column][0] == 0:
						print gamma
						print i
						self.policy[row][column][0] = reward * gamma
						if i == 1 : 
							self.policy[row][column][1] = 'up'
						if i == -1 : 
						    self.policy[row][column][1] = 'down' 
					#print self.policy 	
	
	def solve(self):
		#print "called solve"
		
		for i in range(0, 7):
			for j in range(9, 0, -1):
				self.reward(i, j)		
                
			
	#def transition(self, s, action):
		
	
		
			
maze = MDP(world1)
maze.solve()	
print maze.policy
	
			
