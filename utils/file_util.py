import csv

def save_json_list_as_csv(file_name, json_data_list):
    with open(file_name, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=json_data_list[0].keys())
        writer.writeheader()
        writer.writerows(json_data_list)