# -*- coding: utf-8 -*-

""" This is a Lettuce living place.
We configure there setUp() and tearDown()
and also some useful methods and attributes. """

from lettuce import world
from lettuce.terrain import before, after
from framework.system import System
from time import time
import framework

@before.all
def __init__():
    """Gets system configuration."""
    world.system = System()

@before.each_scenario
def set_up(scenario):
    """Sets up the test fixture before exercising it."""
    # initialize system
    configuration = world.system.selenium_conf
    configuration['base-url'] = world.system.base_url
    world.selenium = framework.start_selenium(configuration)
    # initialize attributes
    world.selenium.timestamp = int(time())
    world.verification_errors = []

@after.each_scenario
def tear_down(scenario):
    """Deconstructs the test fixture after testing it."""
    # stop Selenium
    version = int(world.system.selenium_conf['version'])
    if version == 1: world.selenium.stop()
    elif version == 2: world.selenium.quit()
    else: raise Exception, "Couldn't stop Selenium instance."
    # assert there were no errors
    framework.verify_false(world.verification_errors)