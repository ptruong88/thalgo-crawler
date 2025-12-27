from services.config_service import get_action_links
from services.selenium_service import get_item_info, get_item_page_links
import csv

def main():
    item_data = []
    action_links = get_action_links()
    print(f'Processing action links from environment: {action_links}')
    for action_link in action_links:
        print(f'Processing action link: {action_link}')
        item_links = get_item_page_links(action_link)
        print(f'Processing item_links: {len(item_links)}')
        for item_link in item_links:
            item_json = get_item_info(item_link)
            print(f'item_json: {item_json}')
            item_data.append(item_json)
    
    save_as_csv(item_data)

def save_as_csv(data):
    with open("output.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)



if __name__ == "__main__":
    main()