from stack import Stack1, Stack2

def is_balanced(string): #2
	stack = Stack1()

	for i in string:
		if i == '(':
			stack.push(i)
		elif i == ')':
			if stack.pop() == None: return False

	return stack.size() == 0

def calc_postfix_variable(string):
	stack1 = Stack2()
	stack2 = Stack2()

	for i in string:
		if i == ' ': continue
		stack1.push(i)

	while stack1.size() > 0:
		element = stack1.pop()

		if element == '+' or element == '*':
			element1 = int(stack2.pop())
			element2 = int(stack2.pop())

			if element == '+':
				result = element1 + element2
			elif element == '*':
				result = element1 * element2

			stack2.push(result)
		elif element == '=':
			return stack2.pop()
		else:
			stack2.push(element)



	
