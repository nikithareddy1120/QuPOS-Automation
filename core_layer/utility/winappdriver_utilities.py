import time
from selenium.webdriver import ActionChains
import log_file

logging = log_file.get_logs()

class WinAppDriverUtilities:

    def maximizeWindow(self, driver):
        """
        This method maximizes the application.
            :param driver : WinAppDriver WebDriver instance.
        """
        try:
            driver.maximize_window()
            logging.info("Maximized the application window.")
        except Exception as e:
            logging.error(f"Failed to maximize window: {e}")

    def minimizeWindow(self, driver):
        """
        This method minimizes the application.
            :param driver : WinAppDriver WebDriver instance.
        """
        try:
            driver.minimize_window()
            logging.info("Minimized the application window.")
        except Exception as e:
            logging.error(f"Failed to minimize window: {e}")

    def click_button(self, driver, locator, timeout):
        """
        This method will click on the locator
            :param driver : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param timeout : time to wait for element to be visible
        """
        key = list(locator.keys())[0]
        value = list(locator.values())[0]
        element = driver.find_element(key, value)
        time.sleep(timeout)
        try:
            element.click()
            time.sleep(timeout)
            logging.info(f"Clicked on {locator}")
        except Exception as e:
            logging.error(f"Unable to click on {locator} in {timeout}: {e}")

    def enter_text(self, driver, locator, timeout, text):
        """
        This method will enter the text in the locator
            :param driver : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param timeout : time to wait for element to be visible
            :param text : text to enter in input field
        """
        key = list(locator.keys())[0]
        value = list(locator.values())[0]
        element = driver.find_element(key, value)
        time.sleep(timeout)
        try:
            element.send_keys(text)
            time.sleep(timeout)
            logging.info(f"Entered {text} into {locator}")
        except Exception as e:
            logging.error(f"Could not enter {text} into {locator}: {e}")

    def get_text(self, driver, locator, timeout=10):
        """
        This method will get the text from the locator
            :param driver : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param timeout : time to wait for element to be visible
            :return : returns the text from the locator
        """
        key = list(locator.keys())[0]
        value = list(locator.values())[0]
        element = driver.find_element(key, value)
        time.sleep(timeout)
        try:
            textfromElement = element.text  # Corrected from element.text()
            time.sleep(timeout)
            logging.info(f"Text from the {locator} is {textfromElement}")
            return textfromElement
        except Exception as e:
            logging.error(f"Unable to fetch the text from the {locator}: {e}")

    def is_element_displayed(self, driver, locator, timeout=10):
        """
        This method will wait for an element to be displayed.
            :param driver : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param timeout : time to wait for element to be displayed
        """
        key = list(locator.keys())[0]
        value = list(locator.values())[0]
        element = driver.find_element(key, value)
        time.sleep(timeout)
        try:
            element.is_displayed()
            time.sleep(timeout)
            logging.info(f"{locator} is displayed")
        except Exception as e:
            logging.error(f"{locator} not found in {timeout}: {e}")

    def is_element_enabled(self, driver, locator, timeout):
        """
        This method will wait for an element to be enabled.
            :param driver : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param timeout : time to wait for element to be enabled
        """
        key = list(locator.keys())[0]
        value = list(locator.values())[0]
        element = driver.find_element(key, value)
        time.sleep(timeout)
        try:
            element.is_enabled()
            time.sleep(timeout)
            logging.info(f"{locator} is enabled")
        except Exception as e:
            logging.error(f"{locator} not found in {timeout}: {e}")

    def clear_text(self, driver, locator, timeout=10):
        """
        This method will clear the text from the element
            :param driver : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param timeout : time to wait for element to be visible
        """
        key = list(locator.keys())[0]
        value = list(locator.values())[0]
        element = driver.find_element(key, value)
        time.sleep(timeout)
        try:
            element.clear()
            time.sleep(timeout)
            logging.info(f"Cleared the text from {locator}")
        except Exception as e:
            logging.error(f"Unable to clear the text from {locator}: {e}")

    def double_click(self, driver, locator, timeout):
        """
        This method double-clicks on the element
            :param driver : WinAppDriver WebDriver instance.
            :param locator : Dictionary with locator type as key and value as locator value.
            :param timeout : time to wait for element to be visible
        """
        actions = ActionChains(driver)
        key = list(locator.keys())[0].upper()
        value = list(locator.values())[0]
        try:
            time.sleep(timeout)
            element = driver.find_element(key, value)
            actions.double_click(element).perform()
            logging.info(f"Double clicked on the element with locator: {locator}")
        except Exception as e:
            logging.error(f"Unable to double click on the element with locator {locator}: {e}")

    def drag_and_drop(self, driver,  source_locator, destination_locator, timeout):
        """
        This method performs the drag and drop operation
            :param driver : WinAppDriver WebDriver instance.
            :param source_locator : Dictionary with source_locator type as key and value as source_locator value.
            :param destination_locator : Dictionary with destination_locator type as key and value as destination_locator value.
            :param timeout : time to wait for element to be visible
        """
        try:
            # Extract keys and values from locators
            source_key = list(source_locator.keys())[0]
            source_value = list(source_locator.values())[0]
            destination_key = list(destination_locator.keys())[0]
            destination_value = list(destination_locator.values())[0]
            # Find elements
            source_element = driver.find_element(source_key, source_value)
            destination_element = driver.find_element(destination_key, destination_value)
            time.sleep(timeout)
            # Perform drag and drop
            actions = ActionChains(driver)
            actions.drag_and_drop(source_element, destination_element).perform()
            time.sleep(timeout)
            logging.info(f"Performed drag-and-drop from {source_locator} to {destination_locator}")
        except Exception as e:
            logging.error(f"Unable to perform drag-and-drop from {source_locator} to {destination_locator}: {e}")

    def get_status_of_button(self, driver, locator, timeout=10):
        """
        This method will get the status of a button in the Application.
        :param driver: WinAppDriver WebDriver instance.
        :param locator: Dictionary with locator type as key and value as locator value.
        :param timeout: time to wait for element to be visible.
        :return: Boolean indicating if the button is visible and enabled.
        """
        try:
            key = list(locator.keys())[0]
            value = list(locator.values())[0]
            element = driver.find_element(key, value)
            time.sleep(timeout)
            if element.is_displayed() and element.is_enabled():
                logging.info(f"'{locator}' field is visible and enabled")
                return True
            else:
                logging.error(f"'{locator}' field is not visible or not enabled.")
                return False
        except Exception as e:
            logging.error(f"Exception occurred: {e}")
            return False

    def mouse_hover(self, driver, locator, timeout=10):
        """
        This method will perform a mouse hover action on the specified element.
            :param driver: WinAppDriver WebDriver instance.
            :param locator: Dictionary with the locator type as key and the locator value as value.
            :param timeout: time to wait for the element to be visible.
        """
        try:
            key = list(locator.keys())[0]
            value = list(locator.values())[0]
            element = driver.find_element(key, value)
            time.sleep(timeout)
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            logging.info(f"Mouse hover action performed on the element {locator}.")
        except Exception as e:
            logging.error(f"Unable to perform mouse hover action on the element {locator}: {e}")
            raise

    @staticmethod
    def wait_for_time(wait_in_seconds):
        """
        This method waits for the mentioned time
            :param wait_in_seconds : time (in seconds)
        """
        logging.info(f"Waiting for {wait_in_seconds} seconds")
        time.sleep(wait_in_seconds)
