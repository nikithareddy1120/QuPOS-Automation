@qpos
Feature: payPerItem Feature

  Scenario:
    Given The user launch the "Qu POS" desktop application
    Then user should be able to see the "login" screen
    When user enter an employee "ID" on a counter sign in screen and select "Log In" button
    And user selects the "hamburger menu" in the bottom right corner
    Then user should see the "Claim/Close Till" and "Show Open Checks" options on the top navigation menu of the screen.
    When user select "Claim/Close Till" option
    Then user should see "Till Device Selection" popup
    When user select "Claim" on an available till and verify the till marked as "claimed" and "current cash" in the till
    And user select the "X" button on the til popup
    And user select "DineIn" from the drop down displayed on top left corner
    Then user should see the "DineIn" option which is selected from dropdown
    When user add multiple items to the order
    Then user should see the cart view, subtotal, tax, total on the left side of the screen
    When user select an entree in the cart
    Then user should see entree modification items on the right side of the screen
    When user remove a default modifier by clicking on it
    Then user should see "No (default modifier name)"
    When user add a free modifier by clicking on it
    Then user should see "Add (free modifier name)"
    When user add a priced modifier by clicking on it
    Then user should see "Add (priced modifier name)", and the total should reflect the additional price of the modifier
    When user clicks on "Quick Suspend", "hamburger menu"
    Then user should see the "Claim/Close Till" and "Show Open Checks" options on the top navigation menu of the screen.
    When user clicks on "Show Open Checks"
    Then user should see "All Checks" text and "All order types" dropdown
    When user selects the check by clicking on it.
    Then user should see the Total Amount of the check
    When user select "Payment" button
    Then user should see list of all the available payment methods
    When user click on cash
    Then user should see "Due Amount" of all the items and "Apply Payment" button should be displayed
    When user clicks on Pay per Item, select the items and click on Ok
    And user click on "Apply Payment"
    Then user should see list of all the available payment methods
    When user click on cash
    Then user should see the "Due Amount" and "Apply Payment" button should be displayed
    When user clicks on Pay per Item, select items and click on Ok
    And user click on "Apply Payment"
    Then user see the Total amount as Zero and "No Checks" text
    When user selects the "hamburger menu" in the bottom right corner
    Then user should see the Logout button on the top navigation bar
    And user select "Logout" button on the top navigation bar

