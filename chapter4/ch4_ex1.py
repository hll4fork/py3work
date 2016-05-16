#!/usr/bin/env python3
########################################################################
# author        : huanglilongwk@qq.com
# time          : 2016/5/11
# brief         ; <Programming in Python3 > chapter4 example 1 (page:192)
#########################################################################

import os

YES = frozenset({"y", "Y", "yes", "Yes", "YES"})  # immutable set


def main():
    dirty = False
    items = []

    filename, items = choose_file()
    if not filename:
        print("Cancelled")
        return

    while True:
        print("\nList Keeper\n")
        print_list(items)
        choice = get_choice(items, dirty)

        if choice in "Aa":
            dirty = add_item(items, dirty)
        elif choice in "Dd":
            dirty = delete_item(items, dirty)
        elif choice in "Ss":
            dirty = save_list(filename, items, dirty)
        elif choice in "Qq":
            if(dirty and (get_string("Save unsaved changes(y/n)",
                                     "yes/no", "y") in YES)):
                save_list(filename, items, True)
            break


def choose_file():
    enter_filename = False
    print("\nList Keeper\n")
    files = [x for x in os.listdir(".") if x.endswith(".lst")]  # find all .lst file in current directory
    if not files:   # empty
        enter_filename = True
    if not enter_filename:  # have .lst files
        print_list(files)
        index = get_integer("Specify file's number (or 0 to create a new one)",
                            "number", maximum=len(files))
        if index == 0:
            enter_filename = True
        else:
            filename = files[index - 1]  # start from 1
            items = load_list(filename)  # load line from filename.lst to items -> filename.lst's contents
    if enter_filename:
        filename = get_string("choose filename", "filename")
        if not filename.endswith(".lst"):
            filename += ".lst"
        items = []
    return filename, items


def print_list(items):
    if not items:
        print("-- no items are in the list --")
    else:
        width = 1 if len(items) < 10 else 2 if len(items) < 100 else 3
        for i, item in enumerate(items):
            print("{0:{width}}:{item}".format(i+1, **locals()))
    print()


def get_choice(items, dirty):
    while True:
        if items:
            if dirty:   # have changes
                menu = "[A]dd [D]elete [S]ave [Q]uit"
                valid_choices = "AaDdSsQq"
            else:       # no changes
                menu = "[A]dd [D]elete [Q]uit"
                valid_choices = "AaDdQq"
        else:           # no items
            menu = "[A]dd [Q]uit"
            valid_choices = "AaQq"
        choice = get_string(menu, "choice", "a")

        if choice not in valid_choices:  # invalid choice
            print("ERROR:invalid choice--enter one of '{0}'".format(valid_choices))
            input("Press Enter to continue...")
        else:
            return choice


def add_item(items, dirty):
    item = get_string("Add item", "item")
    if item:
        items.append(item)
        items.sort(key=str.lower)
        return True     # file has changed
    return dirty        # return prev dirty status


def delete_item(items, dirty):
    index = get_integer("Delete item number (or 0 to cancel)", "number",
                        maximum=len(items), allow_zero=True)
    if index != 0:
        del items[index - 1]
        return True
    return dirty


def load_list(filename):
    items = []
    fh = None
    try:
        for line in open(filename, encoding="utf8"):
            items.append(line.rstrip())
    except EnvironmentError as err:
        print("ERROR: failed to load {0}:{1}".format(filename, err))
        return []
    finally:
        if fh is not None:
            fh.close()      # why fh is the opening file's file reference ?
    return items


def save_list(filename, items, terminating=False):
    fh = None
    try:
        fh = open(filename, "w", encoding="utf8")
        fh.write("\n".join(items))
        fh.write("\n")
    except EnvironmentError as err:
        print("ERROR: failed to load {0}:{1}".format(filename, err))
        return True
    else:
        print("Save {0} item{1} to {2}".format(len(items),
             ("s" if len(items) != 1 else ""), filename))
        if not terminating:
            input("Press Enter to continue...")
        return False
    finally:
        if fh is not None:
            fh.close()


def get_string(message, name="string", default=None,
               minimum_length=0, maximum_length=80):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(
                        name))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{name} must have at least "
                                 "{minimum_length} and at most "
                                 "{maximum_length} characters".format(**locals()))
            return line
        except ValueError as err:
            print("ERROR", err)


def get_integer(message, name="integer", default=None, minimum=0,
                maximum=100, allow_zero=True):
    class RangeError(Exception):
        pass

    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError("{0} may not be 0".format(name))
            if not (minimum <= i <= maximum):
                raise RangeError("{name} must be between {minimum} "
                                 "and {maximum} inclusive{0}".format(" (or 0)" if allow_zero else "", **locals()))
            return i
        except RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR {0} must be an integer".format(name))


main()