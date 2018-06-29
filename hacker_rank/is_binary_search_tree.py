


import sys

class node:
	def __init__( self, data ):
		self.left = None
		self.right = None
		self.data = data


def check_binary_search_tree_( root ):
    int_max = sys.maxint
    int_min = -sys.maxint-1
    return isBST( root, int_max, int_min )

    
    
def isBST( root, max_value, min_value ):
	if root == None:
		return True

	if root.data > max_value-1 or root.data < min_value:
		return False

	return_left = isBST( root.left, root.data, min_value )
	return_right = isBST( root.right, max_value, root.data )
	
	return return_left and return_right



if __name__ == "__main__":
	root = node(5)
	root.left = node(5)
	root.right = node(10)

	print check_binary_search_tree_( root )