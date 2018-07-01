from stack import Stack1, Stack2

def rotate_queue(qu, n):
	for _ in range(n):
		value = qu.dequeue()

		qu.enqueue(value)

def queue_with_stacks():
	stack1 = Stack1()
	stack2 = Stack2()

	stack1.push(1)
	stack1.push(2)
	stack1.push(3)

	while stack1.size() > 0:
		value = stack1.pop()
		stack2.push(value)
		
	while stack2.size() > 0:
		value = stack2.pop()