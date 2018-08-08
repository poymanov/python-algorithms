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
				if data[k] < value_j:
					data.insert(k + step, value_j)


	return data