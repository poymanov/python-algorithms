from LinkedList import Node, List

n1 = Node(12)
n2 = Node(55)
n1.next = n2

linked_list = List()
linked_list.add_in_tail(n1)
linked_list.add_in_tail(n2)
linked_list.add_in_tail(Node(128))
linked_list.print_all_nodes()

nf = linked_list.find(55)
if nf is not None:
	print(nf.value)
