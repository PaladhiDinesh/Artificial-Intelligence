import math
import random
f=open("output.txt","w")
for i in range(0,100):

	x=random.uniform(-5,5)
	y=random.uniform(-5,5)

	# print x,y
	fun= (-20)*math.exp(-0.2*math.sqrt(0.5*((x*x)+(y*y)))) - math.exp(0.5*(math.cos(math.radians(2*180*x))+math.cos(math.radians(2*180*y))))

	for i in range(0,99):
		xnew=(random.uniform(0,1)-0.5)*0.1+x
		ynew=(random.uniform(0,1)-0.5)*0.1+y
		# print ("New x and y are %s,%s"%(xnew,ynew))
		while True:
			if(xnew < 5.0 and ynew < 5.0):
				break
			else:
				# print "hi"
				xnew=(random.uniform(0,1)-0.5)*0.1+x
				ynew=(random.uniform(0,1)-0.5)*0.1+y
		newfun= (-20)*math.exp(-0.2*math.sqrt(0.5*((xnew*xnew)+(ynew*ynew)))) - math.exp(0.5*(math.cos(math.radians(2*180*xnew))+math.cos(math.radians(2*180*ynew))))
		# print ("old value is %s,new value is %s"%(fun,newfun))
		if (newfun > fun):
			# print "final output"
			# print x,y
			print fun
			f.write("\n"+str(fun))
			# f.write
			# print i
			break
		x=xnew
		y=ynew
		fun=newfun            
		# print("loops:%s"%i)
		# print fun

f.close()

# y=-5
#
