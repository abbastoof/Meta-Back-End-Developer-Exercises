#Reading Files

#first way:
with open('newFile.txt', 'r') as file:
	print(file.read())
#Second way:
with open('newFile.txt', 'r') as file:
	print(file.read(27))
#Third way:
with open('newFile.txt', 'r') as file:
	print(file.readline())
#fourth way:
with open('newFile.txt', 'r') as file:
	print(file.readlines())
#fifth way:
with open('newFile.txt', 'r') as file:
	data = file.readlines()
	for i in data:
		print(i)
#Sixth way:
with open('newFile.txt', 'r') as file:
	for i in file:
		print(i)
