import io
import sys
import time
from pywinauto.timings import wait_until_passes
import log_file
from config.config_reader import config


logging = log_file.get_logs()
pywinauto_config = config.get_pywinauto_config()


class PywinautoUtilities:

    def maximizeWindow(self, app):
        """
        This method maximizes the application.
            :param app : pywinauto Application instance.
            :param window_title : title of the window
        """
        try:
            window = app[pywinauto_config["window_title"]]
            window.maximize()
            logging.info(f"Maximized the application window.")
        except Exception as e:
            logging.error(f"Failed to maximize window: {e}")

    def minimizeWindow(self, app):
        """
        This method minimizes the application.
            :param app : pywinauto Application instance.
            :param window_title : title of the window.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            window.minimize()
            logging.info(f"Minimized the application window.")
        except Exception as e:
            logging.error(f"Failed to minimize window: {e}")

    def click_button(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method will click on the locator
            :param app : pywinauto Application instance.
            :param window_title : title of the window.
            :param control_identifier : element locator
            :param timeout : time to wait for element to be visible
        """
        try:
            time.sleep(timeout)
            window = app[pywinauto_config['window_title']]
            control = window.child_window(**control_identifier).wrapper_object()
            control.click_input()
            logging.info(f"Clicked on {friendlyNameOfElement}")
        except Exception as e:
            logging.error(f"Unable to click on {friendlyNameOfElement} in {timeout}: {e}")

    def enter_text(self, app, control_identifier, text, friendlyNameOfElement, timeout):
        """
        This method will enter the text in the locator
            :param app : pywinauto Application instance.
            :param window_title : title of the window.
            :param control_identifier : element locator
            :param text : text to enter in input field
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            time.sleep(timeout)
            control.set_edit_text(text)
            logging.info(f"Entered {text} into {friendlyNameOfElement}")
        except Exception as e:
            logging.error(f"Could not {text} into {friendlyNameOfElement}: {e}")

    def get_text(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method will get the text from the locator
            :param app : pywinauto Application instance.
            :param window_title : title of the window.
            :param control_identifier : element locator
            :param timeout : time to wait for element to be visible
            :return : return the text from the locator
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            time.sleep(timeout)
            text = control.window_text()
            logging.info(f"Text from {friendlyNameOfElement} is {text}")
            return text
        except Exception as e:
            logging.error(f"Unable to fetch the text from the {friendlyNameOfElement}: {e}")
            return None

    def is_element_displayed(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method will wait for an element to be displayed.
            :param app : pywinauto Application instance.
            :param window_title : title of the window.
            :param control_identifier : element locator
            :param timeout : time to wait for element to be displayed
        """
        try:
            window = app[pywinauto_config['window_title']]
            control = window.child_window(**control_identifier).wrapper_object()
            time.sleep(timeout)
            control.is_visible()
            logging.info(f"{friendlyNameOfElement} is displayed")
        except Exception as e:
            logging.error(f"{friendlyNameOfElement} not found: {e}")

    def waitUntilVisible(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method will wait for an element to be displayed.
            :param app : pywinauto Application instance.
            :param window_title : title of the window.
            :param control_identifier : element locator
            :param timeout : time to wait for element to be displayed
        """
        try:
            window = app[pywinauto_config['window_title']]
            control = window.child_window(**control_identifier).wrapper_object()
            time.sleep(timeout)
            control.is_visible()
            logging.info(f"{friendlyNameOfElement} is displayed")
            return control
        except Exception as e:
            logging.info(f"{friendlyNameOfElement} not found")

    def is_element_selected(self, app, control_identifier, timeout):
        """
        This method will wait for an element to be selected.
            :param app : pywinauto Application instance.
            :param window_title : title of the window.
            :param control_identifier : element locator
            :param timeout : time to wait for element to be displayed
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            time.sleep(timeout)
            control.is_selected()
            logging.info(f"{control_identifier} is selected")
        except Exception as e:
            logging.error(f"{control_identifier} is not selected in {timeout}: {e}")

    def is_element_enabled(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method will wait for an element to be enabled.
            :param app : pywinauto Application instance.
            :param window_title : title of the window.
            :param control_identifier : element locator
            :param timeout : time to wait for element to be enabled
        """
        flag = False
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            time.sleep(timeout)
            flag = control.is_enabled()
            logging.info(f"{friendlyNameOfElement} is enabled")
            return flag
        except Exception as e:
            logging.error(f"{friendlyNameOfElement} not enabled: {e}")
            return flag

    def clear_text(self, app, control_identifier, timeout):
        """
        This method will clear the text from the element
            :param app : pywinauto Application instance.
            :param window_title : title of the window.
            :param control_identifier : element locator
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            time.sleep(timeout)
            control.set_focus()
            control.send_keys('^a')
            control.send_keys('{DELETE}')
            logging.info(f"Cleared the text from {control_identifier}")
        except Exception as e:
            logging.error(f"Unable to clear the text from {control_identifier}: {e}")

    def double_click(self, app, control_identifier, timeout):
        """
        This method double-clicks on the element.
            :param app : pywinauto Application instance.
            :param window_title : title of the window.
            :param control_identifier : element locator
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            time.sleep(timeout)
            control.double_click_input()
            logging.info(f"Double clicked on the element with locator: {control_identifier}")
        except Exception as e:
            logging.error(f"Unable to double click on the element with locator {control_identifier}: {e}")
            raise

    def drag_and_drop(self, app, source_control_identifier, destination_control_identifier, timeout):
        """
        This method performs the drag and drop operation
            :param app: pywinauto Application instance.
            :param window_title: title of the window.
            :param source_control_identifier: Element locator to start dragging from.
            :param destination_control_identifier: Element locator to drop to.
            :param timeout: Time to wait for the elements to be visible.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            source_control = window.child_window(**source_control_identifier).wrapper_object()
            target_control = window.child_window(**destination_control_identifier).wrapper_object()
            time.sleep(timeout)
            source_control.drag_mouse_input()
            target_control.drop_mouse_input()
            logging.info(f"Performed drag-and-drop from {source_control_identifier} to {destination_control_identifier}")
        except Exception as e:
            logging.error(
                f"Unable to perform drag-and-drop from {source_control_identifier} to {destination_control_identifier}: {e}")
            raise

    def get_status_of_button(self, app, control_identifier, timeout):
        """
        This method will get the status of a button in the Application.
            :param app : pywinauto Application instance.
            :param window_title : title of the window.
            :param control_identifier : element locator
            :param timeout : time to wait for element to be visible
        """
        try:
            flag = False
            main_dlg = app[pywinauto_config["window_title"]]
            button = main_dlg.child_window(**control_identifier, top_level_only=True)
            time.sleep(timeout)
            if button and button.is_visible() and button.is_enabled():
                logging.info(f"'{control_identifier}' field is visible and enabled")
                flag = True
            else:
                logging.error(f"'{control_identifier}' field is not visible or not enabled.")
                flag = False
        except Exception as err:
            logging.error(f"Exception occurred: {err}")
            flag = False
        return flag

    def mouse_hover(self, app, control_identifier, timeout):
        """
        This method will perform a mouse hover action on the specified element.
            :param app: pywinauto Application instance.
            :param window_title: title of the window.
            :param control_identifier: element locator
            :param timeout: time to wait for element to be visible.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            element = window.child_window(**control_identifier).wrapper_object
            element.wait('visible', timeout=timeout)
            element.wait('enabled', timeout=timeout)
            element.move_mouse_input()
            # rect = element.rectangle()
            # mouse.move(coords=(rect.left + 5, rect.top + 5))
            logging.info(f"Mouse hover action performed on the element {control_identifier}.")
        except Exception as e:
            logging.error(f"Unable to perform mouse hover action on the element {control_identifier}: {e}")
            raise

    def close_window(self, app):
        """
         This method closes the application.
            :param app : pywinauto Application instance.
            :param window_title : title of the window
         """
        try:
            window = app[pywinauto_config["window_title"]]
            window.close()
            logging.info(f"Closed the application window.")
        except Exception as e:
            logging.error(f"Failed to close window: {e}")

    def restore_window(self, app):
        """
        This method restores the application window.
            :param app : pywinauto Application instance.
            :param window_title : title of the window
        """
        try:
            window = app[pywinauto_config["window_title"]]
            window.restore()
            logging.info(f"Restored the application window.")
        except Exception as e:
            logging.error(f"Failed to restore window: {e}")

    def is_window_active(self, app):
        """
        This method checks if the specified application window is active.
            :param app: pywinauto Application instance.
            :param window_title: title of the window.
            :return: Boolean indicating whether the window is active.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            active = window.is_active()
            if active:
                logging.info(f"The window '{pywinauto_config['window_title']}' is active.")
            else:
                logging.info(f"The window '{pywinauto_config['window_title']}' is not active.")
            return active
        except Exception as e:
            logging.error(f"Failed to check if window '{pywinauto_config['window_title']}' is active: {e}")
            return False

    def getWindowState(self, app):
        """
        This method will return the current state of the application .
            :param app : pywinauto Application instance.
            :param window_title : title of the window
            :return : returns the current state of the window
        """
        try:
            window = app[pywinauto_config["window_title"]]
            windowState = window.get_show_state()
            logging.info(f"Application window state : {windowState}.")
            return windowState
        except Exception as e:
            logging.error(f"Failed to return the application window state: {e}")

    def scroll_element(self, app, control_identifier, direction, amount, timeout):
        """
        This method will scroll the specified element in the given direction.
            :param app: pywinauto Application instance.
            :param window_title: title of the window.
            :param control_identifier: element locator
            :param direction: Direction to scroll ('up', 'down', 'left', 'right').
            :param amount: Amount to scroll ('large', 'small', 'page', 'begin', 'end').
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            element = window.child_window(**control_identifier).wrapper_object
            element.wait('visible', timeout)
            # element.wait('enabled', timeout)
            element.scroll(direction, amount)
            logging.info(f"Scrolled the element {control_identifier} {direction}.")
        except Exception as e:
            logging.error(f"Unable to scroll the element {control_identifier} {direction}: {e}")
            raise

    def scrollUtilVisible(self, app, control_identifier,timeout):
        try:
            def is_control_visible():
                window = app[pywinauto_config["window_title"]]
                element = window.child_window(**control_identifier).wrapper_object
                # control = window.child_window(**{key: value})
                if element.exists() and control.is_visible():
                    return control
                else:
                    # Try scrolling the window or control to make the element visible
                    try:
                        window.scroll("down")
                        logging.info("scrolled the window")
                    except AttributeError:
                        pass  # Window or control doesn't support scrolling
                    return False

            # Wait until the element is visible or timeout occurs
            control = wait_until_passes(timeout, 1, is_control_visible)
            return control
        except Exception as e:
            return None

    def right_click(self, app, control_identifier, timeout):
        """
        This method right-clicks on the element.
            :param app : pywinauto Application instance.
            :param window_title : title of the window.
            :param control_identifier : element locator
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier).wrapper_object()
            time.sleep(timeout)
            control.right_click_input()
            logging.info(f"Right clicked on the element with locator: {control_identifier}")
        except Exception as e:
            logging.error(f"Unable to right click on the element with locator {control_identifier}: {e}")
            raise

    def send_keyboard_shortcut_to_element(self, app, control_identifier, shortcut, timeout):
        """
        This method sends a keyboard shortcut to a specified element.
            :param app: pywinauto Application instance.
            :param window_title: title of the window.
            :param control_identifier: element locator
            :param shortcut: String representing the keyboard shortcut (e.g., '^s' for Ctrl+S).
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            element = window.child_window(**control_identifier).wrapper_object
            element.wait('ready', timeout)
            element.set_focus()
            element.send_keys(shortcut)
            logging.info(
                f"Sent keyboard shortcut '{shortcut}' to the element '{control_identifier}'.")
        except Exception as e:
            logging.error(
                f"Unable to send keyboard shortcut '{shortcut}' to the element '{control_identifier}': {e}")
            raise

    def set_focus_to_element(self, app, control_identifier, timeout):
        """
        This method sets focus to a specified element.
            :param app: pywinauto Application instance.
            :param window_title: title of the window.
            :param control_identifier: element locator
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            element = window.child_window(**control_identifier).wrapper_object
            element.wait('ready', timeout)
            element.set_focus()
            logging.info(f"Set focus to the element '{control_identifier}'.")
        except Exception as e:
            logging.error(
                f"Unable to set focus to the element '{control_identifier}': {e}")
            raise

    def wait_for_window_to_be_idle(self, app, timeout):
        """
        This method waits for a window to be idle.
            :param app: pywinauto Application instance.
            :param window_title: title of the window
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            window.wait_for_idle(timeout=timeout)
            logging.info(f"Window '{pywinauto_config['window_title']}' is now idle.")
        except Exception as e:
            logging.error(f"Failed to wait for window '{pywinauto_config['window_title']}' to be idle: {e}")
            raise

    def wait_for_element(self, app, control_identifier, timeout):
        """
        This method waits for a specified element to appear.
            :param app: pywinauto Application instance.
            :param window_title: title of the window
            :param control_identifier: element locator.
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            element = window.child_window(**control_identifier).wrapper_object
            element.wait('exists ready', timeout=timeout)
            logging.info(f"Element {control_identifier} is now present.")
        except Exception as e:
            logging.error(f"Failed to wait for element {control_identifier}: {e}")
            raise

    def verify_element_text(self, app, control_identifier, expected_text, timeout):
        """
        This method verifies the text of a specified element.
            :param app: pywinauto Application instance.
            :param window_title: title of the window
            :param control_identifier: element locator.
            :param expected_text: Expected text to verify.
            :param timeout : time to wait for element to be visible
        """
        try:
            window = app[pywinauto_config["window_title"]]
            element = window.child_window(**control_identifier).wrapper_object()
            time.sleep(timeout)
            actual_text = element.window_text()
            assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
            logging.info(f"Element {control_identifier} text verified successfully.")
        except Exception as e:
            logging.error(f"Failed to verify text for element {control_identifier}: {e}")
            raise

    def check_element_existence(self, app, control_identifier, timeout):
        """
        This method checks whether a specified element exists.
            :param app: pywinauto Application instance.
            :param window_title: title of the window
            :param control_identifier: element locator.
            :param timeout : time to wait for element to be visible
            :return: Boolean indicating existence.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            element = window.child_window(**control_identifier)
            time.sleep(timeout)
            exists = element.exists()
            logging.info(f"Element {control_identifier} existence: {exists}")
            return exists
        except Exception as e:
            logging.error(f"Failed to check existence of element {control_identifier}: {e}")
            raise

    def print_control_identifiers(self, app):
        """
        This method will print all the control identifiers displayed on the window
            :param app : pywinauto Application instance.
            :param window_title : title of the window.
        """
        logging.info(f"Printing control identifiers for window: {pywinauto_config['window_title']}")
        try:
            window = app[pywinauto_config['window_title']]
            old_stdout = sys.stdout
            sys.stdout = io.StringIO()
            try:
                window.print_control_identifiers()
                control_identifiers = sys.stdout.getvalue()
            finally:
                sys.stdout = old_stdout
            return control_identifiers
        except Exception as e:
            logging.error(f"Error printing control identifiers for {pywinauto_config['window_title']}: {e}")
            return None

    def print_available_windows(self, app):
        """
        This method will print all the available windows
            :param app : pywinauto Application instance.
        """
        logging.info("Available windows:")
        for window in app.windows():
            logging.info(f"Window title: {window.window_text()}")

    def take_screenshot(self, app, save_path):
        """
        This method takes a screenshot of the application window.
            :param app: pywinauto Application instance.
            :param window_title: title of the window to capture.
            :param save_path: Path to save the screenshot.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            screenshot = window.capture_as_image()
            screenshot.save(save_path)
            logging.info(f"Screenshot saved to {save_path}")
        except Exception as e:
            logging.error(f"Failed to take screenshot: {e}")
            raise

    def get_toggle_state_of_checkbox(self, app, control_identifier, timeout):
        """
        This method retrieves the toggle state of a control (e.g., a checkbox or a toggle button).
            :param app: pywinauto Application instance.
            :param window_title: title of the window.
            :param control_identifier: element locator
            :param timeout: Time to wait for the element to be visible.
            :return: Toggle state (True if toggled on, False if toggled off, None if state cannot be determined).
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier)
            control.wait('exists', timeout)
            toggle_state = control.get_toggle_state()
            logging.info(f"Toggle state for {control_identifier} is {toggle_state}.")
            return toggle_state
        except Exception as e:
            logging.error(f"Failed to get toggle state for {control_identifier}: {e}")
            return None

    def is_element_editable(self, app, control_identifier, timeout):
        """
        This method checks if a specified control is editable.
            :param app: pywinauto Application instance.
            :param window_title: Title of the window.
            :param control_identifier: Dictionary with the control's identifier.
            :param timeout: Time to wait for the element to be visible.
            :return: Boolean indicating whether the control is editable.
        """
        try:
            window = app[pywinauto_config["window_title"]]
            control = window.child_window(**control_identifier)
            control.wait('exists', timeout)
            editable = control.is_editable()
            if editable:
                logging.info(f"The control {control_identifier} is editable.")
            else:
                logging.info(f"The control {control_identifier} is not editable.")
            return editable
        except Exception as e:
            logging.error(f"Failed to determine if the control {control_identifier} is editable: {e}")
            return False

    def get_item_price(self, app, button_auto_id, control_identifier, friendlyNameOfElement, timeout):
        window = app[pywinauto_config['window_title']]
        try:
            time.sleep(timeout)
            button_element = window.child_window(auto_id=button_auto_id, control_type="Button")
            item_static = button_element.child_window(**control_identifier)
            for child in button_element.children(control_type="Text"):
                if child.window_text().replace('.', '', 1).isdigit():
                    text = float(child.window_text())
                    logging.info(f"{friendlyNameOfElement}: {text}")
                    return float(child.window_text())
            logging.error(f"'{friendlyNameOfElement}' not found.")
            return None
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return None

    def calculateAmountAfterDiscount(self, actual_price, discount_percentage):
        # Calculate the discount amount
        discount_amount = (discount_percentage / 100) * actual_price
        # Calculate the selling price and round it to 2 decimal places
        selling_price = round(actual_price - discount_amount, 2)
        return selling_price

    def get_item_price_without_autoid(self, app, control_identifier, friendlyNameOfElement, timeout):
        window = app[pywinauto_config['window_title']]
        try:
            time.sleep(timeout)
            item_static = window.child_window(**control_identifier)
            # logging.info(item_static)
            if item_static.exists():
                # Find the parent of the item static text control
                parent = item_static.parent()
                # logging.info(parent)
                # Check if parent has children and search for the price
                for child in parent.children(control_type="Text"):
                    if child.window_text().replace('.', '', 1).isdigit():
                        text = child.window_text()
                        logging.info(f"'{friendlyNameOfElement} : {text}'")
                        return child.window_text()
                (logging.info(f"'{friendlyNameOfElement}' not found."))
                return None
            else:
                logging.info(f"Item '{friendlyNameOfElement}' not found.")
                return None
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return None

    def get_locator_by_title(self, title_value):
        return {"title": title_value}

    def get_button_locator_by_title(self, title_value):
        return {"title": title_value,  "control_type":"Button"}

    def get_static_text(self, app, control_identifier, friendlyNameOfElement, timeout):
        """
        This method retrieves the static text (e.g., '#4000') from a button element with a given auto_id and control_type.
        :param app: pywinauto Application instance
        :param auto_id: Automation ID of the button
        :param control_type: Control type (e.g., Button)
        :return: The static text under the button if found
        """
        try:
            time.sleep(timeout)
            window = app[pywinauto_config['window_title']]
            # Access the window
            # window = app.window(title="Your Window Title")  # Replace with actual window title

            # Find the button element by auto_id and control_type
            button = window.child_window(**control_identifier).wrapper_object()

            # Find the static text element under the button and retrieve the text
            static_text = button.child_window(control_type="Text").window_text()
            logging.info(f"Text from the {friendlyNameOfElement}: {static_text}")
            return static_text
        except Exception as e:
            print(f"Error occurred: {e}")
            return None

