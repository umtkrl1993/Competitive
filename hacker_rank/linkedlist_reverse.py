#!/usr/bin/python


class ListNode:
	def __init__(self, data ):
		self.data = data
		self.next = None


class LinkedList:
	def __init__( self ):
		self.head = None
		self.tail = None


	def insertNode( self, node_data ):
		node = ListNode( node_data )

		if head == None:
			head = node
		else:
			tail.next = node

		tail = node





def reversePrint( head ):
	print_stack = []
	current = head 
	while current != None:
		print_stack.append( current.data )
		current = current.next

	stack_len = len( print_stack )

	while stack_len > 0:
		data = print_stack.pop()
		print data
		stack_len -= 1


def reverse( head ):
	next_next = None
	if head != None:
		
		while head != None:
			new_head = head.next
			head.next = next_next
			next_next = head
			head = new_head
	return next_next

