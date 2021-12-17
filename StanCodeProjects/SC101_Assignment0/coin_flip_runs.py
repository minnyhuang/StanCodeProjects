"""
File: coin_flip_runs.py
Name: Minny
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r

num_run = 15

def main():
	"""
	TODO: This program should simulate coin flip(s) with the number of runs input by users.
	"""
	print('Let’s flip a coin! ')
	runs = int(input('Number of runs: '))
	roll1 = r.randrange(1, 3)
	if roll1 == 1:
		print('H', end='')
	if roll1 == 2:
		print('T', end='')
	run = 0
	is_in_a_row = False
	while True:
		roll2 = r.randrange(1, 3)
		if roll1 == roll2:            # 判斷是否連續擲出同面
			if not is_in_a_row:
				run += 1
				is_in_a_row = True
		else:
			is_in_a_row = False        # 若擲出不同面則開始計算新的run
		roll1 = roll2
		if roll2 == 1:
			print('H', end='')
		if roll2 == 2:
			print('T', end='')
		if run == runs:
			break


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
