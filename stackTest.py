import unittest
from MyStack import Stack

class stackTest(unittest.TestCase):

	def setUp(self):
		self.stack = Stack()

	def test_newlyCreatedStackShouldBeEmpty(self):
		self.assertTrue(self.stack.isEmpty())
		self.assertEquals(0, self.stack.getSize())

	def test_AfterOnePushStackSizeShouldBeOne(self):
		self.stack.push(1)
		self.assertEquals(1, self.stack.getSize())

	def test_AfterOnePushAndOnePopStackShouldBeEmpty(self):
		self.stack.push(1)
		self.stack.pop()
		self.assertTrue(self.stack.isEmpty())

	def test_AfterOnePopStackSizeShouldDecrement(self):
		size = self.stack.getSize()
		self.stack.pop()
		self.assertEquals( self.stack.getSize(), size-1)

	def test_whenPushedPastLimitStackOverflows(self):
		self.stack = self.stack.Make(2)
		self.stack.push(1)
		self.stack.push(2)
		self.assertRaises( Stack.OverflowException, self.stack.push, 3)
		
if __name__== '__main__' :
	unittest.main()