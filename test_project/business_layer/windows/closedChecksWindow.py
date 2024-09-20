import re
import time
from core_layer.utility.assertions import Assertions
from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
import log_file
from core_layer.utility.yamlManager import YamlUtilities

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver = DriverFactory.create_driver(framework_type)
pywinauto_config = config.get_pywinauto_config()
waits_config = config.get_waits_config()

class closedChecksWindow:

    LISTOFCLOSEDCHECKS = {"auto_id":"ClosedCheck_Results_GridView"}
    ALLORDERTYPESDROPDOWN = {"title":"All order types", "auto_id":"ContentPresenter", "control_type":"ListItem"}
    ALLORDERCHANNELSDROPDOWN = {"title":"All order channels", "auto_id":"ContentPresenter", "control_type":"ListItem"}
    TODAYBUTTON = {"auto_id":"SearchToday_Button"}
    BACKARROW = {"auto_id":"cnbSettingsPage"}
    FULLREFUNDBUTTON = {"auto_id":"ClosedCheck_FullRefund_Button"}
    CONTINUEBUTTON = {"title" : "Continue", "auto_id" : "Full Refund-Continue", "control_type" : "Button"}
    TEXTINFULLREFUNDPOPUP = {"title" : "You have selected to Full Refund the check. Do you want to proceed or go back?", "control_type" : "Text"}
    SELECTAREASONPOPUP = {"title" : "Select a Refund Reason", "auto_id" : "TitleTextBlock", "control_type" : "Text"}
    OVERRINGREASON = {"title":"Select", "auto_id":"ReasonsFlyoutItemView_Select1116_Button", "control_type":"Button"}
    FULLREFUNDAFTERSELECTINGREASON = {"auto_id":"ReasonsFlyoutView_ActionButton", "control_type":"Button"}
    OKBUTTON = {"title":"OK", "auto_id":"Full Refund Completed-OK", "control_type":"Button"}
    FULLREFUNDCOMPLETED_TEXT = {"title":"Full Refund Completed", "control_type":"Text"}
    CHECKRECEIPT = {"auto_id":"CheckDetails"}

    def __init__(self):
        self.yamlmanager = YamlUtilities()
        self.yamlmanager.read_from_yaml_file()
        self.assertions = Assertions(driver)

    def verifyClosedChecksWindow(self):
        driver.utilities.is_element_displayed(driver.app, self.LISTOFCLOSEDCHECKS, "List of all closed checks", waits_config['veryShortWait'])
        driver.utilities.is_element_displayed(driver.app, self.ALLORDERTYPESDROPDOWN, "All order types Dropdown", waits_config['veryShortWait'])
        driver.utilities.is_element_displayed(driver.app, self.ALLORDERCHANNELSDROPDOWN, "All order channels drop down", waits_config['veryShortWait'])

    def selectClosedCheck(self):
        driver.utilities.click_button(driver.app, self.TODAYBUTTON, "Today button", waits_config['veryShortWait'])
        extractedchecknumber = self.yamlmanager.get_data_from_yaml('checknumber')
        match = re.search(r"#(\d+)", extractedchecknumber)
        if match:
            result = match.group(1)
            recentCheck = driver.utilities.get_locator_by_title(result)
            driver.utilities.click_button(driver.app, recentCheck, "clicked on the check", waits_config['veryShortWait'])

    def clickFullRefund(self):
        if driver.utilities.is_element_enabled(driver.app, self.FULLREFUNDBUTTON, waits_config['veryShortWait']):
            logging.info("Full Refund button in enabled")
            driver.utilities.click_button(driver.app, self.FULLREFUNDBUTTON, "Full Refund", waits_config['veryShortWait'])
        else:
            logging.error("Full Refund button is not enabled")

    def verifyFullRefundPopUp(self):
        driver.utilities.is_element_displayed(driver.app, self.TEXTINFULLREFUNDPOPUP, "Text 'You have selected to Full Refund the check' in full refund popup", waits_config['veryShortWait'])

    def clickContinueButton(self):
        driver.utilities.click_button(driver.app, self.CONTINUEBUTTON, "Continue Button", waits_config['veryShortWait'])

    def verifySelectAReasonPopUp(self):
        driver.utilities.is_element_displayed(driver.app, self.SELECTAREASONPOPUP, "Select a Refund Reason popup", waits_config['veryShortWait'])

    def clickOverringReason(self):
        driver.utilities.click_button(driver.app, self.OVERRINGREASON, "Select a Refund Reason popup", waits_config['veryShortWait'])
        driver.utilities.click_button(driver.app, self.FULLREFUNDAFTERSELECTINGREASON, "Full Refund button", waits_config['veryShortWait'])
        time.sleep(waits_config['longWait'])

    def verifyRefundCompletedPopUp(self):
        driver.utilities.is_element_displayed(driver.app, self.FULLREFUNDCOMPLETED_TEXT, "Select a Refund Reason popup", waits_config['veryShortWait'])

    def clickOkAndBackArrow(self):
        driver.utilities.click_button(driver.app, self.OKBUTTON, "Ok button", waits_config['veryShortWait'])
        time.sleep(waits_config['shortWait'])
        driver.utilities.click_button(driver.app, self.BACKARROW, "Back Arrow", waits_config['veryShortWait'])

    def verifyCheckreceipt(self):
        checknumber = driver.utilities.get_text(driver.app, self.CHECKRECEIPT, "Ok button", waits_config['veryShortWait'])
        extractedchecknumber = self.yamlmanager.get_data_from_yaml('checknumber')
        match = re.search(r"#(\d+)", extractedchecknumber)
        if match:
            result = match.group(1)
        self.assertions.assert_contains(checknumber, result)
