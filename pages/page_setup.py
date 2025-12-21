from pages.loginPage import loginPage


class Pages:
    def __init__(self, page):
        # Page objects
        self.login = loginPage(page)
        

def init_pages(page):
    return Pages(page)

