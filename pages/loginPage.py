from playwright.sync_api import Page, expect

class loginPage():
     # -------- locators --------
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = ".gico-login"
    Register = ".ico-register"


    def __init__(self, page: Page):
       self.page = page

    def open(self, base_url: str,):        
        self.page.goto(base_url)
        expect(self.page.locator(".header-logo")).to_be_attached()

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def get_error(self):
        return self.page.text_content(self.ERROR_MESSAGE)
