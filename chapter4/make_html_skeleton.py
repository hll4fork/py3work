#!/usr/bin/env python3

########################################################################
# auhtor        : huanglilongwk@qq.com
# time          : 2016/5/11
# brief         ; <Programming in Python3 > chapter4 example 1 (page:185)
#########################################################################

import datetime
import xml.sax.saxutils

class CancelledError(Exception):pass

COPYRIGHT_TEMPLATE = "Copyright (c) {0} {1}. All right reserved."
STYLESHEET_TEMPLATE = ('<link rel="stylesheet" type="text/css" '
                       'media="all" href="{0}" />\n')

HTML_TEMPLATE = """<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" \
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<title>{title}</title>
<!-- {copyright} -->
<meta name="Description" content="{description}" />
<meta name="Keywords" content="{keywords}" />
<meta equiv="content-type" content="text/html; charset=utf-8" />
{stylesheet}\
</head>
<body>
    Have fun !
</body>
</html>
"""

def main():
    information = dict(name=None, year=datetime.date.today().year,
                       filename=None, title=None, description=None,
                       keywords=None, stylesheet=None)
    while True:
        try:
            print("\nMake HTML Skeleton\n")
            populate_information(information)
            make_html_skeleton(**information)   # keyword unpacking
        except CancelledError:
            print("Cancelled")
        if (get_string("\nCreate another (y/n)?", default="y").lower() not in {"y", "yes"}):
            break

def populate_information(information):
    name = get_string("Enter your name (for copyright)", "name", information["name"])
    if not name:
        raise CancelledError()
    year = get_integer("Enter copyright year", "year",
                      information["year"], 2000,
                      datetime.date.today().year+1, True)

    if year == 0:
        raise CancelledError()
    filename = get_string("Enter filename", "filename")
    if not filename:
        raise CancelledError()
    if not filename.endswith((".html", ".html")):
        filename += ".html"
    title = get_string("Enter title", "title")
    if not title:
        raise CancelledError()
    description = get_string("Enter the stylesheet filename ", "optional", "stylesheet")

    keywords = []
    while True:
        keyword = get_string("Enter a keyword(optional)", "keyword")
        if keyword:
            keywords.append(keyword)
        else:       # empty line from command-line
            break
    stylesheet = get_string("Enter the stylesheet filename "
                            "(optional)", "stylesheet")
    if stylesheet and not stylesheet.endswith(".css"):
        stylesheet += ".css"
    information.update(name=name, year=year, filename=filename,
                       title=title, description=description,
                       keywords=keywords, stylesheet=stylesheet)

def make_html_skeleton(year, name, title, description, keywords,
                       stylesheet, filename):
    copyright = COPYRIGHT_TEMPLATE.format(year, xml.sax.saxutils.escape(name))
    title = xml.sax.saxutils.escape(title)
    description = xml.sax.saxutils.escape(description)
    keywords = ",".join([xml.sax.saxutils.escape(k)
                         for k in keywords]) if keywords else ""
    stylesheet = (STYLESHEET_TEMPLATE.format(stylesheet)
                  if stylesheet else "")
    html = HTML_TEMPLATE.format(**locals())
    fh = None
    try:
        fh = open(filename, "w", encoding="utf8")
        fh.write(html)
    except EnvironmentError as err:
        print("Error", err)
    else:
        print("Save skeleton", filename)
    finally:
        if fh is not None:
            fh.close()

def get_string(message, name="string", default=None,
               minimum_length=0, maximum_length=80):
    message += ":" if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(**locals()))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{name} must have at least "
                                 "{minimum_length} and at most "
                                 "{maximum_length} characters".format(**locals()))
            return line
        except ValueError as err:
            print("ERROR", err)

def get_integer(message, name="integer", default=None, minimum=0,
                maximum=100, allow_zero=True):
    class RangeError(Exception):pass
    message +=": " if default is None else " [{0}]: ".format(default)
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
                                 "and {maximum} inclusive{0}".format(
                    " (or 0)" if allow_zero else "", **locals()))
            return i
        except RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR {0} must be an integer".format(name))

main()
