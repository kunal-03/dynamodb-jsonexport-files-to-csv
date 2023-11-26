# dynamodb-jsonexport-files-to-csv
Python code that reads all DynamoDB exported JSON files (exported via AWS console) in a local machine folder and converts the data into a CSV file that can be used for various purpose.

## Usage
To use this code, you need to provide the path to the folder containing the JSON files (json_folder), and specify the output CSV file path (csv_file). Also update the column names in the column_name list. The code will iterate over each JSON file, read the gzipped file line by line, extract the required fields, and write the data into the CSV file.

## Install
Please make sure to have the gzip library installed to handle reading gzipped JSON files.

```bash
pip install gzip
```


## License

Copyright (C) 2020 GorillaStack. Licensed under the Apache 2.0 License.
