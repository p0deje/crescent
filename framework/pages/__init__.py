# -*- coding: utf-8 -*-
from ConfigParser import RawConfigParser

def parse_locators(file):
    """Parses locators configuration file and
    returns dictionary of locators.

    Arguments:
    file = locators file object (opened with open() method)

    Return:
    Dictionary of parsed locators."""
    # parse file
    parser = RawConfigParser()
    parser.readfp(file)
    # get sections from file
    sections = parser.sections()
    # prepare locators dictionary
    locators = {}
    # don't add sections name
    # when only one section exists
    if len(sections) is 1:
        section = sections[0]
        for name in parser.options(section):
            locators[name] = parser.get(section, name)
    # add section name as a key
    # when more than one section exists
    else:
        for section in sections:
            locators[section] = {}
            for name in parser.options(section):
                locators[section][name] = parser.get(section, name)
    # return dictionary of parsed locators
    return locators