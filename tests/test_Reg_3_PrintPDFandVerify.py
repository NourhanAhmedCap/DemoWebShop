from playwright.sync_api import Playwright, Page, expect
from pages.page_setup import init_pages
import pytest
import re

@pytest.mark.regression
def test_2_Reg_CheckOrderIdandPrint(page:Page, test_data ,recall):
    user = test_data["data"]["valid_user"]
    pages = init_pages(page)
    with open("order_number.txt") as f:
        OrderNumber = f.read().strip()
    path = f"C:/Users/nourahme/Downloads/Order_{OrderNumber}.pdf"
    expected_block = [f"Order# {OrderNumber}","Billing Information","Shipping Information","Company: Capgemini",
    "Name: ",user["FirstName"] ,user["LastName"],"Phone: ",user["Phone"],"Address: ",user["Address1"],user["City"],  user["Zip"],
    user["Country"],"Payment method: Cash On Delivery (COD)","Shipping method: Ground","Blue Jeans 1.00 1 1.00",
    "Casual Golf Belt 1.00 1 1.00","Sub-total: 2.00","Shipping: 10.00", "Shipping: 10.00", "Tax: 0.00"]
    pages.basics.verify_texts_in_pdf(path,expected_block)
  