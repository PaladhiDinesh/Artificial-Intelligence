file = open('Words.txt','r')
# for line in file:
# 	print line
wordcountdict={1:{'a':3,'d':8},
2:{'d':3},
3:{'d':4},
4:{'a':3,'d':4},
5:{'d':3},
6:{'d':8},	
7:{'a':5,'d':6}, 
8:{'d':5},
9:{'a':5,'d':5},
10:{'d':6},
11:{'a':5,'d':5},
12:{'a':5,'d':4},
13:{'a':3,'d':3},
14:{'a':5},
15:{'d':3},
16:{'a':3},	
17:{'d':3},
18:{'a':4},
19:{'d':5},
20:{'a':3},
21:{'a':4,'d':5},
22:{'a':4},
23:{'a':3},
24:{'a':4},
25:{'a':4},
26:{'d':4},
27:{'a':4,'d':4},
28:{'a':4},
29:{'d':4},
30:{'a':4,'d':4},
31:{'a':7},
32:{'d':4},
33:{'a':5}}
print wordcountdict[12]['a']
# positiondict={1:['a',]}
dependencies={1:{'a':[2,3],'d':[7,11,13,18,22,25,28]},
2:{'a':[1,3],'d':[7,11]},
3:{'a':[],'d':[]},
4:{'a':[],'d':[]},
5:{'a':[],'d':[]},
6:{'a':[],'d':[]},
7:{'a':[],'d':[]},
8:{'a':[],'d':[]},
9:{'a':[],'d':[]},
10:{'a':[],'d':[]},
11:{'a':[],'d':[]},
12:{'a':[],'d':[]},
13:{'a':[],'d':[]},
14:{'a':[],'d':[]},
15:{'a':[],'d':[]},
16:{'a':[],'d':[]},
17:{'a':[],'d':[]},
18:{'a':[],'d':[]},
19:{'a':[],'d':[]},
20:{'a':[],'d':[]},
21:{'a':[],'d':[]},
22:{'a':[],'d':[]},
23:{'a':[],'d':[]},
24:{'a':[],'d':[]},
25:{'a':[],'d':[]},
26:{'a':[],'d':[]},
27:{'a':[],'d':[]},
28:{'a':[],'d':[]},
29:{'a':[],'d':[]},
30:{'a':[],'d':[]},
31:{'a':[],'d':[]},
32:{'a':[],'d':[]},
33:{'a':[],'d':[]}}


copyworddict=copy.deepcopy(wordcountdict)
domaindict=copy.deepcopy(copyworddict)
answerdict={}
value=1

def backtrack(copyworddict):
	global domaindict
	if (domaindict == {}):
		print answerdict
		print time.clock() - start_time, "seconds"
		exit()
	global value
	
	# print value,"global value"

	for o in domaindict:
		min=len(domaindict[o])
		value =o
		break
	# print domaindict
	for i in domaindict:
		# print min,"minimum value"
		# print i

		if (len(domaindict[i])<min):
			min=len(domaindict[i])
			value=i
	# print value,"value"
	
	for k in copyworddict[value]:
		flag=1
		for j in dependencies[value]: 
			if(flag==1): 
				# print j,"j value"
				wholedepvalue=wholedependencies[value][j]
				othersidevalue=wholedependencies[j][value]
				# print wholedepvalue
				# print othersidevalue
				for h in copyworddict[j]:
					# print k,h
					if (k[wholedepvalue]==h[othersidevalue]):
						flag=1
						break
					else:
						flag=0

		if flag==1:
			break
	answerdict[value]=k
	# print answerdict,"Answers"
	forwardchecking(k,value,copyworddict)
	domaindict=copy.deepcopy(copyworddict)
	for t in answerdict:
		domaindict.pop(t)
	# print domaindict
	global worddict
	worddict=copy.deepcopy(copyworddict)
	backtrack(copyworddict)




def forwardchecking(k,value,copyworddict):
	for j in dependencies[value]: 
		wholedepvalue=wholedependencies[value][j]
		othersidevalue=wholedependencies[j][value]
		# print wholedepvalue
		# print othersidevalue

		# print worddict
		for h in worddict[j]:
			# print k,h
			if (k[wholedepvalue]==h[othersidevalue]):
				continue	
			else:
				copyworddict[j].remove(h)
				# print copyworddict
	return copyworddict
backtrack(copyworddict)




# print dependencies[1]['a'][0]
# def backtrack(wordcountdict):
# 	for i in range(1,2):
# 		# print len(wordcountdict[i])
# 		for j in range(len(wordcountdict[i])):
# 			# print i
# 			print wordcountdict[i][j]

# backtrack(wordcountdict)

