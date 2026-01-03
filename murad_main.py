from selenium import webdriver
from murad.item_page import ItemPage
from murad.collection_page import CollectionPage
from services.config_service import get_action_links, get_murad_collection_links
from utils.file_util import save_json_list_as_csv
import time

def main():
    collection_links = get_murad_collection_links()
    print(f'Collection_links from environment: {collection_links}')
    for collection_link in collection_links:
        """Handles WebDriver setup, execution, and teardown."""
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")  # Run in headless mode
        # driver = webdriver.Remote(command_executor=get_selenium_url(), options=options)
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(15)

        print(f'Processing collection_link: {collection_link}')
        link_parts = collection_link.split("/")
        print(f'link_parts: {link_parts[-1]}')
        item_data = []
        try:
            driver.get(collection_link)
            collection_page = CollectionPage(driver)
            item_links = collection_page.get_item_page_links()
            # item_links = ['https://www.murad.com/products/retinal-resculpt-eye-lift-treatment']
            print(f'Processing item_links: {len(item_links)}')
            for item_link in item_links:
                item_json = processing_item_link(driver, item_link)
                print(f'item_json: {item_json}')
                item_data.append(item_json)
                
            # save_json_list_as_csv(f'murad_{link_parts[-1]}_{collection_page.get_title()}.csv', item_data)
        except Exception as e:
            print(f"Error processing collection link: {e}, url: {collection_link}")  

         # print("Tear down")
        driver.quit()  

def processing_item_link(driver, item_link):
    print(f'Processing item_link: {item_link}')
    driver.get(item_link)
    time.sleep(5)   
    item_page = ItemPage(driver)
    item_json = item_page.get_info()
    return item_json
    
    
    


if __name__ == "__main__":
    main()