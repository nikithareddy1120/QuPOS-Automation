import time
from core_layer.utility.assertions import Assertions
from config.config_reader import config
from core_layer.driver_manager.driver_factory import DriverFactory
import log_file
from core_layer.utility.yamlManager import YamlUtilities

logging = log_file.get_logs()
framework_type = config.get_framework_type()
driver = DriverFactory.create_driver(framework_type)
qu_config = config.get_QUPOS_config()
waits_config = config.get_waits_config()
prices= []

class orderWindow:
    def __init__(self):
        self.assertion = Assertions(driver)
        self.yamlmanager = YamlUtilities()

    HAMBURGERMENU = {"auto_id":"RegisterPage_AppBar_Show_Button"}
    CLAIMCLOSETILL = {"title":"Claim/Close Till"}
    RECONCILE = {"title":"Reconcile"}
    CLAIM = {"title":"Claim"}
    CURRENTCASH = {"title":"Current cash"}
    CLOSE = {"title":"", "auto_id":"TillDeviceSelectionView_Close_Button"}
    DINETHRU_DROPDOWN = {"auto_id":"ComboBox_CheckTypeSelector"}
    DINEIN = {"title":"DineIn", "control_type":"ListItem"}
    KIDSCHZBURGERMEAL = {"title":"KID'S CHZBURGER MEAL"}
    REMOVEDEFAULTMODIFIER = {"auto_id": "DecrementQty_47587-47958-48038-56642-56645"}
    VERIFYREMOVEDMODIFIER = {"auto_id": "CheckItemDetail_Item-0-47587-47958-48038"}
    QUICKSUSPEND = {"title":"Quick Suspend", "auto_id":"RegisterPage_SuspendCheck2", "control_type":"Button"}
    CHECKNUMBER = {"auto_id":"CheckNumberAndTimeTextBlock"}
    SHOWOPENCHECKS = {"title":"Show Open Checks"}
    SUBTOTAL = {"title":"Subtotal", "control_type":"Text"}
    TOTALAMOUNT = {"auto_id":"CheckView_Total_TextBlock"}
    TAX = {"auto_id":"CheckView_Tax_Value"}
    AUTOIDOFSUPREMECROISSANT = "47587-47958-48038"
    GETPRICEOFSUPREMECROISSANT = {"title":"#21 SUPREME CROISSANT ", "control_type":"Text"}
    AUTOIDOFMEDIUMCOMBO = "47587-56634-56775"
    GETPRICEOFMEDIUMCOMBO = {"title":"Medium", "control_type":"Text"}
    AUTOIDOFKIDSCHZBURGERMEAL = "47587-47893-47957"
    GETPRICEOFKIDSGRILLEDCHEESEMEAL = {"title": "KID'S GRILLED CHEESE MEAL", "auto_id": "MenuItemTitleTextBlock", "control_type": "Text"}
    GETPRICEOFONIONRINGS = {"title":"ONION RINGS", "control_type":"Text"}
    GETPRICEOFJALAPENOS = {"title":"JALAPENOS", "control_type":"Text"}
    AUTOIDOFONIONRINGS = "47587-47893-47957-49677-47705"
    AUTOIDOFJALAPENOS = "47587-47958-48038-56286-47810"
    SUPREMECROISSANT = {"title":"#21 SUPREME CROISSANT "}
    NOCHECKTEXT = {"title" : "No\nCheck", "auto_id" : "CheckView_NoCheck_Text", "control_type" : "Text"}
    SEARCHCLOSEDCHECKS = {"title":"Search Closed Checks"}

    def clickHamburgerMenu(self):
        time.sleep(waits_config['shortWait'])
        driver.utilities.click_button(driver.app, self.HAMBURGERMENU, "Hamburger Menu", waits_config['veryShortWait'])

    def verifyNavigationMenu(self):
        driver.utilities.is_element_displayed(driver.app, self.CLAIMCLOSETILL, "Claim/Close Till button", waits_config['veryShortWait'])   #close/claim till
        driver.utilities.is_element_displayed(driver.app, self.SHOWOPENCHECKS, "Show Open Checks button", waits_config['veryShortWait'])   #show open checks

    def clickClaimCloseTillOption(self):
        driver.utilities.click_button(driver.app, self.CLAIMCLOSETILL, "Show Open Checks button", waits_config['veryShortWait']) #close/claim till
        time.sleep(waits_config['shortWait'])

    def verifyTillDeviceSelectionPopup(self):
        tillDeviceSelectionText = driver.utilities.get_locator_by_title(qu_config['tillDeviceSelectionText'])
        driver.utilities.is_element_displayed(driver.app, tillDeviceSelectionText, "Till Device Selection popup", waits_config['veryShortWait']) #tilldeviceselection

    def selectAvailableTill(self):
        tillAvailability = driver.utilities.waitUntilVisible(driver.app, self.RECONCILE, waits_config['veryShortWait'])
        if tillAvailability:
            logging.info("Till already claimed!")
            self.verifyCurrentCash()
        else:
            driver.utilities.click_button(driver.app, self.CLAIM, "Claim button", waits_config['veryShortWait'])
            self.verfiyTillText()
            self.verifyCurrentCash()

    def verfiyTillText(self):
        tillClaimedText = driver.utilities.get_locator_by_title(qu_config['tillClaimedText'])
        driver.utilities.is_element_displayed(driver.app, tillClaimedText, "Till, Successfully Claimed! text", waits_config['veryShortWait'])  #cliamed

    def verifyCurrentCash(self):
        driver.utilities.is_element_displayed(driver.app, self.CURRENTCASH, "Current cash", waits_config['veryShortWait']) #current cash

    def closeTillPopup(self):
        driver.utilities.click_button(driver.app, self.CLOSE, "Close button", waits_config['veryShortWait'])

    def selectDineInFromDropDrown(self):
        driver.utilities.click_button(driver.app, self.DINETHRU_DROPDOWN, "DineThru dropdown", waits_config['veryShortWait'])
        driver.utilities.click_button(driver.app, self.DINEIN, "DineIn option from dropdown", waits_config['veryShortWait'])

    def verifyDineInOption(self):
        driver.utilities.is_element_displayed(driver.app, self.DINEIN, "DineIn option", waits_config['shortWait'])

    def selectbreakfastItem(self):
        time.sleep(waits_config['veryLongWait'])
        breakfastButton = driver.utilities.get_locator_by_title(qu_config['breakfastButton'])
        driver.utilities.click_button(driver.app, breakfastButton, "Breakfast", waits_config['veryShortWait'])    #breakfast
        supremecroissant = driver.utilities.get_item_price(driver.app, self.AUTOIDOFSUPREMECROISSANT, self.GETPRICEOFSUPREMECROISSANT, "Price of SUPREME CROISSANT", waits_config['veryShortWait'])
        prices.append(supremecroissant)
        driver.utilities.click_button(driver.app, self.SUPREMECROISSANT, "SUPREME CROISSANT", waits_config['shortWait'])    #supreme corrisant

    def selectLunchItem(self):
        lunchDinner_button = driver.utilities.get_locator_by_title(qu_config['lunchDinner_button'])
        driver.utilities.click_button(driver.app, lunchDinner_button, "Lunch/Dinner", waits_config['veryShortWait'])    #Lunch/Dinner
        time.sleep(waits_config['shortWait'])
        lunchItem = driver.utilities.get_locator_by_title(qu_config['lunchItem'])
        driver.utilities.click_button(driver.app, lunchItem, "BACON ULTIMATE CHBURGER", waits_config['veryShortWait'])    #Spicy chicken
        Medium = driver.utilities.get_item_price(driver.app, self.AUTOIDOFMEDIUMCOMBO, self.GETPRICEOFMEDIUMCOMBO, "Price of Medium combo", waits_config['shortWait'])
        prices.append(Medium)
        medium = driver.utilities.get_locator_by_title(qu_config['medium'])
        driver.utilities.click_button(driver.app, medium, "Medium", waits_config['veryShortWait'])
        sides = driver.utilities.get_locator_by_title(qu_config['sides'])
        driver.utilities.click_button(driver.app, sides, "SIDES", waits_config['veryShortWait'])   # slides
        garlicFries = driver.utilities.get_locator_by_title(qu_config['garlicFries'])
        driver.utilities.click_button(driver.app, garlicFries, "GARLIC FRIES", waits_config['veryShortWait'])   #garlic fries
        drinks = driver.utilities.get_locator_by_title(qu_config['drinks'])
        driver.utilities.click_button(driver.app, drinks, "DRINKS", waits_config['veryShortWait'])   #drinks
        hotCoffee = driver.utilities.get_locator_by_title(qu_config['hotCoffee'])
        driver.utilities.click_button(driver.app, hotCoffee, "HOT COFFEE", waits_config['veryShortWait'])   #hot coffee

    def selectKidsMeals(self):
        kidsMeal = driver.utilities.get_locator_by_title(qu_config['kidsMeal'])
        driver.utilities.click_button(driver.app, kidsMeal, "Kid's Meals", waits_config['veryShortWait'])  #kids meals
        time.sleep(waits_config['shortWait'])
        kidsChzBurgerMeal = driver.utilities.get_item_price(driver.app, self.AUTOIDOFKIDSCHZBURGERMEAL, self.GETPRICEOFKIDSGRILLEDCHEESEMEAL, "Price of KIDS GRILLED CHEESE MEAL", waits_config['veryShortWait'])
        logging.info(f"Price of kid's Cheese Burger Meal: {kidsChzBurgerMeal}")
        prices.append(kidsChzBurgerMeal)
        driver.utilities.click_button(driver.app, self.KIDSCHZBURGERMEAL, "KIDS GRILLED CHEESE MEAL", waits_config['veryShortWait'])  #kids grilled cheese meal
        sides = driver.utilities.get_locator_by_title(qu_config['sides'])
        driver.utilities.click_button(driver.app, sides, "SIDES", waits_config['veryShortWait'])  #sides
        priceOfonionRings = driver.utilities.get_item_price(driver.app, self.AUTOIDOFONIONRINGS, self.GETPRICEOFONIONRINGS, "Price of ONION RINGS", waits_config['veryShortWait'])
        prices.append(priceOfonionRings)
        onionRings = driver.utilities.get_locator_by_title(qu_config['onionRings'])
        driver.utilities.click_button(driver.app, onionRings, "ONION RINGS", waits_config['veryShortWait'])  #onion rings

    def selectEntreeInTheCart(self):
        entreeFromCart = driver.utilities.get_locator_by_title(qu_config['entreeFromCart'])
        driver.utilities.click_button(driver.app, entreeFromCart, "SUPREME CROISSANT from cart", waits_config['veryShortWait'])

    def verifySelectedEntreeIsDisplayed(self):
        entreeFromCart = driver.utilities.get_locator_by_title(qu_config['entreeFromCart'])
        driver.utilities.click_button(driver.app, entreeFromCart, "SUPREME CROISSANT from cart", waits_config['veryShortWait'])

    def removeDefaultModifiers(self):
        driver.utilities.click_button(driver.app, self.REMOVEDEFAULTMODIFIER, "'-' button of HAM", waits_config['veryShortWait'])  #

    def addFreeModifier(self):
        mayo = driver.utilities.get_locator_by_title(qu_config['mayo'])
        driver.utilities.click_button(driver.app, mayo, "'+' button of MAYO", waits_config['veryShortWait'])

    def addPricedModifier(self):
        jalapenos = driver.utilities.get_item_price(driver.app, self.AUTOIDOFJALAPENOS, self.GETPRICEOFJALAPENOS, "Price of JALAPENOS", waits_config['veryShortWait'])
        prices.append(jalapenos)
        jalapenos = driver.utilities.get_locator_by_title(qu_config['jalapenos'])
        driver.utilities.click_button(driver.app, jalapenos, "JALAPENOS", waits_config['veryShortWait'])

    def verfiyModifiers(self):
        text = driver.utilities.get_text(driver.app, self.VERIFYREMOVEDMODIFIER, "Modifier", waits_config['veryShortWait'])
        return text

    def verifyRemovedModifier(self):
        text = self.verfiyModifiers()
        self.assertion.assert_contains(text, "No HAM")

    def verifyFreeModifier(self):
        text = self.verfiyModifiers()
        self.assertion.assert_contains(text, "ADD MAYO")

    def verifyPricedModifier(self):
        text = self.verfiyModifiers()
        self.assertion.assert_contains(text, "ADD JALAPENOS @ 0.40")
        subtotal = driver.utilities.get_item_price_without_autoid(driver.app, self.SUBTOTAL, "Subtotal Amount", waits_config['veryShortWait'])
        self.assertion.assert_equal(round(sum(prices), 2), subtotal)

    def clickQuickSuspend(self):
        number = driver.utilities.get_text(driver.app, self.CHECKNUMBER, "Check Number", waits_config['veryShortWait'])  # Retrieve the number and store it
        driver.utilities.click_button(driver.app, self.QUICKSUSPEND, "Quick Suspend", waits_config['veryShortWait'])
        time.sleep(waits_config['longWait'])
        logging.info(f"Check number: {number}")
        self.yamlmanager.write_to_yaml_file(yaml_data = {'checknumber': number})

    def verifyLogoutButton(self):
        logout_button = driver.utilities.get_locator_by_title(qu_config['logout_button'])
        driver.utilities.is_element_displayed(driver.app, logout_button, "Logout button", waits_config['veryShortWait'])

    def clickLogoutButton(self):
        logout_button = driver.utilities.get_locator_by_title(qu_config['logout_button'])
        driver.utilities.click_button(driver.app, logout_button, "Logout button", waits_config['veryShortWait'])

    def closeApplication(self):
        driver.close_application()

    def clickShowOpenChecks(self):
        driver.utilities.click_button(driver.app, self.SHOWOPENCHECKS, "Show Open Checks button", waits_config['veryShortWait'])
        time.sleep(waits_config['veryLongWait'])

    def verifyTotalPriceOfItems(self):
        time.sleep(waits_config['shortWait'])
        subtotal = driver.utilities.get_item_price_without_autoid(driver.app, self.SUBTOTAL, "Subtotal Amount", waits_config['shortWait'])
        self.assertion.assert_equal(round(sum(prices), 2), subtotal)
        tax = driver.utilities.get_text(driver.app, self.TAX, "Tax", waits_config['veryShortWait'])
        total = []
        total.append(tax)
        totalAmount = driver.utilities.get_text(driver.app, self.TOTALAMOUNT, "Total Amount ", waits_config['veryShortWait'])
        total.append(prices)
        calculated_total = sum(prices) + float(tax)
        self.assertion.assert_equal(float(totalAmount.replace('$', '')), round(calculated_total, 2))
        return float(totalAmount.replace('$', ''))

    def verifyWindowAfterPayment(self):
        time.sleep(waits_config['shortWait'])
        driver.utilities.is_element_displayed(driver.app, self.NOCHECKTEXT, "No Checks", waits_config['veryShortWait'])
        total = driver.utilities.get_text(driver.app, self.TOTALAMOUNT, "Total Amount", waits_config['veryShortWait'])
        if float(total.replace('$', '')) == 0.00:
            logging.info("Payment was successful")
        else:
            logging.error("Payment was not successful")

    def clickSearchClosedChecks(self):
        driver.utilities.click_button(driver.app, self.SEARCHCLOSEDCHECKS, "Search Closed Checks", waits_config['veryShortWait'])
        time.sleep(waits_config['veryShortWait'])
