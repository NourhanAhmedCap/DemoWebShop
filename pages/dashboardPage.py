from playwright.sync_api import Page, expect

class dashboardPage():
    #------locators----------------
    Apparel_Shoes ="a[href='/apparel-shoes']"
    
        

    def __init__(self, page: Page):
        self.page = page