import sys 

with open(sys.argv[1], "r") as world:
    maze = [x.strip('\n') for x in world.readlines()] 
        
print maze 

