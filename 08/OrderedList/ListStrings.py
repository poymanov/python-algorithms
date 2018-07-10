from OrderedList.List import List

class ListStrings(List):
	def compare_nodes(self, n1, n2):
		n1_value = n1.value.strip()
		n2_value = n2.value.strip()

		if n1_value == n2_value: return False

		if self.sort == self.SORT_ASC:
			if n1_value > n2_value:
				if n2.next is None: 
					return self.APPEND_AFTER
				elif n1_value <= n2.next.value.strip(): 
					return self.APPEND_AFTER
				return False
		else:
			if n1_value < n2_value:
				if n2.next is None:
					return self.APPEND_AFTER
				elif n1_value >= n2.next.value.strip():
					return self.APPEND_AFTER
				return False
			else:
				if n2.prev is None:
					return self.APPEND_BEFORE
				elif n2_value >= n2.prev.value.strip():
					return self.APPEND_BEFORE
				return False
