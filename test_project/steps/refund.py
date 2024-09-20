from test_project.business_layer.windows.orderWindow import orderWindow
from test_project.business_layer.windows.closedChecksWindow import closedChecksWindow
import log_file
from behave import *


logging = log_file.get_logs()


@step(u'user selects "Search Closed Checks" on the top navigation bar')
def step_impl(context):
    orderWindow().clickSearchClosedChecks()


@step(u'user should see list of closed checks should populate on the screen along with filters to filter the search')
def step_impl(context):
    closedChecksWindow().verifyClosedChecksWindow()


@step(u'user select the check that was just created via the Pay Per Item test case')
def step_impl(context):
    closedChecksWindow().selectClosedCheck()


@step(u'user should see the check number to the right of the check receipt')
def step_impl(context):
    closedChecksWindow().verifyCheckreceipt()


@step(u'user select Full Refund')
def step_impl(context):
    closedChecksWindow().clickFullRefund()


@step(u'user should see "Full refund" pop up should be displayed asking to confirm the refund')
def step_impl(context):
    closedChecksWindow().verifyFullRefundPopUp()


@step(u'user select "Continue"')
def step_impl(context):
    closedChecksWindow().clickContinueButton()


@step(u'user should see "Select a Refund Reason" pop up')
def step_impl(context):
    closedChecksWindow().verifySelectAReasonPopUp()


@step(u'user Select a reason of the refund and click the Full Refund button')
def step_impl(context):
    closedChecksWindow().clickOverringReason()


@step(u'user should see "Full Refund Completed" pop up')
def step_impl(context):
    closedChecksWindow().verifyRefundCompletedPopUp()


@step(u'user click "Ok" and click back arrow which is on top left corner')
def step_impl(context):
    closedChecksWindow().clickOkAndBackArrow()


@step(u'user selects "hamburger menu" in the bottom right corner')
def step_impl(context):
    orderWindow().clickHamburgerMenu()
