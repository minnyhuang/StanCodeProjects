"""
File: anagram.py
Name: Minny
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

lst = []
sub_lst = []


def main():
    """
    TODO:
    """
    ####################
    print('Welcome to stanCode\"Anagram Generator\"( or -1 to quit)')
    read_dictionary()
    start, end = 0, 0
    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break
        else:
            start = time.time()
            find_anagrams(word)
            end = time.time()
    ####################
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    # 讀取字典文字檔並存入list
    global lst
    with open(FILE, 'r') as f:
        for line in f:
            info_list = line.split()
            lst += info_list


def sub_dict(sub):
    # 建立新字典
    global sub_lst
    # 建立空的list
    sub_s = []
    # 把查詢的單字sub，字母分開存入空的list
    sub_s += sub
    for i in range(len(lst)):
        # 字數長度一樣則繼續
        if len(sub) == len(lst[i]):
            # 如果字典的單字開頭為查詢單字sub的其中一個字母則繼續
            if lst[i][0] in sub_s:
                # 如果字典的單字倒數最後一位為查詢單字sub的其中一個字母則繼續
                if lst[i][-1] in sub_s:
                    # 若原字典的字串排序後與查詢的字串排序後相等，則將此字串放入新字典
                    if sorted(sub) == sorted(lst[i]):
                        sub_lst.append(lst[i])


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    global sub_lst
    # 建立新字典
    sub_dict(s)
    # 建立空的list用來存入最後print的結果
    ana_lst = []
    # 計次最後print的結果有幾個anagrams
    count = [0]
    run = [0]
    # recursion
    find_anagrams_helper(s, '', ana_lst, count, run)
    # print anagrams
    print(str(count[0]) + ' anagrams: ', ana_lst)
    print(run)
    # 將新字典清空
    sub_lst = []


def find_anagrams_helper(s, current_str, ana_lst, count, run):
    run[0] += 1
    # 當字串長度相等時停止recursion
    if len(s) == len(current_str):
        # 如果anagram的結果可於新字典找到則加入ana_lst
        if current_str in sub_lst:
            ana_lst.append(current_str)
            count[0] += 1
            print('Searching...')
            print('Found: ' + current_str)
    # recursion
    else:
        # prune：比對新字典是否有以current_str為開頭的單字
        if has_prefix(current_str):
            for i in range(len(s)):
                # 將要查詢的單字s排序
                s = sorted(s)
                # prune：查看此次要查詢的字母與前次是否相同(因相同字母recursion的結果會一樣）
                if s[i] != s[i-1]:
                    # prune：如果目前要串的字母已存在於current_str且數量跟查詢的單字s相同則結束
                    if s[i] in current_str and current_str.count(s[i]) == s.count(s[i]):
                        pass
                    else:
                        # Choose
                        current_str += s[i]
                        # Explore
                        find_anagrams_helper(s, current_str, ana_lst, count, run)
                        # Un-choose
                        current_str = current_str[:-1]


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    # 查詢目前的字串是否於新字典可以找到已它為開頭的單字
    for i in range(len(sub_lst)):
        # 若找到第一筆則break
        if str(sub_lst[i]).startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
