def insertion_sort(data, step=1):
	data_length = len(data)

	if step >= data_length:
		raise ValueError('Incorrect sort step')

	for i in range(data_length):
		j = i + step

		if j >= data_length: break

		if data[i] > data[j]:
			data[i], data[j] = data[j], data[i]

	return data