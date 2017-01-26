import sys
import random

dict={}
flag=0
newchessboard=[]
notcount=0
# global allcount
allcount=0
global fullcount 
fullcount = 0

def collisionscount(chessboard):
	count=0
	length=len(chessboard)
#row collisions
	for i in range(0,length-1):
		for j in range(i+1,length):
			# print i,j
			if (chessboard[i]==chessboard[j]):
				count=count+1
	# print count
	# print chessboard
	# print chessboard
	for i in range(0,length):
		temp=chessboard[i]
		tempi=i
		for j in range(1,len(chessboard)):
			dummy=temp-j
			downdummy=temp+j

			if(tempi>length-2):
				break
			if(downdummy==chessboard[tempi+1]):
				# print "downdiagnol"
				count=count+1
			if(dummy<1):
				break
		
			# print temp,j,dummy,chessboard[tempi+1],tempi
			if(dummy==chessboard[tempi+1]):
				# print "updiagnol"
				count=count+1
			
			tempi=tempi+1
	return count
			
def nextfunction(chessboard):
	global allcount
	global notcount
	global fullcount
	length=len(chessboard)
	heuristicvalue=collisionscount(chessboard)
	for i in range(0,length):
		already=chessboard[i]
		for j in range(1,length+1):
			# if ((j-1)!=already):
			chessboard[i]=j
			newheuristic = collisionscount(chessboard)
			if(newheuristic == 0):
				allcount=allcount+1
				if(fullcount < 10 ):
					print "This is a solution"
					print chessboard
					fullcount=fullcount+1
				return chessboard
			dict[i,j]= newheuristic
			# print dict
			# print chessboard
			# print newheuristic
			chessboard[i]=already
		
	k,l=min(dict,key=dict.get)
	result=dict[k,l]
	if(result >= heuristicvalue):
		if(fullcount < 10 ):
			print "Not a solution"
			print chessboard
			fullcount=fullcount+1
		notcount=notcount+1
		return chessboard
	# print k 
	# print l
	# print chessboard
	chessboard[k]=l
	# print chessboard
	# print collisionscount(chessboard)
	nextfunction(chessboard)
print "Enter the number of participants:"
input=int(raw_input())
print "Output for 1st 10 times"
for i in range (0,100):
	chessboard=[]
	for i in range(1,input+1):
		randvalue=random.randint(1,input)
		# print randvalue
		# print i
		chessboard.append(randvalue)
	# print chessboard
	# chessboard,allcount=nextfunction(chessboard,allcount)

	if (fullcount<10):
		print"Run Number: %s"%fullcount
		print chessboard
	
	nextfunction(chessboard)	
print "On Whole you got the solution for %s times"%allcount
# print notcount
		
# print heuristicvalue



	

