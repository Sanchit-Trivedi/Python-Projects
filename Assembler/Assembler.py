import csv,sys,os
import shutil

filename = sys.argv[1]

#first pass

Opcodes = {
"CLA" : "0000",
"LAC" : "0001",
"SAC" : "0010",
"ADD" : "0011",
"SUB" : "0100",
"BRZ" : "0101",
"BRN" : "0110",
"BRP" : "0111",
"INP" : "1000",
"DSP" : "1001",
"MUL" : "1010",
"DIV" : "1011",
"STP" : "1100"
}

sym_table = []
symbols = []
labels = []
error_flag = 1
opcodetable = []

with open(filename) as file: # Opening the Assembly file
	reader = csv.reader(file,delimiter="\n")
	data = list(reader)
	n = len(data)
	var_add = 0
	lab_add = 0
	# n is the total no of instructions
	l=[]
	# Tokenizing Data
	for i in data:
		for j in i:
			l.append(j.strip().split())
	
	if (l[n-1][0]!="END"):
		print("END Statement Missing!!")
		error_flag = 0
	count = 0
	for i in l:
		
		count+=1
		new_i = []
		#Handling Comments in the Assembly Code
		for element in i :
			if "#" in element:
				break
			else:
				new_i.append(element)
		l[l.index(i)] = new_i
		i = new_i
		
		if i!=[]:
			# Setting the location counter to the given value
			if(i[0]=="START"):
				
				# Checking for error
				if(len(i)<2):
					print("Less Number of operands than expected!!")
					error_flag = 0
					continue

				if(len(i)>2):
					print("More Number of operands than expected!!")
					error_flag = 0
					continue

				var_add = int(i[1])+n
				lab_add = int(i[1])
			
			if(i[0]=="INP" or i[0]=="SAC"):
				# Checking for error
				if(len(i)<2):
					print("Less Number of operands than expected!!")
					error_flag = 0
					continue

				if(len(i)>2):
					print("More Number of operands than expected!!")
					error_flag = 0
					continue

				try:
					
					# handling direct addresses

					y = int(i[1])

				except ValueError:

					# assigning new address to a new variable
					# binary conversion of address of variables

					address = bin(var_add)[2:]
					num_zero = 8-len(address)
					address = "0"*num_zero + address
					var_add = var_add+1

					# adding in symbol table
					if(i[1] not in symbols):
						l1 = [l.index(i)+1,"Variable",i[1],address]
						symbols.append(i[1])
						sym_table.append(l1)
				finally:
					opcodetable.append([count,i[0],Opcodes[i[0]]])


			elif(i[0]=="LAC" or i[0]=="ADD" or i[0]=="SUB" or i[0]=="DSP" or i[0]=="MUL" or i[0]=="DIV"):
				
				# Checking for error
				if(len(i)<2):
					print("Less Number of operands than expected!!")
					error_flag = 0
					continue

				if(len(i)>2):
					print("More Number of operands than expected!!")
					error_flag = 0
					continue
				
				try:

					# handling direct addresses
					
					y = int(i[1])

				except ValueError:
					# Error statement shown if variable is not defined
					if i[1] not in symbols:
						print("Error, variable not defined!!")
						error_flag = 0
					if i[1] in labels:
						print("Variable and label cannot have the same name!!")
						error_flag = 0
				finally:
					opcodetable.append([count,i[0],Opcodes[i[0]]])
			
			# handling labels

			elif(':' in i[0]):
				# checking for error due to operands supplied with CLA and STP statements
				if(i[1]=="CLA" or i[1]=="STP" and len(i)>2):
					print("Error, No operand expected at line",l.index(i)+1,"!!")
					error_flag = 0
					continue
				if(i[1]=="CLA" or i[1]=="STP" and len(i)<2):
					print("No instruction given!!")
					error_flag = 0
					continue
				opcodetable.append([count,i[1],Opcodes[i[1]]])
				# binary conversion of address of labels
				address = bin(lab_add+l.index(i))[2:]
				num_zero = 8-len(address)
				address = "0"*num_zero + address
				
				# create new label in symbol table
				if i[0][:-1] not in labels:	
					sym_table.append([l.index(i)+1,"Label   ",i[0][:-1],address])
					labels.append(i[0][:-1])
				
				# alloting the addresses of the labels

				elif i[0][:-1] in symbols:
					print("Variable and label cannot have the same name!!")
					error_flag = 0

				else:
					for j in sym_table:
						if(j[1]=="Label   " and j[2]==i[0][:-1]):
							j[0] = l.index(i)
							j[3] = address

			#handling branching statements

			elif(i[0]=="BRZ" or i[0]=="BRN" or i[0]=="BRP"):
				
				# Checking for error
				if(len(i)<2):
					print("Less Number of operands than expected!!")
					error_flag = 0
					continue

				if(len(i)>2):
					print("More Number of operands than expected!!")
					error_flag = 0
					continue

				try:

					# direct addresses
					y = int(i[1])

				except ValueError:

					# forward referencing for labels
					if i[1] not in labels :
						sym_table.append([l.index(i)+1,"Label   ",i[1],""])
						labels.append(i[1])
				finally:
					opcodetable.append([count,i[0],Opcodes[i[0]]])

			# handling CLA and STP statements
			elif(i[0]=="CLA" or i[0]=="STP"):
				if(len(i)>1):
					print("Error, No operand expected at line",l.index(i)+1,"!!")
					error_flag = 0
				opcodetable.append([count,i[0],Opcodes[i[0]]])

			# opcode not found error
			elif(i[0]!="START" and i[0]!="END"):
				print("OPCODE not found!!")
				error_flag = 0
	# checking for error in symbol table

	# print(opcodetable)


	for ptr in sym_table:
		if(ptr[3]==""):
			print("Error",ptr[1].strip(),"not defined at line",ptr[0],"!!")
			error_flag = 0
	
	# removes the existing directory
	dirName = filename[:-4] + "_Assembled"
	if os.path.exists(dirName) and os.path.isdir(filename[:-4] + "_Assembled"):
		shutil.rmtree(dirName)
	os.mkdir(dirName)
	path = dirName + "/"

	# Pass two

	if(error_flag):	
		OP_TABLE = open (path + "OPCodeTable.txt","w")
		OP_TABLE.write("Offset\t\tOPCODE\t\tBINARY\n")
		for i in opcodetable:
			l10 = list(map(str,i))
			OP_TABLE.write(("\t\t".join(l10) + "\n"));
		OP_TABLE.close()
		# writing the symbol table into a file
		SYM_TABLE = open(path + "SymbolTable.txt", "w")
		SYM_TABLE.write("Offset\t\tType \t\t\tSymbol \t\tAddress\n")
		
		for i in sym_table:
			l1 = list(map(str,i))
			SYM_TABLE.write(("\t\t".join(l1) + "\n"))
		SYM_TABLE.close()	
		
		Mc = open(path + "MachineCode.txt","w")
		
		for i in l :
			new_i = []

			for element in i :
				if "#" in element:
					break
				else:
					new_i.append(element)
			
			l[l.index(i)] = new_i
			i = new_i

			if(i!=[]):
				if(i[0]=="START" or i[0]=="END" or i[0]=="Text" or i[0]=="Data"):
					continue

				# if line contains a label

				if(":" in i[0]):
					string = Opcodes[i[1]]
					if len(i)==2:
						string += ("0"*8)
					elif len(i)==3:
						try:
							y = int(i[2])
							address = bin(y)[2:]
							zeros = 8-len(address)
							address = "0"*zeros + address
							string += address
						except ValueError:
							for ptr in sym_table:
								if(i[2]==ptr[2]):
									string += ptr[3]
				
				# if label is not present in line

				else:
					string = Opcodes[i[0]]
					# for CLA & STP opcodes
					if len(i)==1:
						string+=("0"*8)

					# for all other opcodes
					elif len(i)==2:
						try:
							y = int(i[1])
							address = bin(y)[2:]
							zeros = 8-len(address)
							address = "0"*zeros + address
							string += address
						except ValueError:
							for ptr in sym_table:
								if(i[1]==ptr[2]):
										string+=ptr[3]
				Mc.write(string + "\n")
		Mc.close()