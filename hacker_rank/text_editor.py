#!/usr/bin/python
import sys
"""
implementing the text ediotrr
"""

if __name__ == "__main__":
	print_stack = []
	operation_stack = []
	main_string = ""

	command_count = int( sys.stdin.readline().strip() )

	while command_count > 0:

		line = sys.stdin.readline().strip()

		command = int( line.split(" ")[0] )

		if command == 1:
			add_string = line.split(" ")[1]
			main_string += add_string
			operation_stack.append( {1:add_string})

		elif command == 2:
			delete_index = int( line.split(" ")[1] )
			main_string_length = len( main_string )
			deleted_string = main_string[main_string_length-delete_index:main_string_length]
			operation_stack.append( {2:[ delete_index, deleted_string] })

		elif command == 3:
			print_index = int( line.split(" ")[1] )
			print_char = main_string[print_index-1:print_index]
			print_stack.append( print_char )

		else:
			last_operation = operation_stack.pop()
			for key,value in  last_operation:
				if key == 1:
					string_to_be_truncated = value
					length_string = len( string_to_be_truncated )
					length_main_string = len( main_string )
					main_string = main_string[0:( length_main_string-length_string )]

				else:
					last_delete_index = value[0]
					last_deleted_string = value[1]
					main_string = main_string + last_deleted_string


		command_count -= 1


	for item in print_stack:
		print item

