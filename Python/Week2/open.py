#first way:
file = open('file.txt', mode='r')
data = file.readline()
print(data)
file.close

#Second way:
with open('file.txt', mode='r') as file:
    data = file.readline()
print(data)

#writing to a file

#first way:
with open('newFile.txt', 'w') as file:
    file.write("This is a new file created!")
    
#Second way:
with open('newFile.txt', 'w') as file:
	file.writelines(["This is a new file created!", "\nThis is another line to be added"])

#Same way different mode:
with open('newFile.txt', 'a') as file:
	file.writelines(["\nThis is a new file created!", "\nThis is another line to be added"])
        
#Using Try except with previous examples:
try:
	with open('sample/newFile.txt', 'a') as file:
		file.writelines(["\nThis is a new file created!", "\nThis is another line to be added"])
except FileNotFoundError as e:
	print("Error", e)
