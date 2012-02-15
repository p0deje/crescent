Feature: Google search
    In order to test Google search
    We will search something on Google
    And make sure the results are displayed

    # Positive scenario
    Scenario: First Search
        Given I am on homepage
        When I enter "behavior driven development" to the "Search" field
        And click "Search"
        Then I see the first result "Behavior Driven Development - Wikipedia, the free encyclopedia"