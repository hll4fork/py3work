####################################################
# File		: bigdigits.py
# Author	: huanglilongwk@qq.com
# Time		: 2016/4/19
# Brief		: generate big digits output
#####################################################

import sys # use sys.argv for getting args from command-line

Digitals = [
			["   ***   ",
			 " *     * ",
			 "*       *",
			 "*       *",
			 "*       *",
			 " *     * ",
			 "   ***   "],
			["    *    ",
			 "   **    ",
			 "    *    ",
			 "    *    ",
			 "    *    ",
			 "    *    ",
			 "    *    "],
			["   ***   ",
			 "  *   *  ",
			 "  *  *   ",
			 "    *    ",
			 "   *     ",
			 "  *      ",
			 " ********"],
			["  *****  ",
			 "     *   ",
			 "    *    ",
			 "   *     ",
			 "    *    ",
			 "     *   ",
			 "  *****  "],
			["    *    ",
			 "  * *    ",
			 " *  *    ",
             "******** ",
			 "    *    ",
			 "    *    ",
			 "    *    "],
			[" ******* ",
			 " *     * ",
			 " *       ",
			 "   *     ",
			 "     *   ",
			 " *     * ",
			 " ******* "],
			[" ******  ",
			 " *       ",
			 " *       ",
			 " ******* ",
			 " *     * ",
			 " *     * ",
			 " ******* "],
			[" ******* ",
			 "       * ",
			 "       * ",
			 "       * ",
			 "       * ",
			 "       * ",
			 "       * "],
			[" ******* ",
			 " *     * ",
			 " *     * ",
			 " ******* ",
			 " *     * ",
			 " *     * ",
			 " ******* "],
			[" ******* ",
			 " *     * ",
			 " *     * ",
			 " ******* ",
			 "       * ",
			 "       * ",
			 " ******* "]]

try:
    digits = sys.argv[1]            # get the digit from command-line
    row = 0
    while row < 7:                 # 7 -> max row for big digit
        line = ""
        column = 0
        while column < len(digits):         # get the number of digits
            number = int(digits[column])     # convert string into integer
            digit = Digitals[number]
            line += digit[row] + " "
            column += 1
        print(line)
        row += 1
except IndexError:                              # argments not digit(can be converted to digit)
    print('usage: bigdigits.py <number>')
except ValueError as err:                       # stirng can't convert to interger
    print(err, "in", digits)