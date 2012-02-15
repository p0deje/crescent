## No longer developed

## Description

Python framework for automated testing with a bit of Behavior-Driven Development via Lettuce (http://lettuce.it) and Selenium RC.

## Usage

1. Configure System Under Test in framework/system/system.cfg.
2. Add users (if necessary) in framework/users/users.cfg.
3. Write page objects in framework/pages dir.
4. Create a feature in features/ directory.
5. Write step definitions in features/step_definitions directory.
6. Run with `lettuce`!

## Lettuce terrain.py

Test fixture, setUp() and tearDown() for tests are defined in features/terrain.py. Take a look at it.

## Locators configuration

It's recommended to store locators in separate .cfg file. You can after call LocatorsParser().parse_locators(file, sections) to parse the locators file. For example, you want to create page object for SearchPage. You create directory pages/searcpage and define SearchPage class in __init__py. You also make "from framework.pages import LocatorsParser". In constructor of your class you just call parse_locators() method.

## Access to Selenium instance

In most Page-Object pattern you pass selenium instance as an argument to page class constructor. And you access it like "self.selenium". In Crescent, you otherwise pass "world" as an argument to page class constructor. Thus, access to Selenium is like "self.world.selenium".
