# CSE 101 - IP HW2
# K-Map Minimization 
# Name:Sanchit Trivedi
# Roll Number:2018091
# Section:A
# Group:3
# Date:19/10/2018

import copy
import re

def minFunc(numVar, func):
	"""
        This python function takes function of maximum of 4 variables
        as input and gives the corresponding minimized function(s)
        as the output (minimized using the K-Map methodology),
        considering the case of Don’t Care conditions.

	Input is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm)
	Output is a string representing the simplified Boolean Expression in
	SOP form.

        No need for checking of invalid inputs.
        
	Do not include any #print statements in the function."""
	
	PI=[]
	gcount=0

	# def print_matrix(matrix,cols,rows):
	# 	for i in range(rows):
	# 		for j in range(cols):
	# 			#print (matrix[i][j],end=' ')
	# 		#print ()

	# def takeinput():
	# 	bits=int(input('Enter no. of variables : '))
	# 	myfunc=input('Enter function to be minimized : ')
	# 	minFunc(bits,myfunc)

	def deci_to_nbitbin(n,bits):
		'''Converts the no. passed as an argument to binary format of 'bits' bits'''
		bin=''
		if n<=int('1'*bits,2):
			while n>0 :
				bin+=str(n%2)
				n//=2
			if len(bin)==bits:
				return (bin[::-1])
			else:
				return '0'*(bits-len(bin))+bin[::-1]
		else:
			return 'INVALID INPUT'

	def grouper(list1,numVar):
		''' Groups the entries of the list passed as an argument according to the no. of 1's '''
		list1=list(set(list1))
		l=[]
		for i in range(numVar+1):
			nl=[]
			for j in list1:
				if j.count('1')==i:
					nl.append(j)
			if len(nl)!=0:
				l.append(nl)
		return l

	def singlebitchange(m,n,gcount):
		''' This function checks whether there is a change of only 1 bit between two terms passed as an argument '''
		m1=[]
		n1=[]
		combine=''
		for j in re.finditer('-',m):#generates a list of indices where '-' was found in the binary representation
			m1.append(j.start())	
		for k in re.finditer('-',n):
			n1.append(k.start())
		if n1==m1:
			for i in range(len(m)):
				if m[i]==n[i]:
					combine+=n[i]
				elif m[i]!=n[i]:
					combine+='-'
			if combine.count('-')==gcount:
				return combine 
		else:
			return 0

	def emptycheck(chart,cols,rows):
		''' This function checks whether the chart formed during chart reduction is empty or not '''
		for i in range(1,rows):
				for j in range (1,cols):
					if chart[i][j]!='_':
						return False
		else:
				return True

	def bin2literalconverter(a,numVar):
		''' This function converts the term passed as an argument to the literal representation  '''
		if a!='-'*numVar:
			s=''
			for i in range(len(a)):
				if a[i]!='-':
					s+=chr(87+i)
					if a[i]=='0':
						s+="'"
			return s
		else:
			return '1'
	
	func=func.split('d')
	l=func[0].strip().lstrip("'(").rstrip(")'").split(',')
	dontc=func[1].strip().lstrip("'(").rstrip(")'").split(',')
	copyl=copy.deepcopy(l)
	if dontc[0]!='-':
		l.extend(dontc)
	binlist=[]#stores the input after conversion of the input to their binary equivalents
	
	for i in l:
		x=deci_to_nbitbin(int(i),numVar)
		if x!='INVALID INPUT':
			binlist.append(x)
		else:
			print(x)
	#print (binlist)
	cbinlist=copy.deepcopy(binlist)

	def finder(bingroups,PI,gcount):
		''' This function finds the prime implicants '''
		dashed1=[]
		tracker=[[0]*len(i) for i in bingroups]#Used for tracking which element is a prime implicant out of bingroups
		for i in range(len(bingroups)-1):
			for j in range(len(bingroups[i])):
				for k in range(len(bingroups[i+1])):
					ans = singlebitchange(bingroups[i][j],bingroups[i+1][k],gcount) 
					if ans:
						dashed1.append(ans)
						tracker[i][j]=1
						tracker[i+1][k]=1
				
		#print (tracker)
		for i in range(len(tracker)):
			for j in range (len(tracker[i])):
				if tracker[i][j]==0:
					PI.append(bingroups[i][j])
		return dashed1

	while binlist!=[]:
		bin0=grouper(binlist,numVar)
		#print (bin0)
		gcount+=1
		binlist=finder(bin0,PI,gcount)

	#print (PI)
	tracer=[[] for i in range(len(PI))]
	for i in range(len(PI)):
		s=PI[i].replace('-','.')
		for k in range(len(cbinlist)):
			j=cbinlist[k]
			if re.match(s,j)!=None:
				tracer[i].append(int(j,2))
	#print (tracer)
	
	cols=len(copyl)+1
	rows=len(PI)+1
	chart=[[0 for i in range(cols)] for j in range(rows)]#initializez the chart for chart reduction in petrick's algorithm
	chart[0][0]=''
	for i in range(len(tracer)):
		chart[i+1][0]=tracer[i]	
	for j in range (len(copyl)):
		chart[0][j+1]=copyl[j]
	
	for i in tracer:#places a "X" in the required places in the chart
		for j in i:
			if str(j) in chart[0]:
				chart[tracer.index(i)+1][chart[0].index(str(j))]='X'

	EPItracker=[]#Tracks which element is an EPI
	coltracker=[]
	for j in range(1,cols):
		count=0
		for i in range (1,rows):
			if chart[i][j]=='X':
				count+=1
				tmp=i
		if count==1:
			EPItracker.append(tmp-1)
			coltracker.append(j)

	#print_matrix(chart,cols,rows)
	#print(EPItracker)
	for i in EPItracker:#crosses out the row of the columns containing a single "x" in the chart
		for j in range(1,cols):
			if chart[i+1][j]!='X':
				chart[i+1][j]='_'
			else:
				coltracker.append(j)
				chart[i+1][j]='_'
	#print_matrix(chart,cols,rows)
	for j in coltracker:#crosses out the columns of the encountered 'X's while moving along the rows of the single "X" in a column
		for i in range(1,rows):
			chart[i][j]='_'
	#print_matrix(chart,cols,rows)


	while not emptycheck(chart,cols,rows):# This loop reduces the chart and finds the EPI's from the PI's
		max=0;maxrow=0
		for i in range(1,rows):
			k=chart[i]
			if k.count('X')>=max and (len(k[0])>=len(chart[maxrow][0])):
				max=k.count('X')
				maxrow=i
			
		EPItracker.append(maxrow-1)
		for i in EPItracker:
			for j in range(1,cols):
				if chart[i+1][j]!='X':
					chart[i+1][j]='_'
				else:
					coltracker.append(j)
					chart[i+1][j]='_'
		for j in coltracker:
			for i in range(1,rows):
				chart[i][j]='_'
		#print_matrix(chart,cols,rows)
	#print (EPItracker)

	EPI=[]
	for i in list(set(EPItracker)):
		EPI.append(PI[i])
	#print (EPI)
	finalans=[]
	for j in EPI:#converts to literal format
		finalans.append(bin2literalconverter(j,numVar))
	finalans.sort()
	finalanswer=' + '.join(finalans)
	#print (finalanswer)
	return finalanswer
#print (minFunc(4,"(0,1,2,3,13) d(5,7,9)"))
#takeinput()