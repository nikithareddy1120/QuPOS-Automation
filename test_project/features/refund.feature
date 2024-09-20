@qpos
Feature: refund Feature

  Scenario:
    Given The user launch the "Qu POS" desktop application
    Then user should be able to see the "login" screen
    When user enter an employee "ID" on a counter sign in screen and select "Log In" button
    And user selects the "hamburger menu" in the bottom right corner
    Then user should see the "Claim/Close Till" and "Show Open Checks" options on the top navigation menu of the screen.
    When user selects "Search Closed Checks" on the top navigation bar
    Then user should see list of closed checks should populate on the screen along with filters to filter the search
    When user select the check that was just created via the Pay Per Item test case
    Then user should see the check number to the right of the check receipt
    When user select Full Refund
    Then user should see "Full refund" pop up should be displayed asking to confirm the refund
    When user select "Continue"
   Then user should see "Select a Refund Reason" pop up
    When user Select a reason of the refund and click the Full Refund button
    Then user should see "Full Refund Completed" pop up
    When user click "Ok" and click back arrow which is on top left corner
    And user selects "hamburger menu" in the bottom right corner
    Then user should see the Logout button on the top navigation bar
    And user select "Logout" button on the top navigation bar
