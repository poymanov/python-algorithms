import random

def quicksort(data, left=None, right=None):
	if left is None and right is None:
		left = 0
		right = len(data) - 1

	if left >= right: return data
 
	i, j = left, right
	pivot = data[random.randint(left, right)]

	while i <= j:
	   while data[i] < pivot: i += 1
	   while data[j] > pivot: j -= 1

	   if i <= j:
	       data[i], data[j] = data[j], data[i]
	       i, j = i + 1, j - 1

	quicksort(data, left, j)
	quicksort(data, i, right)

	return data