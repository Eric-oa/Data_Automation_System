from src.extract.csv_extractor import extract_csv
from src.validate.validator import validate_data, print_validation_report
from src.validate.rejection_handler import (
    find_invalid_rows,
    separate_valid_invalid_rows,
    add_rejection_reasons
    )
from src.transform.cleaner import transform_data
from src.load.file_loader import (
    save_processed_data,
    save_rejected_data
)
from src.extract.excel_extractor import extract_excel
from src.extract.json_extractor import extract_json









file_path = "data/raw/customers.json"

data = extract_json(file_path)

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

invalid_data = add_rejection_reasons(
    invalid_data,
    validation_results
)

save_processed_data(
    valid_data,
    "data/processed/clean_customers.csv"
)

save_rejected_data(
    invalid_data,
    "data/rejected/rejected_customers.csv"
)