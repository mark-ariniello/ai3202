import sys 

with open(sys.argv[1], "r") as world:
    maze = [x.strip('\n').spilt(' ')  for x in world.readlines()] 
         
print maze 

