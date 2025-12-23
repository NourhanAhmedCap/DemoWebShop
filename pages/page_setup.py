from pages.loginPage import loginPage
from methods.basicsMethods import basicsMethods
from methods.assertionsMethods import assertionsMethods
from pages.dashboardPage import dashboardPage
from pages.apparelshoesPage import apparelshoesPage
from pages.shoppingCartPage import shoppingCartPage

class Pages:
    def __init__(self, page):
        # Page objects
        self.login = loginPage(page)
        self.basics = basicsMethods(page)
        self.assertions = assertionsMethods(page)
        self.dashboard = dashboardPage(page)
        self.apparelshoes = apparelshoesPage(page)
        self.shoppingCart = shoppingCartPage(page)

        

def init_pages(page):
    return Pages(page)

