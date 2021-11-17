from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class NewYearPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6 > .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info > .alertinner > p > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6 > h1")
    PRODUCT_IN_BASKET = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
