# -*- coding: utf-8 -*-
"""This is a Lettuce living place.
We configure there setUp() and tearDown()
and also some useful methods and attributes."""
from lettuce import world
from lettuce.terrain import before, after
from framework import SeleniumStart
from framework.system import System
from time import time
from unittest2 import TestCase

@before.all
def __init__():
    """Gets system configuration."""
    world.system = System()

@before.each_scenario
def setUp(scenario):
    """Sets up the test fixture before exercising it."""
    # initialize system
    configuration = world.system.selenium_conf
    configuration['base-url'] = world.system.base_url
    world.s = SeleniumStart(configuration)
    # initialize attributes
    world.s.timestamp = int(time())
    world.verificationErrors = []

@after.each_scenario
def tearDown(scenario):
    """Deconstructs the test fixture after testing it."""
    # stop Selenium RC
    world.s.stop()
    # assert results
    TestCase(None).assertEqual([], world.verificationErrors)