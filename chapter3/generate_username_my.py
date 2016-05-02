#!/usr/bin/env python3

########################################################################
# auhtor        : huanglilongwk@qq.com
# time          : 2016/5/2
# brief         ; <Programming in Python3 > chapter3 example 1 (page:149)
# cmd           ; generate_username_my.py data/users.txt
#########################################################################

# How to solve this problem
# 1. get line from file
# 2. strip right and left whitespaces
# 3. split with ":"
# 4. generate user name

import sys
import collections

ID, FORENAME, MIDNAME, SURNAME, DEPARTNAME = range(5)
User = collections.namedtuple("User", "username, forename, midname, surname, id")

def main():
    # no filename specific here or "-h" and "--help" asking for usage
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("Usage:{0} filename [filename2]".format(sys.argv[0]))
        sys.exit()

    # process file got from command-line
    users = {}
    usernames = set()
    for filename in sys.argv[1:]:
        for line in open(filename, encoding="utf8"):
            line = line.rstrip() # remove right and left spacewhites
            if line:
                user = process_line(line, usernames)    # get unique username
                users[user.surname.lower(), user.forename.lower(), user.id] = user
                print(user.username)

def process_line(line, usernames):
    fields = line.split(":")
    username = generate_name(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDNAME], fields[SURNAME], fields[ID])
    return user

def generate_name(fields, usernames):
    username = fields[FORENAME][0] + fields[MIDNAME][:1] + fields[SURNAME]
    count = 1
    origin_name = username
    while username in usernames:
        username = origin_name
        username = "{0}{1}".format(username, count)
        count += 1
    usernames.add(username)
    return username

main()
