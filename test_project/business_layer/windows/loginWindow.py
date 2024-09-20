import time
from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
import log_file

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver = DriverFactory.create_driver(framework_type)
pywinauto_config = config.get_pywinauto_config()
waits_config = config.get_waits_config()
qu_config = config.get_QUPOS_config()

class loginWindow:

    LOGINBUTTON = {"title":"Log In"}
    CLOCKINBUTTON = {"auto_id":"btnClockIn", "control_type":"Button"}
    ADMINISTRATOR = {"title":"Administrator", "control_type":"ListItem"}
    CLOCKINLOGIN = {"title":"Clock In & Log In", "auto_id":"btnLoginWithJobTitle", "control_type":"Button"}

    def enterEmployeeID(self):
        for digit in qu_config["employeeId"]:
            button_locator = driver.utilities.get_button_locator_by_title(digit)
            driver.utilities.click_button(driver.app, button_locator, digit, waits_config['veryShortWait'])

    def launchApp(self):
        driver.launch_application(pywinauto_config["application_path"])
        time.sleep(5)
        # time.sleep(waits_config['veryVeryLongWait'])

    def verifyloginScreen(self):
        driver.utilities.is_element_displayed(driver.app, self.LOGINBUTTON, "Login button", waits_config['veryShortWait'])  #Login button
        driver.utilities.is_element_displayed(driver.app, self.CLOCKINBUTTON, "Clock In button", waits_config['veryShortWait'])

    def clickLoginButton(self):
        driver.utilities.click_button(driver.app, self.LOGINBUTTON, "Login button", waits_config['veryShortWait'])  # loginbutton
        if driver.utilities.waitUntilVisible(driver.app, self.ADMINISTRATOR, "Administrator button", waits_config['veryShortWait']):
            driver.utilities.click_button(driver.app, self.ADMINISTRATOR, "Administrator button", waits_config['veryShortWait'])
            driver.utilities.click_button(driver.app, self.CLOCKINLOGIN, "Clock In & Log In button", waits_config['veryShortWait'])
        else:
            logging.info("Application is already logged in as an Administrator.")
        time.sleep(waits_config['longWait'])

    def closeApplication(self):
        driver.close_application()
