from core_layer.driver_manager.pywinauto_driver import PywinautoDriver
from core_layer.driver_manager.winappdriver_driver import WinAppDriver
import log_file

logging = log_file.get_logs()

class DriverFactory:
    """
    Factory class to create and return the appropriate driver instance based on the framework type.
    """
    @staticmethod
    def create_driver(framework_type):
        """
        Creates a driver instance based on the provided framework type.
            :param framework_type : The type of the framework ('pywinauto' or 'winappdriver').
            :return : ApplicationDriver - An instance of the appropriate driver class.
                """
        try:
            logging.info(f"Creating driver for framework: {framework_type}")
            if framework_type == 'pywinauto':
                return PywinautoDriver()
            elif framework_type == 'winappdriver':
                return WinAppDriver()
            else:
                logging.error(f"Unknown framework type: {framework_type}")
                raise ValueError(f"Unknown framework type: {framework_type}")
        except ValueError as ve:
            logging.error(f"Driver creation failed due to an invalid framework type: {ve}")
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred while creating the driver: {e}")
            raise
