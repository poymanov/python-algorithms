from quicksort import quicksort
from shell_sort import shell_sort
import random
import time

def create_sort_data():
	elements_length = 30000
	data = []
	for _ in range(elements_length):
		data.append(random.randint(0, elements_length))		

	return data

sort_data = create_sort_data()

start_time = time.time()
quicksort(sort_data)

quicksort_time = time.time() - start_time

start_time = time.time()
shell_sort(sort_data)

shell_sort_time = time.time() - start_time


print('quicksort time', quicksort_time)
print('shell sort time', shell_sort_time)

