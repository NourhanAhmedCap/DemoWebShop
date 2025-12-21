from pages.loginPage import loginPage
from methods.basicsMethods import basicsMethods
from methods.assertionsMethods import assertionsMethods


class Pages:
    def __init__(self, page):
        # Page objects
        self.login = loginPage(page)
        self.basics = basicsMethods(page)
        self.assertions = assertionsMethods(page)

        

def init_pages(page):
    return Pages(page)

