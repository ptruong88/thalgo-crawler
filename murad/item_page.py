from selenium.webdriver.chrome.webdriver import WebDriver
from utils.selenium_element import get_element_text, get_element_attribute, get_url, get_elements

class ItemPage:
    def __init__(self, page_content_driver: WebDriver):
        self.page_content_driver = page_content_driver

    def get_info(self):
        item_data = {}
        try:
            item_data["title"] = get_element_text(self.page_content_driver, ['CLASS_NAME:product-name-pdp'])
            item_data['price'] = get_element_text(self.page_content_driver, ['CLASS_NAME:one-time-container', 'CLASS_NAME:otp-product-price-pdp'])
            item_data['volumn'] = get_element_text(self.page_content_driver, ['CLASS_NAME:product-size-pdp', 'CLASS_NAME:whitespace-nowrap'])
            item_data['description'] = get_element_text(self.page_content_driver, ['CSS_SELECTOR:.pb-4 .rte'])

            ingredient_elements = get_elements(self.page_content_driver, ['CLASS_NAME:pagination-ingredients','CLASS_NAME:splide__list', 'TAG_NAME:li'])
            ingredients = []
            for ingredient_element in ingredient_elements:
                ingredients.append(ingredient_element.text)
            item_data['ingredients'] = "".join(ingredients)

            # item_data['ingredients'] = get_element_text(self.page_content_driver, ['CSS_SELECTOR:.pagination-ingredients .splide__slide'])

            item_data['image_link'] = get_element_attribute(self.page_content_driver, ['CSS_SELECTOR:.splide__slide img'], 'src')
        except Exception as e:
            print(f"Error extracting match info: {e}, url: {get_url(self.page_content_driver)}")
        return item_data
    