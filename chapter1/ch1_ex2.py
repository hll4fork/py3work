#########################################################################
# auhtor        : huanglilongwk@qq.com
# time          : 2016/4/21
# brief         : <Programming in Python3 > chapter1 exercise 2 (page:47)
##########################################################################

# How to solve this problem
# 1. get number input from user until empty line get(just ENTER got)
# 2. save number entered in number_ins
# 3. count numbers and save in counts
# 4. calculate the sum
# 5. get min for current
# 6. get max for current
# 7. get mean = sum / counts

number = [] # list for save number from input
sum_n = max_n = counts = 0
min_n = 9
while True:
    number_ins = input("Enter a number or Enter to finish:") # 2. save numbers
    if number_ins:
        try:
            number.append(int(number_ins))
        except ValueError as err:
            print(err, "in", "input")
            continue
        if int(number_ins) > max_n:     # 6. ger max number
            max_n = int(number_ins)
        if int(number_ins) < min_n:     # 5. get min number
            min_n = int(number_ins)
        sum_n += int(number_ins)        # 4. calculate sum
        counts += 1                     # 3. count the numbers
    else:
        break

if counts:
    for n in number:    # 1. print enter numbers
        print(n)
    print("max: ", max_n)
    print("min: ", min_n)
    print("counts: ", counts)
    print("sum: ", sum_n)
    print("mean: ", sum_n/counts)



