class Employee:
	def __init__(self, position, status):
		self._position = position
		self._status = status

	def intro(self):
		return "I am a " + self._position + " and I am " + self._status + "."

emp1 = Employee("Manager", "Full-time")
print(emp1.intro())


class Alpha:

	def __init__(self):
		self._a = 2.  # Protected member ‘a’
		self.__b = 2.  # Private member ‘b’

	def show(self):
		print(self._a)
		print(self.__b)  # Private member ‘b’

	def show2(self):
		print(self._a)
		print(self.__b)  # Private member ‘b’

class Beta(Alpha): # Inherit from Alpha

	def __init__(self): # Constructor of Beta class (inherits from Alpha)
		Alpha.__init__(self) # Call constructor of Alpha class (super class)

	def show(self):
		print(self._a)
		print(self.__b)  # Private member ‘b’

	def show2(self):
		print(self._a)
		print(self.__b)  # Private member ‘b’
# self._a is a protected member and can be accessed by the class and its subclasses.

# Private members in Python are conventionally used with preceding double underscores:
# 	__. self.__b is a private member of the class Alpha and can only be accessed from within the class Alpha.

# It should be noted that these private and protected members can still be accessed from outside of the class by using public methods to access them
# or by a practice known as name mangling. Name mangling is the use of two leading underscores and one trailing underscore, for example:

# _class__identifier

# Class is the name of the class and identifier is the data member that I want to access.


class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        # Functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost



house = House()
print(house.num_rooms)
print(House.num_rooms)
house.num_rooms = 7
# House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

class MyFirstClass:
	def __init__(self):
		print("Who wrote this?")
	index = "Author-Book"
	def hand_list(self, philosopher, book):
		print(philosopher + " wrote the book: " + book)
whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")

