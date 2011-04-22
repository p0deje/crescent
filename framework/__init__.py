from selenium import selenium
from unittest2 import TestCase
from lettuce import world

class SeleniumStart(object):
    def __init__(self, configuration):
        if configuration['version'] == 1:
            self._start_selenium_rc(configuration)
        elif configuration['version'] == 2:
            self._start_selenium_webdriver(configuration)
        else:
            error = 'Selenium version is not set.'
            error += 'Check you system.cfg confiugraion file'
            raise RuntimeError, error

    def _start_selenium_rc(self, configuration):
        """Starts Selenium RC connection."""
        s = selenium(configuration['hostname'],
                     configuration['port'],
                     configuration['browser'],
                     configuration['base-url'])
        return s.start()

    def _start_selenium_webdriver(self, configuration):
        pass


class SoftAsserts(object):
    def verifyEqual(expected, actual, msg=None):
        try: TestCase(None).assertEqual(expected, actual, msg)
        except AssertionError, e: world.verificationErrors.append(e)

    def verifyTrue(expr, msg=None):
        try: TestCase(None).assertTrue(expr, msg)
        except AssertionError, e: world.verificationErrors.append(e)

    def verifyTrue(expr, msg=None):
        try: TestCase(None).assertTrue(expr, msg)
        except AssertionError, e: world.verificationErrors.append(e)


class SeleniumRCExtensions(object):
    """Some useful extensions for Selenium."""
    def __init__(self, selenium):
        self.selenium = selenium

    def click_and_wait(self, locator, timeout):
        """Clicks locator and automatically waits for page to load."""
        self.selenium.selenium.click(locator)
        self.selenium.selenium.wait_for_page_to_load(timeout)