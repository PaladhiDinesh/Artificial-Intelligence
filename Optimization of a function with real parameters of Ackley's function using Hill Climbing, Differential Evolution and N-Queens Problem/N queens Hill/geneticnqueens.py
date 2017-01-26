import random
import copy
pop_dict={}	
child_new_dict={}
child_count=0
solution_count = 0
def collisionscount(chessboard):
	count=0
	length=len(chessboard)
	for i in range(0,length-1):
		for j in range(i+1,length):
			if (chessboard[i]==chessboard[j]):
				count=count+1
	for i in range(0,length):
		temp=chessboard[i]
		tempi=i
		for j in range(1,len(chessboard)):
			dummy=temp-j
			downdummy=temp+j

			if(tempi>length-2):
				break
			if(downdummy==chessboard[tempi+1]):
				count=count+1
			if(dummy<1):
				break
			if(dummy==chessboard[tempi+1]):
				count=count+1
			tempi=tempi+1
	return count
	
def crossoverfunction(list1,list2):
	otherlist=[]
	newlist=[]
	temp=[]
	length=len(list1)
	for i in range(3,length-(length/4)):
		newlist.append(list1[i])
	# print newlist
	for i in range(length-(length/4),length):
		if list2[i] not in newlist:
			otherlist.append(list2[i])
	for i in range(0,length-(length/4)):
		if list2[i] not in newlist:
			otherlist.append(list2[i])
	# print otherlist
	for i in range(0,length-(length-(length/4))):
		newlist.append(otherlist[i])
	for i in range(length-(length-(length/4)),len(otherlist)):
		temp.append(otherlist[i])
	newlist=temp+newlist
	# print newlist
	return mutationfunction(newlist)
	
def mutationfunction(list):
	length=len(list)
	temp=list[2]
	list[2]=list[length-3]
	list[length-3]=temp
	# print list
	return list
	
print "Please enter the participants count:"
n=int(raw_input())
for q in range(0,100):
	for i in range(child_count,100):
		dummy=random.sample(range(0,n),n)
		pop_dict[i]=dummy
	# print pop_dict
	# print pop_dict
	j=0
	p=0
	while (j<10):
		children = crossoverfunction(pop_dict[j],pop_dict[j+1])
		if (collisionscount(children)==0):
			print "solution",children
			#print children,"This is solution"
			solution_count=solution_count+1
		else:
			child_new_dict[p]=children
			p=p+1
		j=j+2
	pop_dict={}
	# print child_new_dict
	child_count= len(child_new_dict)
	pop_dict= copy.copy(child_new_dict)
	child_new_dict={}
	# print pop_dict
print solution_count
		# print j

# crossoverfunction([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],[15,16,13,6,12,1,10,9,4,14,3,11,2,5,7,8])
