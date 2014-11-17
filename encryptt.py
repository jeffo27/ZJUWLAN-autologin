import os, random, getpass

def encrypt(username, password, sampletime):
	""" simple encrypt the username and password, 
		storing them in a local file"""
	
	cwd = os.getcwd()
	filerec = open(cwd+"/.info", "w")	
									# create a loca file to store info.
	filerec.write(username +" "+ str(sampletime) + "\n")
									# store username and sampletime
					
	numlib = '1234567890'
	charlib = 'qwertyuiopasdfghjklzxcvbnm'
	index = sampletime				
	
	for char in password:
		line = []
		for i in range(sampletime):
			line.extend(random.sample(numlib+charlib,10))
		line[index] = char
		index += 1
		filerec.write("".join(line)+"\n")
	
	filerec.close()
	
		
def decrypt():

	cwd = os.getcwd()	
	filerec = open(cwd+"/.info","r")
	lines = filerec.readlines()
	filerec.close()
	
	firstline = lines.pop(0).split()
	username = firstline[0]
	sampletime = int(firstline[1])
	
	password = []
	index = sampletime
	for line in lines:
		password.append(line[index])
		index += 1
	
	password = "".join(password)
	
	return (username, password)

if __name__ == "__main__":
	
	username = raw_input("enter username:")
	password = getpass.getpass("enter password:")
	sampletime = input("enter sampletime:")
	
	encrypt(username, password, sampletime)
	
	rec = open(".info", "r")
	
	for line in rec.readlines():
		print line
	
	rec.seek(0)
	
	print decrypt()

	rec.close()
