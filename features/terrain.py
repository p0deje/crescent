# -*- coding: utf-8 -*-
"""This is a Lettuce living place.
We configure there setUp() and tearDown()
and also some useful methods and attributes."""
from lettuce import world
from lettuce.terrain import before, after
from framework.system import System
from selenium import selenium
from time import time

@before.each_scenario
def setUp(scenario):
    """Sets up the test fixture before exercising it."""
    # initialize Selenium RC
    world.system = System()
    world.selenium = selenium(world.system.selenium_conf['hostname'],
                              world.system.selenium_conf['port'],
                              world.system.selenium_conf['browser'],
                              world.system.base_url)
    world.selenium.start()
    # initialize attributes
    world.selenium.timestamp = int(time())
    world.selenium.timeout = 30000
    # initialize methods
    world.selenium.click_and_wait = click_and_wait

@after.each_scenario
def tearDown(scenario):
    """Deconstructs the test fixture after testing it."""
    # stop Selenium RC
    world.selenium.stop()

def click_and_wait(locator, timeout):
    """Clicks locator and automatically waits for page to load."""
    world.selenium.click(locator)
    world.selenium.wait_for_page_to_load(timeout)