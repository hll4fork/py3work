#########################################################################
# auhtor        : huanglilongwk@qq.com
# time          : 2016/4/25
# brief         : <Programming in Python3 > chapter1 exercise 5 (page:47)
##########################################################################

# How to solve the problem
# 1. read integer from input, until a empty line input
# 2. sort the input
# 3. find the middle value and print

datas =[]
end_flag = False
try:
    while True:
        line = input("Enter integers: ")
        if line:
            value = int(line)
            datas.append(value)
        else:
            # sort datas(from small to large)
            row = 0
            while row < len(datas) - 1:
                column = 0
                end_flag = True
                while column < (len(datas) - row) - 1:
                    if datas[column] > datas[column + 1]:
                        temp = datas[column + 1]
                        datas[column + 1] = datas[column]
                        datas[column] = temp
                        end_flag = False
                    column += 1
                if end_flag:
                    break;
                print(datas)
                row += 1

            # find and print middle value
            if len(datas)%2 == 0:
                middle_value = (datas[len(datas)//2] + datas[len(datas)//2 -1])/2
            else:
                middle_value = datas[len(datas)//2]
            print("middle value is: ", middle_value)
            break
except ValueError:
    print("can't convert to int")


