class Stack:

	def __init__(self, capacity = None):
		self.size     = 0
		self.capacity = capacity

	def isEmpty(self):
		return self.size == 0	

	def getSize(self):
		return self.size

	def push(self, element):
		if( (self.capacity != None) and ((self.size +1 ) > self.capacity )):
			raise self.OverflowException("jiji")
		self.size+=1

	def pop(self):
		self.size -=1

	def Make(self, capacity):
		return Stack(capacity)

	class OverflowException(Exception):

		def __init__(self, value = "Stack Overflow"):
			self.value = value
		def __str__(self):
			return self.value

	class UnderflowException(Exception):

		def __init__(self, value = "Stack Underflow"):
			self.value = value
		def __str__(self):
			return self.value