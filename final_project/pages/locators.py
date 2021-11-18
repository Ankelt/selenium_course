from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6 > .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info > .alertinner > p > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6 > h1")
    PRODUCT_IN_BASKET = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    SUCCESS_MESSAGE = (By.XPATH, ".alert-success> .alertinner")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "#content_inner .basket-title")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
