from random_supporting_functions import *

# Set up input data and our representation
file_name = ""
input_data = open(file_name)
table = load_input(input_data)
# Number of elements that finish the representation of a block
n_elements = 2

partition_par1 = 5
partition_par2 = 5
blocks = partition(table, partition_par1, partition_par2)

iteration = 10000
trial = 100000
best_methods = list()

for block in blocks:
	config = # To be completed
	best_block_methods = list()
	for i in range(0, iteration):
		covered = list()
		temp_methods = list()
		for j in range(0, trial):
			restrictions = list()
			# Restrictions to randomly select elements to be completed
			elements = pick_random_element(table, n_elements, restrictions)
			subblock = table_construct(elements)
			if check_if_valid(table, covered, subblock):
				update_covered(covered, subblock)
				temp_methods.append(subblock)
		if check_rewards(table, temp_methods) > check_rewards(table, best_block_methods):
			best_block_methods = temp_methods
	best_methods.extend(best_block_methods)

