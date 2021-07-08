import matplotlib.pyplot as plt
import math,sys
x1=[]
y1=[]
c=0
all_outputs=[]
plt.figure()
plt.grid()
def plotter(x,y):
	'''Plot the x and the y arrays passed as an argument'''	
	if c==1:
		plt.title('Original Figure')
	else:
		plt.title('After '+str(c-1)+' transformation')
	plt.plot(x,y)
	plt.pause(0.0000000000000000000001)	
	plt.show(block=False)

def main1():
	'''This is the main function wherevthe real exexcution of the program takes place'''
	plt.ion()
	global x1,y1,c,all_outputs
	a=input().split()
	if a[0].lower()=='polygon':
		x=list(map(float,input().split()))
		y=list(map(float,input().split()))
		x.append(x[0]);y.append(y[0])
		print(x)
		print(y)
		c+=1
		plotter(x,y)
	elif a[0].lower()=='disc':
		dim = input().split()
		xi=float(dim[0])
		yi=float(dim[1])
		r1=float(dim[2])
		r2=float(dim[2])
		i=0;x=[];y=[]
		while i<=6.28:
			x.append(xi+r1*math.cos(i))
			y.append(yi+r2*math.sin(i))
			i+=0.01
		c+=1
		plotter(x,y)
	while 1:
		act=input().split()
		if act[0].lower()=='s':
			for i in range(len(x)):
				scaling(float(act[1]),float(act[2]),x[i],y[i])
			x=list(x1) 
			y=list(y1)
			c+=1
			plotter(x,y)
			if a[0].lower()=='disc':
				scaling(float(act[1]),float(act[2]),r1,r2)
				r1=x1[len(x1)-1]
				r2=y1[len(y1)-1]
				all_outputs.append([xi,yi,r1,r2])
			else:
				all_outputs.append(x)
				all_outputs.append(y)
			x1=[]
			y1=[]
		elif act[0].lower()=='r':
			for i in range(len(x)):
				rotation(float(act[1]),x[i],y[i])
			x=list(x1) 
			y=list(y1)
			c+=1
			plotter(x,y)
			if a[0].lower()=='disc':
				rotation(float(act[1]),xi,yi)
				xi=x1[len(x1)-1];yi=y1[len(y1)-1]
				all_outputs.append([xi,yi,r1,r2])
			else:
				all_outputs.append(x)
				all_outputs.append(y)
			x1=[]
			y1=[]
		elif act[0].lower()=='t':
			for i in range(len(x)):
				translation(float(act[1]),float(act[2]),x[i],y[i])
			x=list(x1) 
			y=list(y1)
			c+=1
			plotter(x,y)
			if a[0].lower()=='disc':
				translation(float(act[1]),float(act[2]),xi,yi)
				xi=x1[len(x1)-1];yi=y1[len(y1)-1]
				all_outputs.append([xi,yi,r1,r2])
			else:
				all_outputs.append(x)
				all_outputs.append(y)
			x1=[]
			y1=[]
		elif act[0].lower()=='quit':
			plt.close('all')
			if a[0].lower()=='polygon':
				for i in range(0,len(all_outputs),2):
					print()
					print (all_outputs[i][0:len(all_outputs[i])-1])
					print (all_outputs[i+1][0:len(all_outputs[i+1])-1])
			else:
				for i in all_outputs:
					print()
					print(i)
			break
	
def matrix_multiplication(matrix1,matrix2,r1=3,c1=3,r2=3,c2=1):
	'''Multiplies 2 matrices matrix1 and matrix2 '''
	if c1==r2:
		product=[[0 for i in range(c2)] for j in range(r1)]
		for i in range(r1):
			for j in range(c2):
				for k in range(c1):
					product[i][j]+=matrix1[i][k]*matrix2[k][j]
		return product
	else:
		print ("Given matrices cannot be multiplied")

def scaling(sx,sy,x,y):
	''' Scales the x, y coordinates according to the passed values'''
	global x1,y1
	transformation = [[0 for j in range(3)] for i in range(3)]
	transformation[0][0]=sx
	transformation[1][1]=sy
	transformation[2][2]=1
	multiplier=[[x],[y],[1]]
	scaled=matrix_multiplication(transformation,multiplier)
	x1.append(scaled[0][0])
	y1.append(scaled[1][0])

def rotation(th,x,y):
	'''Rotates the x and y coordinates according to the given angle'''
	global x1,y1
	transformation=[[0 for j in range(3)] for i in range(3)]
	th=math.radians(th)
	cosine=math.cos(th)
	sine=math.sin(th)
	transformation[0][0]=cosine
	transformation[0][1]=-sine
	transformation[1][1]=cosine
	transformation[1][0]=sine
	multiplier=[[x],[y],[1]]
	rotated=matrix_multiplication(transformation,multiplier)
	x1.append(rotated[0][0])
	y1.append(rotated[1][0])

def translation(dx,dy,x,y):
	''' Translates the given coordinates according to the passed parameters dx and dy '''
	global x1,y1
	transformation = [[0 for j in range(3)] for i in range(3)]
	transformation[0][2]=dx
	transformation[1][2]=dy
	transformation[0][0]=1
	transformation[1][1]=1
	transformation[2][2]=1
	multiplier=[[x],[y],[1]]
	moved=matrix_multiplication(transformation,multiplier)
	x1.append(moved[0][0])
	y1.append(moved[1][0])
main1()
sys.exit()