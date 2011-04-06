from ConfigParser import RawConfigParser

class LocatorsParser(object):
    def parse_locators(self, file, *sections):
        """Parses locators configuration file and
        returns dictionary of locators.

        Arguments:
        file = locators file object (opened with open() method)
        sections = tuple of sections in locators file
        """
        locators = {}
        parser = RawConfigParser()
        parser.readfp(file)
        for section in sections:
            print section
            for name in parser.options(section):
                locators[name] = parser.get(section, name)
        return locators