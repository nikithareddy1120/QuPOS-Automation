import re
import time
from core_layer.utility.yamlManager import YamlUtilities
from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
import log_file
from test_project.business_layer.windows.orderWindow import orderWindow

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver = DriverFactory.create_driver(framework_type)
pywinauto_config = config.get_pywinauto_config()
waits_config = config.get_waits_config()

class checksWindow:

    ALLCHECKS = {"title":"All Checks", "control_type":"Text"}
    ALLORDERTYPES = {"title":"All order types", "auto_id":"filterByOrderTypeButton", "control_type":"Button"}

    def __init__(self):
        self.orderwindow = orderWindow()
        self.yamlmanager = YamlUtilities()
        self.yamlmanager.read_from_yaml_file()


    def verifyChecksWindow(self):
        driver.utilities.is_element_displayed(driver.app, self.ALLCHECKS, "All Checks text",  waits_config['veryShortWait'])
        driver.utilities.is_element_displayed(driver.app, self.ALLORDERTYPES, "All Order types button", waits_config['veryShortWait'])

    def openCheck(self):
        extractedchecknumber = self.yamlmanager.get_data_from_yaml('checknumber')
        match = re.search(r"#(\d+)", extractedchecknumber)
        if match:
            result = match.group()
            checklocator = driver.utilities.get_locator_by_title(result)
            driver.utilities.click_button(driver.app, checklocator, result + " (Recent check number)", waits_config['veryShortWait'])
        time.sleep(waits_config['longWait'])
