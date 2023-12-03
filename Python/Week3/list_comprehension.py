# The syntax for list comprehension is:

# [ <expression> for x in <sequence> if <condition>]

data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

#alternative in the case of example 1:
# List comprehension:
# data = [x+3 for x in data]

# # Regular for loop:
# for x in range(len(data)):
#     data[x] = data[x] + 3

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)


#Dictionary comprehension

# The syntax for dictionary comprehension is:

# dict = { key:value for key, value in <sequence> if <condition> }

# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)

# Note how in case of using two lists, the format it follows is:

#     new_dict ={key:value for (key, value) in zip(list1, list2)}

# Here I used the zip function that combines the two lists. When the two lists are of unequal length, the length of the shorter list is the length of the dictionary.

# Set comprehension

# The set comprehension deals with the set data type and it's very similar to list comprehension.
# The only key difference is the use of curly brackets for sets instead of square brackets as in lists. For example:

set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)

# The syntax for set comprehension is:

# { <expression> for x in <sequence> if <condition> }
# You can see the code format is similar to what I used in list comprehensions.
# For the sake of showing versatility, I used the "not in" keywords to check the values in the list.
# The output is the values in ranges 10 and 20 that are not present in that list.


# Generator comprehension

# Generator comprehensions are also very similar to lists with the variation of using curved brackets instead of square brackets.
# They are also more memory efficient as compared to list comprehensions. For example:


data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")

# In the code above, I created a generator object of the class generator instead of a list.
# The elements in this iterator object cannot be directly accessed and need the help of a for loop and as such,
# I iterate over these elements and print them.


def square(num):
    return num * 2


# Here is the difference between map() function and list comprehensions:

newdata = map(square, data)

# newdata = [x + 3 for x in data]

print(newdata)


numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers)) # why map return a true or false value for each element in the list, but filter return the element itself? because map is used to apply a function to each element in the list, but filter is used to filter out the elements that don't meet the condition.
print(small)
