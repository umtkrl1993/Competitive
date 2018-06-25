
def left_rotate( a, number_of_rotations ):

	array_length = len(a)
	mod = number_of_rotations%array_length

	rotated = [ i for i in range( array_length )]

	for i in range(array_length):
		rotated[i] = a[ ( mod + i )% array_length]

	return rotated

if __name__ == '__main__':
    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    a = left_rotate( a, d )



    print " ".join( map( str, a ) )

    #print " ".join( a )