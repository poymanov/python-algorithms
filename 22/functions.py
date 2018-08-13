def insertion_sort(data, step=1):
	if step >= len(data):
		raise ValueError('Incorrect sort step')

	for i in range(len(data)):
		j = i + step

		if j >= len(data): break

		if data[i] > data[j]:
			value_j = data[j]

			del data[j]

			for k in range(len(data)):
				if data[k] > value_j:
					value_k = data[k]
					del data[k]
					data.insert(k, value_j)
					data.insert(k + step, value_k)
					break
					
	return data

def shell_sort(data):
	length = len(data)
	steps = [1]

	i = 1

	while i < length // 3:
		i = 3 * i + 1
		steps.insert(0, i)

	for step in steps:
		data = insertion_sort(data, step)	

	return data