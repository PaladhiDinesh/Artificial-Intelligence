import random
import copy
import math
f=open("outputdiff.txt","w")
np=10
nc=100
F=0.8
CR=0.1
dummy=[]
dict={}
newdict={}


def funcval(x,y):
	fun= (-20)*math.exp(-0.2*math.sqrt(0.5*((x*x)+(y*y)))) - math.exp(0.5*(math.cos(math.radians(2*180*x))+math.cos(math.radians(2*180*y))))
	return fun

for i in range(0,100):
	outputlist=[]
	for l in range (0,np):
		x=random.uniform(-5,5)
		y=random.uniform(-5,5)
		newdict[l]=(x,y)

	# print newdict
	for k in range(0,nc):
		dict=newdict.copy()
		for i in range(0,np):
			a= random.sample(range(0,np),3)
			while True:
				if i not in a:
					dummy=a
					# print dummy
					break
				else:
					a= random.sample(range(0,np),3)
			# print dummy
			# print dict[dummy[0]]
			v1=dict[dummy[0]][0]+(F*(dict[dummy[1]][0]-dict[dummy[2]][0]))
			v2=dict[dummy[0]][1]+(F*(dict[dummy[1]][1]-dict[dummy[2]][1]))		
			# # v1,v2=dict[dummy[0]]+(F*(dict[dummy[1]]-dict[dummy[2]]))
			# print (v1,v2)
			# for j in range(0,2):
			u=random.uniform(0,1)
				# print u
			if(u<CR):
				U1=v1
			else:
				U1=dict[i][0]
			u=random.uniform(0,1)
				# print u
			if(u<CR):
				U2=v2
			else:
				U2=dict[i][1]
			# print (U1,U2)
			newval=funcval(U1,U2)
			oldval=funcval(dict[i][0],dict[i][1])
			# print newval,oldval
			if (newval<oldval):
				newdict[i]=(U1,U2)
			else:
				newdict[i]=(dict[i][0],dict[i][1])
						
	# print newdict
	for i in range(0,10):
		outputlist.append(funcval(newdict[i][0],newdict[i][1]))
	# print outputlist
	globaloutputlist= min(outputlist)
	f.write("\n"+str(globaloutputlist))
	print globaloutputlist

	
	
f.close()