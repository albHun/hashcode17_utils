from random import randint

def table_construct(*argv):
	"""Construct a table with argv."""
	return table

def get_table_element(table, *argv):
	"""Return element in the table with given parameters."""
	return element

def load_input(input_data):
	"""This function loads the input_data and change it to our preferred
	representation and outputs as table."""
	return table

def pick_random_element(table, lower_limits, higher_limits):
	"""This function generates random numbers from a table with
	two limits. The element picked have parameters r[0], r[1], r[2], r[3] ... r[n-1]
	that satisfy lower_limits[i] <= r[i] <= higher_limits[i] for any i."""
	parameters = list()
	for l, h in lower_limits, higher_limits:
		par = randint(l, h)
		parameters.add(par)
	return get_table_element(table, parameters)

def partition(table, grids_dir1, grids_dir2):
	"""This function divides the table into smaller tables with sizes of 
	small tables specified in parameters: grids_dir1 * grids_dir2. This
	function returns a complete list of smaller tables"""
	subtables = list()
	count_dir1 = 0
	count_dir2 = 0
	
	return subtables

def construct_random_blocks(table, *args):
	"""This function constructs a block of elements in some representation
	which is sophisticated for each case and hence cannot be implemented 
	generally."""

def check_if_valid(table, covered, new_block):
	"""This function checks if a new block is valid to put on with existing 
	covered "area" and if it satisfies the condition required for a block
	It returns a binary value: True for valid and False for invalid."""

def update_covered(covered, new_block):
	"""Say no more."""

def check_rewards(table, covered):
	"""Check how many point we have earned."""