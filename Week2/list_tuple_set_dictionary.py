list1 = [1, 2, 3, 4, 5]
# print(list1[0])
# list2 = ['A', 'B', 'C']
# list3 = ['Hello', 1, True, 4.22]

# list4 = [1, [1, 2, 3], 4, 5, 6]

print(list1, sep=" ")
print(*list1)
list1.insert(len(list1), 6)
print(*list1)
print(list1, sep=" ")
list1.append("hello")
print(*list1)
print(list1, sep=" ")
list1.extend([7, 8, 9])
print(*list1)
print(list1, sep=" ")
list1.pop(6)
print(list1, sep=" ")
del list1[8]
print(list1, sep=" ")
for x, y in enumerate(list1):
	del list1[x]

print(list1, sep=" ")
list1.clear()
print(list1, sep=" ")
my_tuple = (2, 2, 3)
print(my_tuple)
print(my_tuple.count(2))
# The issue lies in the loop where you are using enumerate(list1)
# and then trying to delete elements from list1 inside the loop.
# The problem is that when you delete an element from the list,
# the indices of the remaining elements shift, and you end up skipping some elements.
# A safer way to delete all elements from the list in this case would be
# to use list1.clear() or simply reassign an empty list to list1 after the loop.
# Instead, you can do:
# list1.clear()  # or
# list1 = []

print(my_tuple.index(3))
set_a = {1, 2, 3, 4, 5}
set_a.add(6)
set_a.remove(6)
set_a.discard(5)
set_b = {4, 5, 6, 7, 8, 9}
print(set_a.union(set_b))
print(set_a)
set_a = set_a.union(set_b)
print(set_a)
set_a.update(set_b)
print(set_a)
set_b.add(10)
print(set_b)
set_a = set_a | set_b # same as union
print(set_a)
print(set_a.intersection(set_b))
# set_a = set_a - set_a.intersection(set_b)
# set_a = set_a - (set_a & set_b) # same as intersection
# set_a = set_a.difference(set_b)
set_a = set_a - set_b # same as difference
set_a = set_a.union(set_b)
print(set_a)
print(set_b)
set_a.add(4)
print(set_a)
set_a = set_a - set_b # same as difference
print(set_a)
set_a.add(4)
set_a.add(5)
set_a.add(6)
print(set_a)
set_a = set_a.symmetric_difference(set_b) # all elements that are in set a and set b but not in both sets
set_a = set_a ^ set_b # same as symmetric_difference
print(set_a)

sample_dictionary = {1: 'coffee', 2: 'Tea', 3: 'Juice'}
print(sample_dictionary[2])
