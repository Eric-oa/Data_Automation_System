from src.extract.csv_extractor import extract_csv
from src.validate.validator import validate_data, print_validation_report


file_path = "data/raw/customers.csv"

data = extract_csv(file_path)

validation_results = validate_data(data)

print_validation_report(validation_results, data)