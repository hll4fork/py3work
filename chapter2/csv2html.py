#!/usr/bin/env python3

#########################################################################
# auhtor        : huanglilongwk@qq.com
# time          : 2016/4/29
# brief         : <Programming in Python3 > chapter2 example 3 (page:97)
##########################################################################

# Notes
# 1. !/usr/bin/env python3 -> must be added first here, i don't kown why.
# 2. pycharm can't redirect to a file, so csv2html.py need run from cmd.exe

import sys

def main():
    maxwidth = 100
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:              # first line from csv file
                color = "lightgreen"
            elif count % 2:             # every one line
                color = "white"
            else:
                color = "lightyellow"  # every one line
            print_line(line, color, maxwidth)
            count += 1
        except EOFError:
            break
    print_end()

def print_start():
    print("<table border='1'>")

def print_line(line, color, maxwidth):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line) # extract fields from line to a list(fields)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")     # remove "," from number
            try:
                x = float(number)
                print("<td align='right'>{0:d}</td>".format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = escape_html(field)
                else:
                    field = "{0} ...".format(
                            escape_html(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")

# state machine for extract fields
def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start of quoted string, check for first (\"') characters
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c    # other quote inside quoted string
            continue
        if quote is None and c == ",": # end of a field
            fields.append(field)
            field = ""
        else:
            field += c        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


def escape_html(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


def print_end():
    print("</table>")


main()
