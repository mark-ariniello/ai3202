#Mark Ariniello

# Program not really working, but I would guess that as e go loarger you would exit sooner, which could potentially change the path.

import sys
import numpy

#help from http://artint.info/html/ArtInt_227.html

#import the world
with open(sys.argv[1], "r") as maze:
    world = []
    for line in maze.readlines():
        world.append(line.rstrip('\n').split(' '))  
    
class MDP:
	def __init__(self, world, epsilon, discount): 
		self.up = 0
		self.down = 0
		self.left = 0
		self.right = 0
		self.gammafinal = (epsilon*(1-discount))/discount 
		self.world = world
		self.rewards = [[0 for x in range(10)] for y in range(8)]
		self.utility = [[0 for x in range(10)] for y in range(8)]
		
		#set the value for the start state
		for i in range(8): 
			for j in range(10):
				#print("CurrentValue is: ")
				currentValue = int(world[i][j])
				print currentValue 
				if currentValue == 1: 
					self.rewards[i][j] = -1
				if currentValue == 2: 
					self.rewards[i][j] = None
				if currentValue == 3:
					self.rewards[i][j] = -2
				if currentValue == 4:
					self.rewards[i][j] = 1
				if currentValue == 50: 
					self.rewards[i][j] = 50
				print self.rewards
		
		self.uprime = 0
		self.gamma = 1
		self.utility = self.rewards
		while (self.gamma > self.gammafinal): 
			for i in range(8):
				for j in range(10):
					
					print self.rewards[i][j]
					if self.rewards[i][j] != None and self.rewards[i][j] == 0: 
						self.uprime = self.maximize(i, j, self.rewards, discount)
						print
						#print ("potential new gamma: ")
						print (abs(self.uprime - self.utility[i][j]))
					#print ("gamma to test against: ")
						print self.gammafinal
					#	print ("current gamma: ")
						print self.gamma
						self.gamma = 0
						if abs(self.uprime - self.utility[i][j]) > self.gamma :
							self.gamma = abs(self.uprime - self.utility[i][j])
							#print("self.gamma new assignment is: ") 
							#print self.gamma
						self.utility[i][j] = self.uprime
			#print ("self.uprime is: ")
			print self.uprime
			print self.utility
			
			
				
		#print world 
	def maximize (self, row, column, rewards, discount):
		if (row + 1) < 8 :
			if rewards[row + 1][column] != None:
				self.up = rewards[row + 1][column]
		else : self.up = rewards[row][column]
		if (row - 1) >= 0 :
			if rewards[row - 1][column] != None:
				self.down = rewards[row - 1][column]
		else : self.down = rewards[row][column]
		if (column + 1) < 10 :
			if rewards[row][column + 1] != None: 
				self.right = rewards[row][column + 1]
		else : self.right = rewards[row][column]
		if (column - 1) >= 0 :
			if rewards[row][column -1] != None: 
				self.left = rewards[row][column - 1]
		else : self.left = rewards[row][column]
	
		possible = [(.8*self.up + .1*self.left + .1*self.right), (.8*self.down + .1*self.left + .1*self.right), (.8*self.right + .1*self.up + .1*self.down), (.8*self.left + .1*self.up + .1*self.down)]
		self.uprime = self.rewards[row][column] + discount*max(possible)
		print ("self.uprime in maximize is: ")
		print self.uprime
		return self.uprime
		
		
				
	#def value(states, actions, rewards, values, gamma, niter):
		
	#def 
x = MDP(world, .5, .9) 
