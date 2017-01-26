import time
start_time = time.clock()
worddict={1:['LASER','STEER','SAILS','SHEET','HOSES'],2:['HOSES','LASER','STEER','SHEET','SAILS'],3:['STEER','LASER','SAILS','SHEET','LASER'],4:['HEEL','HIKE','KNOT','KEEL','LINE'],5:['HEEL','HIKE','KNOT','KEEL','LINE'],6:['AFT','EEL','ALE','LEE','TIE'],7:['AFT','EEL','ALE','LEE','TIE'],8:['HOSES','STEER','SAILS','SHEET','LASER']}
#global templist1
templist1=[]
templist2=[]
templist3=[]
templist4=[]
templist5=[]
templist6=[]
templist7=[]
answerdict={}
flag3=0
flag6=0
flag2=0
flag5=0
flag4=0
flag1=0

def word1():
	global flag1
	answerdict[1] = worddict[1][flag1]
	#print answerdict
	word2()

def word2():
	global flag1
	global flag2
	global flag3
	templist1=[]
	for k in range(0,5):
		if (worddict[2][k][0]==answerdict[1][2]):
			templist1.append(worddict[2][k])
	#print "templist1",templist1
	if not templist1:
		flag1=flag1+1
		word1()
	else:
		answerdict[2]=templist1[flag2]
		#print answerdict
		flag3=0
		word3()
		
def word3():
	global flag4
	global flag2
	global flag5
	global flag1
	global templist2
	#print "entered flag3"
	#print "flag3",flag3
	if (flag3 < len(templist2) or flag3 == 0):
		templist2=[]
		for l in range(0,5):
			if (worddict[3][l][0]==answerdict[1][4]):
				templist2.append(worddict[3][l])
		#print "templist2",templist2	
		if not templist2:
			flag1=flag1+1
			word1()
		else:
			flag4=0
			flag5=0
			answerdict[3]=templist2[flag3]
			#print "at word3",answerdict
			word4(flag4)
	else:
		flag2=flag2+1
		#print "flag2",flag2
		word2()
def word4(flag4):
	global flag3
	global flag6
	global flag5
	global templist3
	#print "mine",answerdict
	#print "flag4",flag4
	#print "flag5 in word4", flag5
	if (flag4 < len(templist3) or flag4 == 0):
		templist3=[]
		for m in range(0,5):
			if(worddict[4][m][1]==answerdict[2][2] and worddict[4][m][3]==answerdict[3][2]):
				templist3.append(worddict[4][m])
		#print templist3
		if not templist3:

			flag3=flag3+1
			word3()
		else:
			#print flag4
			if (flag6 >4):
				del answerdict[flag6]
				flag6=0	
			#print templist3[flag4]
			answerdict[4]=templist3[flag4]
			word5(flag5)
	else:
		flag3=flag3+1
		#print "flag3",flag3
		word3()


def word5(dummyflag5):

	global flag6
	global templist4
	global flag4
	global flag5

	#print "flag6",flag6
	#print "flag5",flag5
	#print answerdict
	#print len(templist4)
	if (flag5 < len(templist4) or flag5 == 0):
		templist4=[]
		for n in range(0,5):
			if(worddict[5][n][0]==answerdict[4][2]):
				templist4.append(worddict[5][n])
		#print templist4
		if not templist4:
			del answerdict[4]
			word4(flag4)
		else:

			answerdict[5]=templist4[flag5]
			#print "k",answerdict[5]
			word6(flag6)
	else:
		flag4=flag4+1
		#print "flag4",flag4
		#print "entered flag4"
		#print "flag5=" + str(flag5)
		word4(flag4)

def word6(flag6):
	global templist5
	global flag5
	#print flag6
	#print len(templist5)
	if (flag6 < len(templist5) or flag6 == 0):
		templist5=[]
		for o in range(0,5):
				templist5.append(worddict[6][o])
		#print templist5

		answerdict[6]=templist5[flag6]
		#print "new",answerdict[6]
		word7()
	else:
		#print "entered word5"
		flag5=flag5+1
		#print "flag5",flag5
		#print answerdict
		word5(flag5)

def word7():
	global templist6
	#print answerdict
	global flag4
	global flag5
	global flag6
	templist6=[]
	for p in range(0,5):
		if(worddict[7][p][0]==answerdict[2][3] and worddict[7][p][1]==answerdict[5][1] and worddict[7][p][2]==answerdict[3][3]):
			templist6.append(worddict[7][p])

	#print templist6
	if not templist6:
		#print templist5
		flag5=flag5+1
		#print "flag5",flag5
		flag6=0
		word5(flag5)
	else:
		answerdict[7]=templist6[0]
		flag5=0
		word8()
def word8():
	global flag6
	global flag5
	#print answerdict[6]
	for q in range(0,5):	
		if (worddict[8][q] not in answerdict.values()):
			#print worddict[8][q]
			#print answerdict
			if(worddict[8][q][0]==answerdict[6][1] and worddict[8][q][2]==answerdict[2][4] and worddict[8][q][3]== answerdict[5][2] and worddict[8][q][4]== answerdict[3][4]):
				templist7.append(worddict[8][q])
	#print "hi"
	#print "result",	templist7
	#print "answerdict",answerdict
	if not templist7:
	  	flag6=flag6+1
		del answerdict[6]
		del answerdict[7]
		flag5=flag5+1	
		#print "hahahahahahahahahahahahah"
		word6(flag6)
	else:
		print "my answer"
		answerdict[8]=templist7[0]
		print answerdict


word1()	
print time.clock() - start_time, "seconds"