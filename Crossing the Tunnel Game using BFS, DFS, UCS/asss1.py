import sys	
from itertools import combinations
import copy
from collections import OrderedDict
from operator import itemgetter

num = input('Enter the number of participants: ')
participants=[]
for i in range(num):
	print "Enter the weight for {}th participant".format(i)
	a=int(raw_input())
	participants.append(a)	
# #to get 1st level child nodes
list_child = []
temp_list=[]
dict_all={}
dict_parent={}
dict_child={}
dict_cost ={}
global count
participantsall=participants +['%']
list_child.append(participantsall)
dict_all[1]=participantsall
count = 1
parent = []
for p in combinations(participants,2):
	for element in participants:
		if element not in p:
			if "%" in p:
				p = (element,) + p
			else:
				dict_cost[count+1] = max(p)
				p = ('%',) + p
				p = (element,) + p 
	parent.append(count+1)
	count=count+1
	dict_child[count] = 1
	# dict_cost[count] =
	dict_all[count]=list(p)
	
	list_child.append(list(p)) 
dict_parent[1] = parent
def forward(mynext,count1):
	list_dummy =[]
	a=mynext
	# print a
	y=a.index('%')
	b= a[:y]
	for u in combinations(b,2):
		global count
		u=list(u)
		dict_cost[count+1] = max(u)
		# print u
		c=copy.copy(a)
		# print a
		# print c
		for i in u:
			# print u
			# print i
			c.remove(i)
		for i in u :
			c.append(i)
			# print a
		list_child.append(c)
		# print count 
		# print c 
		count=count+1
		dict_child[count] = count1
		list_dummy.append(count)
		dict_all[count]=c
		# if(c[0]=='%'):
			# break
		# backtrack(c)
	# print list_dummy
	dict_parent[count1]= list_dummy
	# del list_dummy[:]
	return count
count1=2
def backtrack(b,count1):
	list_dummy =[]
	y=b.index('%')
	a=b[y+1:]
	for p in combinations(a,1):
		global count
		p=list(p)
		# print p	
		dict_cost[count+1] = max(p)
		f=copy.copy(b)
		# print type(b)
		for i in p:
			
			f.remove(i)
			f=[i]+f
			# print f
			list_child.append(f)
			count=count+1
			dict_child[count] = count1
			list_dummy.append(count)
			dict_all[count]=f
			# print count
	# print count1
	# print list_dummy
	dict_parent[count1]= list_dummy		
	# del list_dummy[:]
	return list_child

def bfs():	
	queue_list = []
	parent=[]
	i=1
	queue_list.append(i)
	# print parent
	while True:
		if (dict_all[queue_list[0]][0]=='%'):
			parent.append(queue_list[0])
			b=queue_list[0]
			while True:
				a=dict_child[b]
				parent.append(a)
				b=a
				# print a
				if(a == 1):
					break
			break
		temp = queue_list[0]
		queue_list.pop(0)
		queue_list=queue_list+dict_parent[temp]
	# print parent	
	length =len(parent)
	parent.reverse()
	sum=0
	for c in range (0,length):
		a=parent[c]
		if (c>0):
			v=dict_cost[a]
			sum = sum + v
			print "Stage %s takes %s seconds" %(c,v)
		print dict_all[a]
	print "Total Time taken to pass all the people from one end to other end is %s"%sum
		# print sum
	
	
def dfs():
	stack_list = []
	new_parent=[]
	i=1
	stack_list.append(i)
	while True:
		if(dict_all[stack_list[0]][0]=='%'):
			# print "hi"
			new_parent.append(stack_list[0])
			b=stack_list[0]
			# print new_parent
			while True:
				# print i
				a=dict_child[b]
				new_parent.append(a)
				b=a
				# print new_parent
				if (a==1):
					break
			break
		temp = stack_list[0]
		stack_list.pop(0)
		# print stack_list
		# print dict_parent[temp]
		stack_list=dict_parent[temp]+stack_list
		
		# print stack_list
	# new_parent.append(1)
	# print new_parent
	length =len(new_parent)
	new_parent.reverse()
	sum=0
	for c in range (0,length):
		a=new_parent[c]
		if (c>0):
			v=dict_cost[a]
			sum = sum + v
			print "Stage %s takes %s seconds" %(c,v)
		print dict_all[a]
	print "Total Time taken to pass all the people from one end to other end is %s"%sum

def ucs():
	pri_que_list =[]
	dummy = []
	new_list=[]
	i=0
	pre_dict={}
	dummy=dict_parent[1]
	# print dummy
	for i in dummy:
		pre_dict[i]=dict_cost[i]
	# print pre_dict
	b= sorted(pre_dict.items(),key=lambda t:t[1])
	while True:
		c=b[0][0]
		del pre_dict[c]
		# print "after deleting"
		# print pre_dict
		# print b
		for i in dict_parent[c]:
			# print i
			pre_dict[i]=dict_cost[i]+b[0][1]
		# print"puttin new value"
		# print pre_dict
		b= sorted(pre_dict.items(),key=lambda t:t[1])
		h=b[0][0]
		if(dict_all[h][0]=='%'):
			# print h
			# print b[0][1]
			new_list=[h]
			while True:
				z=dict_child[h]
				new_list.append(z)
				h=z
				if(h==1):
					break
			# print new_list
			break
	length =len(new_list)
	new_list.reverse()
	sum=0
	for c in range (0,length):
		a=new_list[c]
		if (c>0):
			v=dict_cost[a]
			sum = sum + v
			print "Stage %s takes %s seconds" %(c,v)
		print dict_all[a]
	print "Total Time taken to pass all the people from one end to other end is %s"%sum
	
	# print c
		# print pre_dict
	# pre_dict = OrderedDict(sorted(pri_dict.items(),key=itemgetter(1)))
	# print pre_dict
	# child = pre_dict[1]
	# for i in dict_child[child]:
		# print i
	# print pre_dict
	
	# from operator import itemgetter
	# print pri_dict
	# a=min(pri_que_list)
	# print a
	# print dict_parent[a]
	
	
counttt = 0
while True:
	count2=count
	for i in range(count1-1,count2):
		# print i
		b=list_child[i]
		# print b
		# flag=len(list_child)
		# print b
		k= backtrack(b,i+1)
	count1= count2+1
	count2= count
	
	# print count1
	for i in range(count1,count2+1):
		forward(dict_all[i],i)
		# print dict_all[i]
		temp_list=dict_all[i]
	if(dict_all[count][0]=='%'):
		break	
	count1= count2+1
	counttt=counttt+1
# for d,e in dict_all.items():
	# print (d,e)

# for d,e in dict_parent.items():
	# print (d,e)
	
# for d,e in dict_child.items():
	# print (d,e)

# for d,e in dict_cost.items():
	# print (d,e)
	
# print"************************Breadth First Search*************************"
# bfs()	

# print "************************Depth First Search*************************"
# dfs()
ucs()