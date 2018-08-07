def insertion_sort(data, step=1):
	data_length = len(data)

	if step >= data_length:
		raise ValueError('Incorrect sort step')

	for i in range(data_length):
		j = i + step

		if j >= data_length: break

		if data[i] > data[j]:
			value_i = data[i]
			value_j = data[j]

			del data[i]
			del data[j-1]

			data.insert(i, value_j)
			data.insert(j, value_i)

	return data