from lettuce import world, step
import framework.pages.homepage

@step('Given I am on homepage')
def open_page(step):
    world.selenium.get(world.system.base_url)

@step('When I enter "(.+)" to the "Search" field')
def search_fill(step, keyword):
    framework.pages.homepage.search_fill(keyword)

@step('And click "Search"')
def search_submit(step):
    framework.pages.homepage.search_submit()

@step('Then I see the first result "(.+)"')
def verify_search(step, keyword):
    framework.pages.homepage.verify_result_one(keyword)