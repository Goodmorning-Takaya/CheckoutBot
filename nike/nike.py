import nike.constants as const

from selenium import webdriver

class Nike(webdriver.Safari):
    def __init__(self, config) -> None:
        super(Nike, self).__init__()

        self.username = config.get("NIKE_ACCOUNT", "USERNAME")
        self.password = config.get("NIKE_ACCOUNT", "PASSWORD")
        self.ID = config.get("NIKE_ACCOUNT", "ID")
        self.card = config.get("CREDIT_CARD", "CCNUM")
        self.ccsecurity = config.get("CREDIT_CARD", "CCV")
        self.expiration_month = config.get("CREDIT_CARD", "EXPM")
        self.expiration_year = config.get("CREDIT_CARD", "EXPY")

    def land_item_page(self) -> None:
        self.get(const.ITEM_URL)

    def login(self) -> None:
        signButtonElement = self.find_element(By.CLASS_NAME, const.SIGN_BUTTON_CLASS)
        loginButtonElement = self.find_element(By.ID, const.LOGIN_BUTTON_ID)
        passwordButtonElement = self.find_element(By.ID, const.PASSWORD_BUTTON_ID)

        action = ActionChains(super())
        action.move_to_element(signButtonElement)
        action.click(signButtonElement)
        action.move_to_element(loginButtonElement)
        action.click(loginButtonElement)
        action.send_keys(self.username)
        action.move_to_element(passwordButtonElement)
        action.click(passwordButtonElement)
        action.send_keys(self.password)
        action.perform()
     