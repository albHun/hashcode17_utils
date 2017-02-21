from random_supporting_functions import *

# Set up input data and our representation
file_name = ""
input_data = open(file_name)
table = load_input(input_data)

partition_par1 = 5
partition_par2 = 5
blocks = partition(table, partition_par1, partition_par2)

trial = 100000
best_methods = list()

temp_methods = list()
for block in blocks:
	config = ...
	best_block_methods = list()
	covered = list()
	for j in range(0, trial):
		pick_random_element(table, )
