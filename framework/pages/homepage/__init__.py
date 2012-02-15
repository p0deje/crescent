# -*- coding: utf-8 -*-
from framework.pages import parse_locators
from framework import verify_equal
from lettuce import world

# parse locators.cfg file
locators = parse_locators(open('framework/pages/homepage/locators.cfg', 'r'))

def search_fill(keyword):
    """Enters keyword to search field."""
    world.selenium.find_element_by_name(locators['search_field']).\
        send_keys(keyword)

def search_submit():
    """Submits search."""
    world.selenium.find_element_by_name(locators['search_button']).click()

def verify_result_one(expected):
    e = world.selenium.find_element_by_css_selector(locators['result_one'])
    actual = e.text
    verify_equal(expected, actual,
                 'Link to Wikipedia is on top.')