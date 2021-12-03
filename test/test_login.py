from pom.login import Login


def test_valid_username_password(driver):
    login = Login(driver)
    login.login_with_credentials(username="john@gmail.com", password="test1234")


def test_blank_username(driver):
    login = Login(driver)
    login.login_with_credentials("", "test1234")


def test_blank_password(driver):
    login = Login(driver)
    login.login_with_credentials("dan@gmail.com", "")


def test_blank_username_password(driver):
    login = Login(driver)
    login.login_with_credentials("", "")


def test_invalid_username(driver):
    login = Login(driver)
    login.login_with_credentials("invalid-dan@gmail.com", "test1234")


def test_invalid_password(driver):
    login = Login(driver)
    login.login_with_credentials("dan@gmail.com", "invalid-test1234")


def test_invalid_username_password(driver):
    login = Login(driver)
    login.login_with_credentials("invalid-dan@gmail.com", "invalid-test1234")

