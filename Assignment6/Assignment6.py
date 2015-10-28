import sys
import getopt

def main():
	x = Bayesnet()
	try:
		opts, args = getopt.getopt(sys.argv[1:], "m:g:j:p:")
	except getopt.GetoptError as err:
		# print help information and exit:
		print str(err) # will print something like "option -a not recognized"
		sys.exit(2)
	for o, a in opts:
		if o in ("-p"):
			print "flag", o
			print "args", a
			print a[0]
			print float(a[1:])
			if a[0] == 'S' :
				x.net[0].node['marginal'] = float(a[1:])
				print x.net[0].node
			elif a[0] == 'P' : 
				x.net[1].node['marginal'] = float(a[1:]) 
				print x.net[1].node
			#setting the prior here works if the Bayes net is already built
			#setPrior(a[0], float(a[1:])
		elif o in ("-m"):
			print "flag", o
			print "args", a
			print type(a)
			marg(x, a)
			#calcMarginal(a)
		elif o in ("-g"):
			print "flag", o
			print "args", a
			print type(a)
			'''you may want to parse a here and pass the left of |
			and right of | as arguments to calcConditional
			'''
			p = a.find("|")
			print a[:p]
			print a[p+1:]
			#calcConditional(a[:p], a[p+1:])
		elif o in ("-j"):
			print "flag", o
			print "args", a
		else:
			assert False, "unhandled option"

    
    # ...

def marg(net, event):
	answer = 0
	smoker = net.net[0].node['marginal']
	pollution = net.net[1].node['marginal']
	print 1 - pollution
	if event is 's' or event is 'S' :
		print ("marginal probablility of smoking is: ") 
		print smoker

	elif event is 'p' or event is 'P': 
		print ("marginal probablility of low pollution is: ")
		print pollution

	elif event is 'c' or event is 'C' :
		answer = net.net[2].node['conditional'][0][1]*smoker*(1-pollution) + net.net[2].node['conditional'][1][1]*smoker*pollution + net.net[2].node['conditional'][2][1]*(1-smoker)*(1-pollution) + net.net[2].node['conditional'][3][1]*(1-smoker)*pollution
		print answer 

	


class Node: 
	def __init__(self, name, parent): 
		self.node = {'name' : name, 'parent' : parent, 'child' : None, 'marginal' : 0.0 , 'conditional' : []}
		print (self.node)
		print ("made it to Node creation") 
		

class Bayesnet: 
	def __init__(self): 
		# create dictonaries for all nodes in the chart. 
		smoker = Node('smoker', None)
		smoker.node['marginal'] = 0.3
		pollution = Node('pollution', None)
		pollution.node['marginal'] = 0.9
		cancer = Node('cancer', [smoker, pollution])
		xray = Node('xray', cancer) 
		breath = Node('breath', cancer)
		cancer.node['child'] = [xray, breath]
		smoker.node['child'] = cancer
		pollution.node['child']= cancer 
		cancer.node['conditional'] = [["sh", .05],["sl", .03],["~sh", .02],["~sl", .001]]
		xray.node['conditional'] =[["true", .9],["false", .2]]
		breath.node['conditional'] = [["true", .65],["false", .3]]

		self.net = [smoker, pollution, cancer, xray, breath] 
	
	#def cprob(a,b): 
		
			
if __name__ == "__main__":
    main()
