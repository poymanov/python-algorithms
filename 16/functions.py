def create_array_from_tree(tree):
	tree_size = tree.get_array_size()

	result_list = [None] * tree_size

	for node in tree.iterate_node():
		if tree.root == node:
			result_list[0] = node.key
		else:			
			parent = node.parent

			parent_index = result_list.index(parent.key)	

			if parent.left_child == node:
				node_index = 2 * parent_index + 1
			elif parent.right_child == node:
				node_index = 2 * parent_index + 2

			result_list[node_index] = node.key	

	return result_list

def search(tree, array, value):	
	search_result = tree.search(value)

	if search_result[1] == False:
		parent = search_result[0]

		parent_index = array.index(parent.key)

		left_child_index = 2 * parent_index + 1
		right_child_index = 2 * parent_index + 2

		try:
			if array[left_child_index] == None or array[right_child_index] == None:
				return -12
		except:
			return None
	else:
		return array.index(search_result[0].key)
