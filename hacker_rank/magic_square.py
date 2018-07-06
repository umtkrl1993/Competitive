



import math
import os
import random
import re
import sys

pre = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        ]


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
	global pre
    
	totals = []
	for p in pre:
		total = 0
		for p_row, s_row in zip(p, s):
			for i, j in zip(p_row, s_row):
				if not i == j:
					total += max([i, j]) - min([i, j])
		totals.append(total)
	return min(totals)

if __name__ == '__main__':
	

    s = []

    for _ in xrange(3):
        s.append(map(int, raw_input().rstrip().split()))

    result = formingMagicSquare(s)

    sys.stdout.write(str(result) + '\n')

