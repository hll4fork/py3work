#!/usr/bin/env python3
#
# author        : huanglilongwk@qq.com
# time          : 2016/5/21
# brief         : <Programming in Python3 > chapter5 optparse example (page:215)
# ref           : csv2html2_opt.py

import sys
import optparse

#
# opts save the processed command-line arguments
# args save the unprocessed command-line arguments
#


def main():
    parser = optparse.OptionParser()
    parser.add_option("-w", "--maxwidth", dest="maxwidth", type="int",
                      help=("the maxinum number of characters that can be "
                           "output to string fields [default; %default]"))
    parser.add_option("-f", "--format", dest="format",
                      help=("the format used for outputing numbers "
                            "[default: %default]"))
    parser.set_defaults(maxwidth=100, format="0.f")
    opts, args = parser.parse_args()

    # print msgs
    print(("maxwidth is {0}, format is {1}").format(opts.maxwidth, opts.format))
    print("args:")
    for a in args:
        print(a)


main()
