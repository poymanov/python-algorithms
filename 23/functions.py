def partitioning(data, pivot_element):
	data_length = len(data)

	i1 = 0
	i2 = data_length - 1

	while True:		
		if i1 == i2 - 1:
			break		

		if data[i1] < pivot_element or data[i1] == pivot_element:
			i1 += 1
			continue

		if data[i2] > pivot_element or data[i2] == pivot_element:
			i2 -= 1			
			continue

		data[i1], data[i2] = data[i2], data[i1]		

	return {'i1': i1, 'i2': i2}	
