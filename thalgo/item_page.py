from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from utils.selenium_element import get_element_text, get_element_attribute, get_url, get_elements

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
            item_data['active_ingredients'] = get_element_text(self.page_content_driver, ['CLASS_NAME:produit_ref_detail', 'CLASS_NAME:bloc_actifs', 'ID:contenu_actifs'], True)
            item_data['results'] = get_element_text(self.page_content_driver, ['CLASS_NAME:produit_ref_detail', 'ID:contenu_resultats'], True)
            item_data['image_link'] = get_element_attribute(self.page_content_driver, ['CLASS_NAME:photo_prod'], 'src')

            image_elements = get_elements(self.page_content_driver, ['CLASS_NAME:owl-photos','TAG_NAME:img'])
            for index, image_element in enumerate(image_elements):
                image_url = get_element_attribute(image_element, [], 'src')
                item_data[f'image_link_{index}'] = image_url

            for i in range(len(image_elements),10):
                item_data[f'image_link_{i}'] = ''

            item_data['category'] = get_element_text(self.page_content_driver, ['ID:ariane', 'CLASS_NAME:niveau2'])
        except Exception as e:
            print(f"Error extracting match info: {e}, url: {get_url(self.page_content_driver)}")
        return item_data
    