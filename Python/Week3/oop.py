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
