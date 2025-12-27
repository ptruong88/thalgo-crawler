from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from utils.selenium_element import get_element_text, get_element_attribute, get_elements

class ActionPage:
    def __init__(self, page_content_driver: WebDriver):
        self.page_content_driver = page_content_driver

    def get_item_page_links(self):
        item_links = []
        try:
            product_item_elements = get_elements(self.page_content_driver, ['CLASS_NAME:produits_listing_visage1', 'CLASS_NAME:products-item'])
            for product_item_element in product_item_elements:
                product_link = get_element_attribute(product_item_element, ['CLASS_NAME:photo', 'TAG_NAME:a'], 'href')
                item_links.append(product_link)

        except Exception as e:
            print(f"Error extracting match info: {e}")
        return item_links
    