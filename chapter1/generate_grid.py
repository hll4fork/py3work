############################################
# file		: generate_grid.py
# author	: huanglilongwk@qq.com
# time		: 2016/4/18
# brief		: generate grid output
############################################
import random						# use random module

def get_int(msg, minimum, default): # define a function
	while True:
		try:
			line = input(msg)
			if not line and default is not None:
				return default
			i = int(line)
			if i < minimum:
				print("must be >=", minimum)
			else:
				return i
		except ValueError as err:	# if line can't convert to digital
			print(err)

rows = get_int("rows:", 1, None)		# row --> get a value > 1
columns = get_int("columns:", 1, None)	# column --> get a value > 1
minimum = get_int("minimum(or Enter for 0):", -1000000, 0)

default = 1000
if default < minimum:
	default = 2 * minimum
maximum = get_int("maximum (or Enter for " + str(default) + "): ", minimum, default)

# print big digital
row = 0
while row < rows:
	line = ""
	column = 0
	while column < columns:
		i = random.randint(minimum, maximum)
		s = str(i)
		while len(s) < 10:
			s = " " + s
		line += s 
		column += 1
	print(line)
	row += 1