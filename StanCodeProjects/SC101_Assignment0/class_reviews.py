"""
File: class_reviews.py
Name: Minny
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""
# This constant controls when to stop
EXIT = '-1'

def main():
    """
    TODO: Calculating the scores of each class.
    """
    cla = input('Which class? ')
    cla = cla.upper()
    if cla == EXIT:
        print('No class scores were entered')
    else:
        data = int(input('Score:'))
        max001 = data                # 定義SC001的最大值
        min001 = data                # 定義SC001的最小值
        num001 = 0                   # 計次SC001的分數
        total001 = 0                 # 加總SC001的分數
        max101 = data                # 定義SC101的最大值
        min101 = data                # 定義SC101的最小值
        num101 = 0                   # 計次SC101的分數
        total101 = 0                 # 加總SC101的分數
        while True:
            if cla == 'SC001':              # 判斷是否為SC001
                if data > max001:
                    max001 = data
                elif data < min001:
                    min001 = data
                num001 += 1
                total001 += data
            if cla == 'SC101':              # 判斷是否為SC101
                if data > max101:
                    max101 = data
                elif data < min101:
                    min101 = data
                num101 += 1
                total101 += data
            cla = input('Which class? ')
            cla = cla.upper()
            if cla == EXIT:
                break
            data = int(input('Score:'))
        print("=============SC001=============")
        if num001 == 0:
            print('No score for SC001')
        else:
            print("Max(001):" + str(max001))
            print("Min(001):" + str(min001))
            print("Ave(001):" + str(total001 / num001))
        print("=============SC101=============")
        if num101 == 0:
            print('No score for SC101')
        else:
            print("Max(101):" + str(max101))
            print("Min(101):" + str(min101))
            print("Ave(101):" + str(total101 / num101))


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
