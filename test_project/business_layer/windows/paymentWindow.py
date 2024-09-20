import time
from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
import log_file
from core_layer.utility.assertions import Assertions
from test_project.business_layer.windows.orderWindow import orderWindow

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver = DriverFactory.create_driver(framework_type)
pywinauto_config = config.get_pywinauto_config()
waits_config = config.get_waits_config()

class paymentWindow:

    APPLYPAYMENTBUTTON = {"title":"Apply Payment", "auto_id":"CashPayment_ApplyPayment_Button_Cash", "control_type":"Button"}
    CASH = {"title":"Cash", "auto_id":"Cash", "control_type":"Button"}
    CREDIT = {"title":"Credit", "auto_id":"Credit", "control_type":"Button"}
    OFFLINECREDIT = {"title":"Offline Credit", "auto_id":"Offline Credit", "control_type":"Button"}
    OTHERDIGITAL = {"title":"Other Digital", "control_type":"ListItem"}
    PAYMENTBUTTON = {"title":"Payment"}
    PAYPERITEM = {"title":"Pay per Item", "auto_id":"CashPayment_PayPerItem_Button_Cash", "control_type":"Button"}
    ITEMONE = {"auto_id":"PayPerItemItemPrice_47587-47958-48038"}
    ITEMTWO = {"auto_id":"PayPerItemItemPrice_47587-56634-56775"}
    ITEMTHREE = {"auto_id":"PayPerItemItemPrice_47587-47893-47957"}
    OKBUTTON = {"title": "OK"}
    NOTHANKS = {"title":"NO THANKS", "auto_id":"-NO THANKS", "control_type":"Button"}
    DUEAMOUNT = {"auto_id": "CashPayment_SetAmount_Button_Cash"}

    def __init__(self):
        self.orderwindow = orderWindow()
        self.assertions = Assertions(driver)

    def clickPaymentButton(self):
        driver.utilities.click_button(driver.app, self.PAYMENTBUTTON, "Payment button", waits_config['veryShortWait'])
        time.sleep(waits_config['shortWait'])
        driver.utilities.click_button(driver.app, self.NOTHANKS, "No Thanks button", waits_config['veryShortWait'])
        time.sleep(waits_config['shortWait'])

    def verifyPaymentMethods(self):
        driver.utilities.is_element_displayed(driver.app, self.CASH, "Cash button", waits_config['veryShortWait'])
        driver.utilities.is_element_displayed(driver.app, self.CREDIT, "Credit button", waits_config['veryShortWait'])
        driver.utilities.is_element_displayed(driver.app, self.OFFLINECREDIT, "Offline Credit button", waits_config['veryShortWait'])
        driver.utilities.is_element_displayed(driver.app, self.OTHERDIGITAL, "Other Digital button", waits_config['veryShortWait'])

    def clickCashPaymentMethod(self):
        driver.utilities.click_button(driver.app, self.CASH, "Cash button", waits_config['veryShortWait'])
        time.sleep(waits_config['veryShortWait'])

    def verifyDueAmount(self):
        dueAmount = driver.utilities.get_text(driver.app, self.DUEAMOUNT, "Due Amount", waits_config['veryShortWait'])   # Due Amount
        # logging.info(dueAmount)
        totalAmount = self.orderwindow.verifyTotalPriceOfItems()
        self.assertions.assert_equal(dueAmount, totalAmount)

    def verifyApplyPaymentButton(self):
        driver.utilities.is_element_displayed(driver.app, self.APPLYPAYMENTBUTTON, "Apply Payment button", waits_config['veryShortWait'])
        time.sleep(waits_config['shortWait'])

    def clickPayPerItemAndSelectItems(self):
        driver.utilities.click_button(driver.app, self.PAYPERITEM, "Pay per Item button", waits_config['veryShortWait'])
        time.sleep(waits_config['shortWait'])
        driver.utilities.click_button(driver.app, self.ITEMONE, "Item one from Select Check Items to Pay popup", waits_config['veryShortWait'])
        driver.utilities.click_button(driver.app, self.ITEMTWO, "Item two from Select Check Items to Pay popup", waits_config['veryShortWait'])
        driver.utilities.click_button(driver.app, self.OKBUTTON, "OK button", waits_config['veryShortWait'])

    def clickPayPerItemAndSelectRestOfTheItems(self):
        driver.utilities.click_button(driver.app, self.PAYPERITEM, "Pay per Item button", waits_config['veryShortWait'])
        time.sleep(waits_config['shortWait'])
        driver.utilities.click_button(driver.app, self.ITEMTHREE, "Item two from Select Check Items to Pay popup", waits_config['veryShortWait'])
        driver.utilities.click_button(driver.app, self.OKBUTTON, "OK button", waits_config['veryShortWait'])

    def clickApplyPayment(self):
        driver.utilities.click_button(driver.app, self.APPLYPAYMENTBUTTON, "Apply Payment button", waits_config['veryShortWait'])
        time.sleep(waits_config['shortWait'])
