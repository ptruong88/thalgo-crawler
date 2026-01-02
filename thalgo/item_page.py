from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from utils.selenium_element import get_element_text, get_element_attribute, get_url

class ItemPage:
    def __init__(self, page_content_driver: WebDriver):
        self.page_content_driver = page_content_driver

    def get_info(self):
        item_data = {}
        try:
            item_data["title"] = get_element_text(self.page_content_driver, ['CLASS_NAME:produit_ref_detail', 'CLASS_NAME:designation'])
            item_data['price'] = get_element_text(self.page_content_driver, ['CLASS_NAME:produit_ref_detail', 'CLASS_NAME:bloc_prix', 'CLASS_NAME:prix'])
            item_data['volumn'] = get_element_text(self.page_content_driver, ['CLASS_NAME:produit_ref_detail', 'CLASS_NAME:contenance', 'CLASS_NAME:text'])
            item_data['description'] = get_element_text(self.page_content_driver, ['CLASS_NAME:produit_ref_detail', 'CLASS_NAME:produits_description'])
            item_data['ingredients'] = get_element_text(self.page_content_driver, ['CLASS_NAME:produit_ref_detail', 'CLASS_NAME:bloc_infosup', 'CLASS_NAME:bloc_ingredients', 'ID:contenu_ingredients'], True)
            item_data['image_link'] = get_element_attribute(self.page_content_driver, ['CLASS_NAME:photo_prod'], 'src')
        except Exception as e:
            print(f"Error extracting match info: {e}, url: {get_url(self.page_content_driver)}")
        return item_data
    