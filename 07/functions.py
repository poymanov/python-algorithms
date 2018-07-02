from deque import Deque

def check_palindrom(string):
	result_string = ""
	deq = Deque()

	for symbol in string:		
		deq.addTail(symbol)
	
	while deq.size() > 0:
		result_string += deq.removeTail()

	return result_string == string
