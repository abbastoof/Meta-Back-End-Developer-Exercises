import random
f_name = input("Type the file name: ")
with open(f_name, 'r') as f:
    data = f.read()
    data_list = data.split("\n")
    print(random.choice(data_list))