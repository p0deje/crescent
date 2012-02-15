# -*- coding: utf-8 -*-
from selenium import selenium
from selenium import webdriver
from unittest2 import TestCase
from lettuce import world

def start_selenium(configuration):
    """Starts Selenium session.

    Arguments:
    configuration - dictionary of Selenium configuration settings.

    Return:
    Selenium instance."""
    # get version
    version = int(configuration['version'])
    # if version is 1, start Selenium RC
    if version == 1:
        s = selenium(configuration['hostname'],
                     configuration['port'],
                     configuration['browser'],
                     configuration['base-url'])
        s.start()
    # if version is 2, start Selenium Webdriver
    elif version == 2:
        # initialize correct browser
        browser = configuration['browser'].lower()
        if browser == 'firefox':
            s = webdriver.Firefox()
        elif browser == 'chrome':
            s = webdriver.Chrome()
        elif browser == 'ie':
            s = webdriver.Ie()
        else:
            error = "Unknown browser. Can't start Webdriver session."
            raise RuntimeError, error
    # otherwise raise error
    else:
        error = 'Selenium version is not set. Check you system.cfg file.'
        raise RuntimeError, error
    return s

def verify_equal(expected, actual, msg=None):
    """Softly asserts that two values are equal."""
    try: TestCase(None).assertEqual(expected, actual, msg)
    except AssertionError, e: world.verification_errors.append(str(e))

def verify_true(expr, msg=None):
    """Softly asserts that expression is True."""
    try: TestCase(None).assertTrue(expr, msg)
    except AssertionError, e: world.verification_errors.append(str(e))

def verify_false(expr, msg=None):
    """Softly asserts that expression is False."""
    try: TestCase(None).assertTrue(expr, msg)
    except AssertionError, e: world.verification_errors.append(str(e))


class SeleniumRCExtensions(object):
    """Some useful extensions for Selenium."""
    def __init__(self, selenium):
        self.selenium = selenium

    def click_and_wait(self, locator, timeout):
        """Clicks locator and automatically waits for page to load."""
        self.selenium.click(locator)
        self.selenium.wait_for_page_to_load(timeout)