import configparser
import log_file

logging = log_file.get_logs()

class ConfigReader:
    """
    A utility class to read configuration settings from a config file.
    """
    def __init__(self, config_file='config.cfg'):
        """
        Initializes the ConfigReader with the provided config file.
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_framework_type(self):
        """
        Retrieves the framework type from the configuration.
            :return: The type of the framework.
        """
        try:
            framework_type = self.config.get('Framework', 'type')
            logging.info(f"Framework type retrieved: {framework_type}")
            return framework_type
        except configparser.NoSectionError as e:
            logging.error(f"Framework section missing in the config file: {str(e)}")
            raise
        except configparser.NoOptionError as e:
            logging.error(f"Type option missing in the Framework section: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Error retrieving framework type: {str(e)}")
            raise

    def get_winappdriver_config(self):
        """
        Retrieves the WinAppDriver configuration from the configuration file.
            :return: A dictionary containing WinAppDriver configuration.
        """
        try:
            winappdriver_config = {
                'path': self.config.get('WinAppDriver', 'path_to_winappdriver'),
                'application_path': self.config.get('WinAppDriver', 'application_path'),
                'url': self.config.get('WinAppDriver', 'url')
            }
            logging.info("WinAppDriver configuration retrieved successfully.")
            return winappdriver_config
        except configparser.NoSectionError as e:
            logging.error(f"WinAppDriver section missing in the config file: {str(e)}")
            raise
        except configparser.NoOptionError as e:
            logging.error(f"Required option missing in the WinAppDriver section: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Error retrieving WinAppDriver configuration: {str(e)}")
            raise

    def get_pywinauto_config(self):
        """
        Retrieves the Pywinauto configuration from the configuration file.
            :returns: A dictionary containing Pywinauto configuration.
        """
        try:
            pywinauto_config = {
                'application_path': self.config.get('Pywinauto', 'application_path'),
                'window_title': self.config.get('Pywinauto', 'window_title')
            }
            logging.info("Pywinauto configuration retrieved successfully.")
            return pywinauto_config
        except configparser.NoSectionError as e:
            logging.error(f"Pywinauto section missing in the config file: {str(e)}")
            raise
        except configparser.NoOptionError as e:
            logging.error(f"Required option missing in the Pywinauto section: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Error retrieving Pywinauto configuration: {str(e)}")
            raise

    def get_waits_config(self):
        """
        Retrieves the Wait configuration from the configuration file.
            :returns: A dictionary containing Wait configuration.
        """
        try:
            wait_config = {
                'veryShortWait': int(self.config.get('waits', 'veryShortWait')),
                'shortWait': int(self.config.get('waits', 'shortWait')),
                'longWait': int(self.config.get('waits', 'longWait')),
                'veryLongWait': int(self.config.get('waits', 'veryLongWait'))
            }
            logging.info("waits configuration retrieved successfully.")
            return wait_config
        except configparser.NoSectionError as e:
            logging.error(f"Waits section missing in the config file: {str(e)}")
            raise
        except configparser.NoOptionError as e:
            logging.error(f"Required option missing in the waits section: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Error retrieving waits configuration: {str(e)}")
            raise

    def get_QUPOS_config(self):
        """
        Retrieves the QuPOS configuration from the configuration file.
            :returns: A dictionary containing QuPOS configuration.
        """
        try:
            qu_config = {
                'employeeId': self.config.get('QuPOS', 'EmployeeId'),
                'breakfastButton' : self.config.get('QuPOS', "breakfast_button"),
                'lunchDinner_button': self.config.get('QuPOS', "lunchDinner_button"),
                'lunchItem': self.config.get('QuPOS', "lunchItem"),
                'combo': self.config.get('QuPOS', "combo"),
                'medium': self.config.get('QuPOS', "medium"),
                'sides': self.config.get('QuPOS', "sides"),
                'garlicFries': self.config.get('QuPOS', "garlicFries"),
                'drinks': self.config.get('QuPOS', "drinks"),
                'hotCoffee': self.config.get('QuPOS', "hotCoffee"),
                'kidsMeal': self.config.get('QuPOS', "kidsMeal"),
                'onionRings': self.config.get('QuPOS', "onionRings"),
                'mayo': self.config.get('QuPOS', "mayo"),
                'jalapenos': self.config.get('QuPOS', "jalapenos"),
                'logout_button': self.config.get('QuPOS', "logout_button"),
                'tillClaimedText': self.config.get('QuPOS', "tillClaimedText"),
                'tillDeviceSelectionText': self.config.get('QuPOS', "tillDeviceSelectionText"),
                'entreeFromCart': self.config.get('QuPOS', "entreeFromCart"),
                'discountPriceForOnionRings': float(self.config.get('QuPOS', "discountPriceForOnionRings"))
            }
            logging.info("QU POS configuration retrieved successfully.")
            return qu_config
        except configparser.NoSectionError as e:
            logging.error(f"QU POS section missing in the config file: {str(e)}")
            raise
        except configparser.NoOptionError as e:
            logging.error(f"QU POS option missing in the Pywinauto section: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Error retrieving QU POS configuration: {str(e)}")
            raise


config = ConfigReader()
