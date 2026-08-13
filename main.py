from src.extract.csv_extractor import extract_csv
from src.validate.validator import validate_data, print_validation_report
from src.validate.rejection_handler import (
    find_invalid_rows,
    separate_valid_invalid_rows
)
from src.transform.cleaner import transform_data


file_path = "data/raw/customers.csv"

# EXTRACT
data = extract_csv(file_path)

# VALIDATE
validation_results = validate_data(data)

print_validation_report(validation_results, data)

# SEPARATE
invalid_rows = find_invalid_rows(
    data,
    validation_results
)

valid_data, invalid_data = separate_valid_invalid_rows(
    data,
    invalid_rows
)

print("\nVALID DATA")
print(valid_data)

print("\nINVALID DATA")
print(invalid_data)

# TRANSFORM ONLY VALID DATA
valid_data = transform_data(valid_data)

print("\nTRANSFORMED DATA")
print(valid_data)