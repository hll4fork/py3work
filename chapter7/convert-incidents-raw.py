#!/usr/bin/env python3
#
# Author    : huanglilong <huanglilongwk@qq.com>
# Time      : 2016/5/21
# Ref       : <Programming in Python3 > chapter7 convert-incidents.py
# Brief     : using struct module -- write and read binary file
#

import locale
locale.setlocale(locale.LC_ALL, "")

import datetime
import gzip
import optparse
import os
import struct
import sys


MAGIC = b"AIB\x00"
FORMAT_VERSION = b"\x00\x01"
GZIP_MAGIC = b"\x1F\x8B"

NumbersStruct = struct.Struct("<Idi?")

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


    def export_binary(self, filename, compress=False):

        def pack_string(string):
            data = string.encode("utf8")                # for string, must give encoding parameter
            formats = "<H{0}s".format(len(data))
            return struct.pack(formats, len(data), data)

        fh = None
        try:
            if compress:
                fh = gzip.open(filename, "wb")
            else:
                fh = open(filename, "wb")
            fh.write(MAGIC)                  # write magic number
            fh.write(FORMAT_VERSION)         # write version number
            for incident in self.values():  # generate incidents
                data = bytearray()
                data.extend(pack_string(incident.report_id))
                data.extend(pack_string(incident.airport))
                data.extend(pack_string(incident.aircraft_id))
                data.extend(pack_string(incident.aircraft_type))
                data.extend(pack_string(incident.narrative.strip()))
                data.extend(NumbersStruct.pack(
                    incident.date.toordinal(),
                    incident.pilot_percent_hours_on_type,
                    incident.pilot_total_hours,
                    incident.midair))
                fh.write(data)
            return True
        except EnvironmentError as err:
            print("{0}: export error:{1}".format(
                os.path.basename(sys.argv[0]), err
            ))
            return False
        finally:
            if fh is not None:
                fh.close()

    def import_binary(self, filename):

        def unpack_string(fh, eof_is_error=True):
            size_format = struct.Struct("<H")
            length_data = fh.read(size_format.size)     # return read data size in bytes
            if not length_data:
                if eof_is_error:
                    raise ValueError("missing or corrupt string size")
                return None
            length = size_format.unpack(length_data)[0]
            if length == 0:
                return ""
            data = fh.read(length)
            if not data or len(data) != length:        # less data read from file
                raise ValueError("missing or corrupt string")
            formats = "<{0}s".format(length)
            return struct.unpack(formats, data)[0].decode("utf8")

        fh = None
        try:
            fh = open(filename, "rb")
            magic = fh.read(len(GZIP_MAGIC))
            if magic == GZIP_MAGIC:
                fh.close()
                fh = gzip.open(filename, "rb")
            else:
                fh.seek(0)
            magic = fh.read(len(MAGIC))
            if magic != MAGIC:
                raise ValueError("unrecognized file format")
            version = fh.read(len(FORMAT_VERSION))
            if version > FORMAT_VERSION:
                raise ValueError("unrecognized file version")
            self.clear()
            while True:
                report_id = unpack_string(fh, False)
                if report_id is None:
                    break
                data = {}
                data["report_id"] = report_id
                for name in ("airport", "aircraft_id", "aircraft_type", "narrative"):
                    data[name] = unpack_string(fh, False)
                other_data = fh.read(NumbersStruct.size)
                numbers = NumbersStruct.unpack(other_data)
                data["date"] = datetime.date.fromordinal(numbers[0])
                data["pilot_percent_hours_on_type"] = numbers[1]
                data["pilot_total_hours"] = numbers[2]
                data["midair"] = numbers[3]
                incident = Incident(**data)
                self[incident.report_id] = incident
            return True
        except (EnvironmentError, ValueError, IncidentError) as err:
            print("{0}: import error: {1}".format(
                os.path.basename(sys.argv[0]), err
            ))
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
    aircraft_incidents.export_binary(opts.file, compress=False)

    # pickle read binary file
    aircraft_incidents = IncidentCollection()
    aircraft_incidents.import_binary(opts.file)
    for key in aircraft_incidents:
        print(("the read incident from binary file is: {0}").format(key))



main()

# report_id     : 2007061289X(string)                     --> 11 bytes
# date          : datetime.date(2007, 6, 12)(uint32)      --> 4 bytes
# airport       : Los Angeles(string)                     --> 11 bytes
# aircraft_id   : 8184XK(string)                          --> 6 bytes
# aircraft_type : CVS91(string)                           --> 5 bytes
# pilot_percent_hours_on_type : 17.5(double)              --> 8 bytes
# pilot_total_hours           : 1258(uint32)              --> 4 bytes
# midair                      : False(bool)               --> 1 bytes
# narrative                   : ""                        --> 0 bytes

# total size
# string_size = 11 + 11 + 6 + 5 + 5*2 = 43
# integer_size = 4 + 8 + 4 + 1 = 17
# magic_version_size = 4 + 2 = 6
# total = 43 + 17 + 6 = 66
