class Stack1:
	def __init__(self):
		self.stack = []

	def pop(self):
		if len(self.stack) == 0:
			return None
		return self.stack.pop()

	def push(self, value):
		return self.stack.append(value)

	def peak(self):
		if len(self.stack) == 0:
			return None
		return self.stack[-1]

	def size(self):
		return len(self.stack)

class Stack2: #1
	def __init__(self):
		self.stack = []

	def pop(self):
		if len(self.stack) == 0:
			return None
		return self.stack.pop(0)

	def push(self, value):
		return self.stack.insert(0, value)

	def peak(self):
		if len(self.stack) == 0:
			return None
		return self.stack[-1]

	def size(self):
		return len(self.stack)


