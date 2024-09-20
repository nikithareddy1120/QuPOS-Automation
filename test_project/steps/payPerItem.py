from test_project.business_layer.windows.checksWindow import checksWindow
from test_project.business_layer.windows.loginWindow import loginWindow
from test_project.business_layer.windows.orderWindow import orderWindow
import log_file
from behave import *

from test_project.business_layer.windows.paymentWindow import paymentWindow

logging = log_file.get_logs()


@given(u'The user launch the "Qu POS" desktop application')
def step_impl(context):
    loginWindow().launchApp()
    logging.info("Qu POS application has launched successfully")


@step(u'user should be able to see the "login" screen')
def step_impl(context):
    loginWindow().verifyloginScreen()


@step(u'user enter an employee "ID" on a counter sign in screen and select "Log In" button')
def step_impl(context):
    loginWindow().enterEmployeeID()
    loginWindow().clickLoginButton()


@step(u'user selects the "hamburger menu" in the bottom right corner')
def step_impl(context):
    orderWindow().clickHamburgerMenu()


@step(u'user should see the "Claim/Close Till" and "Show Open Checks" options on the top navigation menu of the screen.')
def step_impl(context):
    orderWindow().verifyNavigationMenu()


@step(u'user select "Claim/Close Till" option')
def step_impl(context):
    orderWindow().clickClaimCloseTillOption()


@step(u'user should see "Till Device Selection" popup')
def step_impl(context):
    orderWindow().verifyTillDeviceSelectionPopup()


@step(u'user select "Claim" on an available till and verify the till marked as "claimed" and "current cash" in the till')
def step_impl(context):
    orderWindow().selectAvailableTill()


@step(u'user select the "X" button on the til popup')
def step_impl(context):
    orderWindow().closeTillPopup()


@step(u'user select "DineIn" from the drop down displayed on top left corner')
def step_impl(context):
    orderWindow().selectDineInFromDropDrown()

@step(u'user should see the "DineIn" option which is selected from dropdown')
def step_impl(context):
    orderWindow().verifyDineInOption()

@step(u'user add multiple items to the order')
def step_impl(context):
    orderWindow().selectbreakfastItem()
    orderWindow().selectLunchItem()
    orderWindow().selectKidsMeals()


@step(u'user should see the cart view, subtotal, tax, total on the left side of the screen')
def step_impl(context):
    orderWindow().verifyTotalPriceOfItems()


@step(u'user select an entree in the cart')
def step_impl(context):
    orderWindow().selectEntreeInTheCart()


@step(u'user should see entree modification items on the right side of the screen')
def step_impl(context):
    orderWindow().verifySelectedEntreeIsDisplayed()


@step(u'user remove a default modifier by clicking on it')
def step_impl(context):
    orderWindow().removeDefaultModifiers()


@step(u'user should see "No (default modifier name)"')
def step_impl(context):
    orderWindow().verifyRemovedModifier()


@step(u'user add a free modifier by clicking on it')
def step_impl(context):
    orderWindow().addFreeModifier()


@step(u'user should see "Add (free modifier name)"')
def step_impl(context):
    orderWindow().verifyFreeModifier()


@step(u'user add a priced modifier by clicking on it')
def step_impl(context):
    orderWindow().addPricedModifier()


@step(u'user should see "Add (priced modifier name)", and the total should reflect the additional price of the modifier')
def step_impl(context):
    orderWindow().verifyPricedModifier()


@step(u'user clicks on "Quick Suspend", "hamburger menu"')
def step_impl(context):
    orderWindow().clickQuickSuspend()
    orderWindow().clickHamburgerMenu()


@step(u'user clicks on "Show Open Checks"')
def step_impl(context):
    orderWindow().clickShowOpenChecks()


@step(u'user should see "All Checks" text and "All order types" dropdown')
def step_impl(context):
    checksWindow().verifyChecksWindow()


@step(u'user selects the check by clicking on it.')
def step_impl(context):
    checksWindow().openCheck()


@step(u'user should see the Total Amount of the check')
def step_impl(context):
    orderWindow().verifyTotalPriceOfItems()


@step(u'user select "Payment" button')
def step_impl(context):
    paymentWindow().clickPaymentButton()


@step(u'user should see list of all the available payment methods')
def step_impl(context):
    paymentWindow().verifyPaymentMethods()


@step(u'user click on cash')
def step_impl(context):
    paymentWindow().clickCashPaymentMethod()


@step(u'user should see "Due Amount" of all the items and "Apply Payment" button should be displayed')
def step_impl(context):
    paymentWindow().verifyDueAmount()
    paymentWindow().verifyApplyPaymentButton()


@step(u'user clicks on Pay per Item, select the items and click on Ok')
def step_impl(context):
    paymentWindow().clickPayPerItemAndSelectItems()


@step(u'user click on "Apply Payment"')
def step_impl(context):
    paymentWindow().clickApplyPayment()


@step(u'user should see the "Due Amount" and "Apply Payment" button should be displayed')
def step_impl(context):
    paymentWindow().verifyApplyPaymentButton()

@step(u'user clicks on Pay per Item, select items and click on Ok')
def step_impl(context):
    paymentWindow().clickPayPerItemAndSelectRestOfTheItems()


@step(u'user see the Total amount as Zero and "No Checks" text')
def step_impl(context):
    orderWindow().verifyWindowAfterPayment()


@step(u'user should see the Logout button on the top navigation bar')
def step_impl(context):
    orderWindow().verifyLogoutButton()


@step(u'user select "Logout" button on the top navigation bar')
def step_impl(context):
    orderWindow().clickLogoutButton()
    # loginWindow().closeApplication()
