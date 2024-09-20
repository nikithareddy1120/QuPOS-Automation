import subprocess
import time

from pywinauto.application import Application
from core_layer.utility.pywinauto_utilities import PywinautoUtilities
from core_layer.driver_manager.application_driver import ApplicationDriver
from abc import ABCMeta
import log_file
from config.config_reader import config

logging = log_file.get_logs()
pywinauto_config = config.get_pywinauto_config()


class Singleton(type):
    """
    Singleton class to ensure that only one instance of a class is created.
    This pattern is useful for creating a single instance of the driver.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonABCMeta(Singleton, ABCMeta):
    """
    A metaclass combining Singleton and ABCMeta, ensuring that subclasses of this class
    follow both the Singleton and Abstract Base Class (ABC) design patterns.
    """
    pass


class PywinautoDriver(ApplicationDriver, metaclass=SingletonABCMeta):
    """
    PywinautoDriver class responsible for launching and closing applications using Pywinauto.
    Implements the ApplicationDriver interface and uses the Singleton pattern to ensure a single instance.
    """
    def __init__(self):
        """
        Initializes the PywinautoDriver class with an application instance and utilities.
       """
        self.app = None
        self.utilities = PywinautoUtilities()

    def launch_application(self, app_path):
        """
        Launches the application using the provided path and attempts to connect using the window title.
        Falls back to connecting using the process ID if the title method fails.
            :param app_path : The file path to the application to be launched.
            :param window_title : The expected window title of the application.
            :return : An instance of the launched application.
        """
        try:
            logging.info("Trying to launch application using subprocess")
            proc = subprocess.Popen('start shell:AppsFolder\\QuBeyondPOS_3x5bkgewp3n9r!App', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(3)
            # application = Application(backend='uia').connect(title="Qu")
            proc.communicate()
            logging.info(proc.pid)
            logging.info("Application launched successfully with window title")
            desktop = Application(backend="uia")
            logging.info("backend")
            self.app = desktop.connect(title=pywinauto_config['window_title'])
            # logging.info("connected to app")
        except Exception as e:
            logging.warning(f"Failed to launch application using window title: {e}. Trying process ID method.")
            try:
                self.app = Application(backend='uia').start("start shell:AppsFolder\\QuBeyondPOS_3x5bkgewp3n9r!App")
                # Get the process ID of the started application
                pid = self.app.process
                # Wait for the initial window to appear
                time.sleep(2)
                # Connect to the application using the process ID
                self.app = Application(backend='uia').connect(process=pid)
                logging.info("Application launched successfully with process ID")
            except Exception as e:
                logging.error(f"Failed to launch application using both methods: {e}")
                raise

        return self.app

    def close_application(self):
        """
        Closes the launched application if it is running.
        """
        try:
            if self.app:
                logging.info("Closing application")
                self.app.kill()
                logging.info("Application closed successfully")
            else:
                logging.warning("No application instance to close")
        except Exception as e:
            logging.error(f"Failed to close application with Pywinauto: {e}")
            raise
