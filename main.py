import os
import json
import csv
import gzip

column_names = ['column_1', 'column_2', 'ccolumn_3', 'column_4',
                        'column_5', 'column_6', 'column_7', 'column_8', 'column_9',
                        'column_10']

def process_json_file(json_file):
    csv_data = []
    with gzip.open(json_file, 'rt') as f:
        for line in f:
            json_data = json.loads(line)
            item_data = json_data['Item']
            csv_row = []
            for key in column_names:
                if key in item_data:
                    csv_row.append(item_data[key].get('S', ''))
                else:
                    csv_row.append('')
            csv_data.append(csv_row)
    return csv_data

def convert_json_to_csv(json_folder, csv_file):
    json_files = [f for f in os.listdir(json_folder) if f.endswith('.json.gz')]
    if not json_files:
        print('No JSON files found in the folder.')
        return
    
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(column_names)
        for json_file in json_files:
            json_path = os.path.join(json_folder, json_file)
            csv_data = process_json_file(json_path)
            writer.writerows(csv_data)
    
    print('Conversion completed. CSV file created:', csv_file)

# Example usage
json_folder = 'path/to/json/files'
csv_file = 'output.csv'
convert_json_to_csv(json_folder, csv_file)
