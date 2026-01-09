import csv
import pandas as pd
import glob

def merge_csv_files(path, merged_file_name):
    # Path to CSV files
    files = glob.glob(f"{path}/thalgo_*.csv")

    # Read and combine
    df = pd.concat(
        (pd.read_csv(f, encoding="utf-8-sig") for f in files),
        ignore_index=True
    )

    # Save merged file
    df.to_csv(f"{merged_file_name}", index=False)

    print(f"Merged {len(files)} files into {merged_file_name}")

def save_json_list_as_csv(file_name, json_data_list):
    with open(file_name, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=json_data_list[0].keys())
        writer.writeheader()
        writer.writerows(json_data_list)