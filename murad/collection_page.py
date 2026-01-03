from selenium.webdriver.chrome.webdriver import WebDriver
from utils.selenium_element import get_element_text, get_element_attribute, get_elements, get_url, get_element, get_title

class CollectionPage:
    def __init__(self, page_content_driver: WebDriver):
        self.page_content_driver = page_content_driver

    def get_item_page_links(self):
        item_links = []
        try:
            product_item_elements = get_elements(self.page_content_driver, ['ID:MainContent', 'CLASS_NAME:product-card-outer-wrapper'])
            for product_item_element in product_item_elements:                
                url = get_element_attribute(product_item_element, ['CLASS_NAME:plp-product-name'], 'href')
                item_links.append(url)                

        except Exception as e:
            print(f"Error extracting match info: {e}, url: {get_url(self.page_content_driver)}")
        return item_links
    
    def get_title(self):
        return get_title(self.page_content_driver)
    