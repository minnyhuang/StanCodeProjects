"""
File: boggle.py
Name: Minny
----------------------------------------
TODO: create a "boggle" to match every exist vocabs in the dictionary with the 4x4 character input
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO: create a "boggle" to match every exist vocabs in the dictionary with the 4x4 character input
	"""
	word_lst = []
	# 排出一個 4 x 4 的方形字母若輸入不符合規定則顯示"illegal format"
	for i in range(4):
		word = input(str(i + 1) + " row of letters: ")
		row_lst = []
		if len(word) != 7:
			print("Illegal input")
			break
		for j in range(4):
			row_lst += word[(2 * j)].lower()
		word_lst.append(row_lst)
	start = time.time()
	####################
	boggle(word_lst)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(s):
	processed = []
	word_lst = []
	count = [0]
	# 將所有字母作為開頭遞迴所有可能的單字結果
	for i in range(4):
		for j in range(4):
			boggle_helper(s, '', read_dictionary(s)[s[i][j]], word_lst, i, j, count, processed)
	# print最後的結果
	print('There are ' + str(count[0]) + ' words in total.')


def boggle_helper(s, current_str, s_dict, word_lst, i, j, count, processed):
	# 如果單字的結果可於字典找到則加入word_lst
	if current_str in s_dict:
		if current_str not in word_lst:
			count[0] += 1
			word_lst.append(current_str)
			print('Found ' + '\"' + current_str + '\"')
	# recursion
	# prune：比對字典是否有以current_str為開頭的單字
	if has_prefix(s_dict, current_str):
		# 用double for loop串所有可能的單字
		for k in range(-1, 2, 1):
			for m in range(-1, 2, 1):
				if 0 <= i+k < 4 and 0 <= j+m < 4:
					# 串過的字母塊不能重複被選擇
					if (i+k, j+m) not in processed:
						# Choose
						current_str += s[i+k][j+m]
						# 儲存被選過的字母塊位址
						processed.append((i+k, j+m))
						# Explore
						boggle_helper(s, current_str, s_dict, word_lst, i+k, j+m, count, processed)
						# Un-choose
						processed.pop()
						current_str = current_str[:-1]


def read_dictionary(s):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	sub_s = []
	# 把要串連的字母存入空的list
	for i in range(len(s)):
		for j in range(len(s[i])):
			sub_s += s[i][j]
	# 讀取字典文字檔並將單字開頭字母存為key，當單字長度大於4則排除
	lst = {}
	with open(FILE, 'r') as f:
		for line in f:
			info_list = line.split()
			if len(info_list[0]) >= 4:
				# 若單字的開頭至第四位與最後一位字母，皆可於串連的字母list(sub_s)找到則存入字典
				if info_list[0][0] not in lst:
					if info_list[0][0] in sub_s:
						if info_list[0][1] in sub_s:
							if info_list[0][2] in sub_s:
								if info_list[0][3] in sub_s:
									if info_list[0][-1] in sub_s:
										lst[info_list[0][0]] = [info_list[0]]
				else:
					if info_list[0][0] in sub_s:
						if info_list[0][1] in sub_s:
							if info_list[0][2] in sub_s:
								if info_list[0][3] in sub_s:
									if info_list[0][-1] in sub_s:
										lst[info_list[0][0]].append(info_list[0])
	return lst


def has_prefix(s, sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	# 查詢目前的字串是否於字典可以找到以它為開頭的單字
	for i in range(len(s)):
		# 若找到第一筆則break
		if str(s[i]).startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
