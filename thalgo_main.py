from selenium import webdriver
from thalgo.item_page import ItemPage
from thalgo.action_page import ActionPage
from services.config_service import get_action_links
from utils.file_util import save_json_list_as_csv

def main():
    item_data = []

    """Handles WebDriver setup, execution, and teardown."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Run in headless mode
    # driver = webdriver.Remote(command_executor=get_selenium_url(), options=options)
    driver = webdriver.Chrome(options=options)

    action_links = get_action_links()
    print(f'Processing action links from environment: {action_links}')
    for action_link in action_links:
        print(f'Processing action link: {action_link}')
        try:
            driver.get(action_link)
            action_page = ActionPage(driver)
            item_links = action_page.get_item_page_links()
            print(f'Processing item_links: {len(item_links)}')
            for item_link in item_links:
                print(f'Processing item_link: {item_link}')
                driver.get(item_link)
                item_page = ItemPage(driver)
                item_json = item_page.get_info()
                # print(f'item_json: {item_json}')
                item_data.append(item_json)
        except Exception as e:
            print(f"Error processing action link: {e}, url: {action_link}")


    # print("Tear down")
    driver.quit()    
    save_json_list_as_csv('thalgo.csv', item_data)



if __name__ == "__main__":
    main()