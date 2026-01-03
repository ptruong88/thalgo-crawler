from selenium.webdriver.chrome.webdriver import WebDriver
from utils.selenium_element import get_element_text, get_element_attribute, get_url, get_elements, get_element

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

            item_data['image_link'] = get_element_attribute(self.page_content_driver, ['ID:splide08-slide01','TAG_NAME:img'], 'src')
            item_data['url'] = get_url(self.page_content_driver)

            # Processing to get images
            # splide_track = get_element_attribute(self.page_content_driver, ['ID:shopify-section-template--22265855705391__5025aca4-fd38-48fe-b5dd-577ab6e20f22'], 'outerHTML')
            # print(f'splide_track {splide_track}')
            image_elements = get_elements(self.page_content_driver, ['CLASS_NAME:main-product','TAG_NAME:img'])
            print(f'image_elements {len(image_elements)}')
            for index, image_element in enumerate(image_elements):
                image_url = get_element_attribute(image_element, [], 'src')
                # print(f'image_url {image_url}')
                item_data[f'image_link_{index}'] = image_url
        except Exception as e:
            print(f"Error extracting match info: {e}, url: {get_url(self.page_content_driver)}")
        return item_data
    