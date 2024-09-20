from abc import ABC, abstractmethod


class ApplicationDriver(ABC):
    """
    Abstract base class for application drivers.
    This class defines the common interface that all specific application drivers must implement.
    """
    @abstractmethod
    def launch_application(self, app_path):
        """
        Launches the application.
            :param app_path : The file path to the application to be launched.
        """
        pass

    @abstractmethod
    def close_application(self):
        """
        Closes the application.
        """
        pass
