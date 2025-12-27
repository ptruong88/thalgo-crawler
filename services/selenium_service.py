from item_page import ItemPage
from action_page import ActionPage
from selenium import webdriver
from typing import List, Callable, TypeVar
from services.config_service import get_selenium_url

T = TypeVar("T")  # Generic return type for functions that use WebDriver

def with_driver(func: Callable[[webdriver.Chrome], T]) -> T:
    """Handles WebDriver setup, execution, and teardown."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Run in headless mode
    # driver = webdriver.Remote(command_executor=get_selenium_url(), options=options)
    driver = webdriver.Chrome(options=options)
    try:
        return func(driver)
    finally:
        # print("Tear down")
        driver.quit()

def get_item_info(item_link: str):
    def fetch_links(driver: webdriver.Chrome):
        driver.get(item_link)
        item_page = ItemPage(driver)
        return item_page.get_info()
    
    return with_driver(fetch_links)

def get_item_page_links(action_link: str):
    def fetch_links(driver: webdriver.Chrome):
        driver.get(action_link)
        action_page = ActionPage(driver)
        return action_page.get_item_page_links()
    
    return with_driver(fetch_links)