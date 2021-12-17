"""
File: largest_digit.py
Name: Minny
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	# 確認n為正數
	if n < -1:
		n = n * -1
	# 當n剩個位數即為最大值
	if n % 10 == n:
		return n
	else:
		# 取個位數與十位數比較，當個位數小於等於十位數，保留除個位數以外的數字
		if n % 10 <= (int(n/10)) % 10:
			return find_largest_digit(int(n/10))
		# 當個位數大於十位數，扣除十位數的數字，保留其餘數字
		elif n % 10 > (int(n / 10)) % 10:
			return find_largest_digit(int(n/10)-((int(n / 10)) % 10)+n % 10)


if __name__ == '__main__':
	main()
