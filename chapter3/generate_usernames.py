#!/usr/bin/env python3
#########################################################################
# auhtor        : huanglilongwk@qq.com
# time          : 2016/5/2
# brief         : <Programming in Python3 > chapter3 example 1 (page:149)
# cmd           : generate_usernames.py data/users.txt
##########################################################################

# must add "#!/usr/bin/env python3" on the first line, i don't kown why

import sys
import collections

ID, FORNAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)
User = collections.namedtuple("User", "username, forname, middlename, surname, id")

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("Usage: {0} file1 [file2 [...[fileN]]".format(sys.argv[0]))
        sys.exit()

    usernames = set()            # no duplicates
    users = {}
    for filename in sys.argv[1:]:                   # get filenames from command-line
        for line in open(filename,encoding="utf8"):
            line = line.rstrip()                     # remove right and left whitespace
            if line:    # not empty line
                user = process_line(line, usernames)
                users[(user.surname.lower(), user.forname.lower(), user.id)] = user # 3-tuple -> key, user -> value
    print_users(users)

def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FORNAME], fields[MIDDLENAME],fields[SURNAME], fields[ID])
    return user

def generate_username(fields, usernames):
    username = ((fields[FORNAME][0] + fields[MIDDLENAME][:1] + fields[SURNAME].replace("-", "").replace("'","")))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:    # deal with duplicate names(huanglilong -> huanglilong{count})
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username

def print_users(users):
    namewidth = 32
    usernamewidth = 9
    print("{0:<{nw}} {1:^6} {2:{uw}}".format(
        "Name", 'ID', "Username", nw=namewidth, uw=usernamewidth))
    print("{0:-<{nw}} {0:-<6} {0:-<{uw}}".format(
        "", nw=namewidth, uw=usernamewidth
    ))
    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
            name = "{0.surname}, {0.forname}{1}".format(user, initial)
            print("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}".format(
                name, user, nw=namewidth, uw=usernamewidth
            ))

main()