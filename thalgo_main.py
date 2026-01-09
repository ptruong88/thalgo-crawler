from selenium import webdriver
from thalgo.item_page import ItemPage
from thalgo.action_page import ActionPage
from services.config_service import get_thalgo_action_links
from utils.file_util import save_json_list_as_csv, merge_csv_files
import pandas as pd

def main():
    action_links = get_thalgo_action_links()
    print(f'Processing action links from environment: {action_links}')
    for action_link in action_links:
        print(f'Processing action link: {action_link}')
        link_parts = action_link.split("/")
        print(f'link_parts: {link_parts[-1]}')
        try:
            item_data = []

            """Handles WebDriver setup, execution, and teardown."""
            options = webdriver.ChromeOptions()
            options.add_argument("--headless=new")  # Run in headless mode
            # driver = webdriver.Remote(command_executor=get_selenium_url(), options=options)
            driver = webdriver.Chrome(options=options)

            driver.get(action_link)
            action_page = ActionPage(driver)
            item_links = action_page.get_item_page_links()

            print(f'Processing item_links: {len(item_links)}')
            for item_link in item_links:
                item_json = processing_item_link(driver, item_link)
                print(f'item_json: {item_json}')
                item_data.append(item_json)
        except Exception as e:
            print(f"Error processing action link: {e}, url: {action_link}")

        # print("Tear down")
        driver.quit()
        save_json_list_as_csv(f'csv/thalgo_{link_parts[-1]}.csv', item_data)

def processing_item_link(driver, item_link):
    print(f'Processing item_link: {item_link}')
    driver.get(item_link)
    item_page = ItemPage(driver)
    item_json = item_page.get_info()
    return item_json

def proccess_for_shopify_import(df):
    df["Handle"] = (
        "thalgo-" + df["category"].str.strip() + "-" + df["title"].str.strip()
            ).str.lower() \
            .str.replace(r"[^a-z0-9]", "-", regex=True) \
            .str.replace(r"\-+", "-", regex=True)

    print(df[["category", "title", "Handle"]].head())

    
if __name__ == "__main__":
    # main()
    crawled_data_file_name = "csv/crawled_data.csv"
    merge_csv_files("csv", crawled_data_file_name)
    df = pd.read_csv(crawled_data_file_name, encoding="utf-8-sig")
    # print(df.head())
    proccess_for_shopify_import(df)
    df.to_csv("csv/updated_crawled_data.csv", encoding="utf-8-sig")


    # exported_df = pd.read_csv("csv/products_export.csv", encoding="utf-8-sig")
    # combined_df = df.merge(exported_df, on="Handle", how="outer")

    # print(combined_df['Title'])
    # priority = ["Handle", "Title", "title", "category"]
    # remaining = [c for c in combined_df.columns if c not in priority]
    # reorder_combined_df = combined_df[priority + remaining]

    # reorder_combined_df.to_csv("csv/combined.csv", encoding="utf-8-sig")