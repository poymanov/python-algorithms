class List():
	SORT_ASC = 'ASC'
	SORT_DESC = 'DESC'
	APPEND_AFTER = 'append_after'
	APPEND_BEFORE = 'append_before'

	def __init__(self, sort = SORT_ASC):
		self.head = None
		self.tail = None
		self.sort = sort

	def add(self, item):
		if self.head == None:
			self.head = item
			self.tail = item
			return

		element = self.head
	
		while element != None:		
			compare_result = self.compare_nodes(item, element);

			if compare_result == self.APPEND_AFTER:
				self.append_after_node(item, element)
				break
			elif compare_result == self.APPEND_BEFORE:
				self.append_before_node(item, element)
				break

			element = element.next	

	def compare_nodes(self, n1, n2):		
		if n1.value == n2.value: return False

		if self.sort == self.SORT_ASC:
			if n1.value > n2.value:
				if n2.next is None: 
					return self.APPEND_AFTER
				elif n1.value <= n2.next.value: 
					return self.APPEND_AFTER
				return False
		else:
			if n1.value < n2.value:
				if n2.next is None:
					return self.APPEND_AFTER
				elif n1.value >= n2.next.value:
					return self.APPEND_AFTER
				return False
			else:
				if n2.prev is None:
					return self.APPEND_BEFORE
				elif n2.value >= n2.prev.value:
					return self.APPEND_BEFORE
				return False

	def append_after_node(self, node, after):
		node.prev = after
		node.next = after.next

		if after.next is not None:
			after.next.prev = node

		if self.tail is None or self.tail == after:
			self.tail = node	

		after.next = node

	def append_before_node(self, node, before):
		node.prev = before.prev
		node.next = before

		if before.prev is not None:
			before.prev.next = node

		if self.head == before:
			self.head = node

		before.prev = node	

	def find(self, val):
		if self.sort == self.SORT_ASC:
			if self.head.value > val or self.tail.value < val: return None
		elif self.sort == self.SORT_DESC:
			if self.head.value < val or self.tail.value > val: return None

		node = self.head

		while node is not None:
			if node.value == val:
				return node
			node = node.next
		return None	