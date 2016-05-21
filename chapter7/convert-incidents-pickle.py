#!/usr/bin/env python3
#
# Author    : huanglilong <huanglilongwk@qq.com>
# Time      : 2016/5/21
# Ref       : <Programming in Python3 > chapter7 convert-incidents.py
# Brief     : using pickle module -- write and read binary file
#


import locale
locale.setlocale(locale.LC_ALL, "")

import datetime
import gzip
import optparse
import os
import pickle
import sys

MAGIC = b"AIB\x00"
FORMAT_VERSION = b"\x00\x01"
GZIP_MAGIC = b"\x1F\x8B"


class IncidentError(Exception): pass


class Incident:

    def __init__(self, report_id, date, airport, aircraft_id,
                 aircraft_type, pilot_percent_hours_on_type,
                 pilot_total_hours, midair, narrative=""):
        assert len(report_id) >= 8 and len(report_id.split()) == 1, \
            "invalid report ID"
        self.__report_id = report_id
        self.date = date
        self.airport = airport
        self.aircraft_id = aircraft_id
        self.aircraft_type = aircraft_type
        self.pilot_percent_hours_on_type = pilot_percent_hours_on_type
        self.pilot_total_hours = pilot_total_hours
        self.midair = midair
        self.narrative = narrative

    @property
    def report_id(self):
        return self.__report_id

    @property
    def date(self):
        "The incident date"
        return self.__date

    @date.setter
    def date(self, date):
        assert isinstance(date, datetime.date), "invalid date"
        self.__date = date

    @property
    def pilot_percent_hours_on_type(self):
        "The percentage of total hours flown on this aircraft type"
        return self.__pilot_percent_hours_on_type

    @pilot_percent_hours_on_type.setter
    def pilot_percent_hours_on_type(self, percent):
        assert 0.0 <= percent <= 100.0, "out of range percentage"
        self.__pilot_percent_hours_on_type = percent

    @property
    def pilot_total_hours(self):
        "The total hours this pilot has flown"
        return self.__pilot_total_hours

    @pilot_total_hours.setter
    def pilot_total_hours(self, hours):
        assert hours > 0, "invalid number of hours"
        self.__pilot_total_hours = hours

    @property
    def approximate_hours_on_type(self):
        return int(self.__pilot_total_hours *
                   (self.__pilot_percent_hours_on_type / 100))

    @property
    def midair(self):
        "Whether the incident involved another aircraft"
        return self.__midair

    @midair.setter
    def midair(self, value):
        assert isinstance(value, bool), "invalid midair value"
        self.__midair = value

    @property
    def airport(self):
        "The incident's airport"
        return self.__airport

    @airport.setter
    def airport(self, airport):
        assert airport and "\n" not in airport, "invalid airport"
        self.__airport = airport

    @property
    def aircraft_id(self):
        "The aircraft ID"
        return self.__aircraft_id

    @aircraft_id.setter
    def aircraft_id(self, aircraft_id):
        assert aircraft_id and "\n" not in aircraft_id, \
            "invalid aircraft ID"
        self.__aircraft_id = aircraft_id

    @property
    def aircraft_type(self):
        "The aircraft type"
        return self.__aircraft_type

    @aircraft_type.setter
    def aircraft_type(self, aircraft_type):
        assert aircraft_type and "\n" not in aircraft_type, \
            "invalid aircraft type"
        self.__aircraft_type = aircraft_type

    @property
    def narrative(self):
        "The incident's narrative"
        return self.__narrative

    @narrative.setter
    def narrative(self, narrative):
        self.__narrative = narrative

    def __repr__(self):
        return ("Incident({report_id!r}, {date!r}, "
                "{airport!r}, {aircraft_id!r}, "
                "{aircraft_type!r}, "
                "{pilot_percent_hours_on_type!r}, "
                "{pilot_total_hours!r}, {midair!r}, "
                "'''{narrative}''')".format(**self))

class IncidentCollection(dict):

    def values(self):
        for report_id in self.keys():
            yield self[report_id]

    def items(self):
        for report_id in self.keys():
            yield (report_id, self[report_id])

    def __iter__(self):
        for report_id in sorted(super().keys()):
            yield report_id

    keys = __iter__

    def __reversed__(self):
        for report_id in sorted(super().keys(), reverse=True):
            yield report_id

    def export_pickle(self, filename, compress=False):
        fh = None
        try:
            if compress:
                fh = gzip.open(filename, "wb")
            else:
                fh = open(filename, "wb")
            pickle.dump(self, fh, pickle.HIGHEST_PROTOCOL)
            return True
        except (EnvironmentError, pickle.PicklingError) as err:
            print("{0}: export error: {1}".format(
                os.path.basename(sys.argv[0]), err))
            return False
        finally:
            if fh is not None:
                fh.close()

    def import_pickle(self, filename):
        fh = None
        try:
            fh = open(filename, "rb")
            magic = fh.read(len(GZIP_MAGIC))
            if magic == GZIP_MAGIC:
                fh.close()
                fh = gzip.open(filename, "rb")
            else:
                fh.seek(0)
            self.clear()
            self.update(pickle.load(fh))
            return True
        except (EnvironmentError, pickle.UnpicklingError) as err:
            print("{0}: import error: {1}".format(
                os.path.basename(sys.argv[0]), err))
            return False
        finally:
            if fh is not None:
                fh.close()


def process_options():
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="file",
                      help=("binary file [default: %default]"))
    parser.set_defaults(file="test_file")
    opts, args = parser.parse_args()
    return opts


def main():
    opts = process_options()

    # pickle write binary file
    aircraft_incidents = IncidentCollection()
    incident = Incident("2007061289X", datetime.date(2007, 6, 12), "Los Angeles",
                        "8184XK", "CVS91", 17.5, 1258, False)
    aircraft_incidents[incident.report_id] = incident
    aircraft_incidents.export_pickle(opts.file, compress=False)

    # pickle read binary file
    aircraft_incidents = IncidentCollection()
    aircraft_incidents.import_pickle(opts.file)
    for key in aircraft_incidents:
        print(("the read incident from binary file is: {0}").format(key))



main()
