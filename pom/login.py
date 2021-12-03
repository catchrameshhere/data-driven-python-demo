from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver

    """locators"""
    email = "//input[@id='email']"
    passwd = "pass"

    def login_with_credentials(self, username, password):
        print("username = {}, password = {}".format(username, password))
        self.driver.find_element(By.XPATH, self.email).clear()
        self.driver.find_element(By.XPATH, self.email).send_keys(username)
        self.driver.find_element(By.ID, self.passwd).clear()
        self.driver.find_element(By.ID, self.passwd).send_keys(password)
        # click submit button
