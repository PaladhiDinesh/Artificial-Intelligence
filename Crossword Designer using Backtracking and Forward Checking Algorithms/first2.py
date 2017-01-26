import copy
import sys
import time
start_time = time.clock()
worddict={1:['LASER','STEER','SAILS','SHEET','GOSES','HOSES'],2:['HOSES','LASER','STEER','SHEET','SAILS'],3:['STEER','LASER','SAILS','SHEET','HOSES'],4:['HEEL','HIKE','KNOT','KEEL','LINE'],5:['HEEL','HIKE','KNOT','KEEL','LINE'],6:['AFT','EEL','ALE','LEE','TIE'],7:['AFT','EEL','ALE','LEE','TIE'],8:['HOSES','STEER','SAILS','SHEET','LASER']}
dependencies={1:[2,3],2:[1,4,7,8],3:[1,4,7,8],4:[2,3,5],5:[4,7,8],6:[8],7:[2,3,5],8:[6,2,3,5]}
wholedependencies={1:{2:2,3:4},2:{1:0,4:2,7:3,8:4},3:{1:0,4:3,7:3,8:4},4:{2:1,3:3,5:2},5:{4:0,7:1,8:2},6:{8:1},7:{2:0,3:2,5:1},8:{6:0,2:2,3:4,5:3}}
copyworddict=copy.deepcopy(worddict)
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


