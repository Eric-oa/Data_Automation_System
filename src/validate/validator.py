import re
import pandas as pd

REQUIRED_COLUMNS = ["customer_id", "name", "email", "age", "county", "purchase_amount"]

EXPECTED_TYPES = {
    "customer_id": "integer",
      "name": "string", 
      "email": "string", 
      "age": "integer", 
      "country": "string", 
      "purchase_amount": "number"
}

def validate_required_columns(df):
    missing_columns = []
    
    for column in REQUIRED_COLUMNS:
        if column not in df.columns:
            missing_columns.append(column)

    return missing_columns

def validate_missing_values(df):
    missing_values = df.isnull().sum()

    return missing_values

def validate_duplicates(df):
    duplicate_count = df.duplicated().sum()

    return duplicate_count


def validate_data_types(df):

    invalid_types = {}

    if "customer_id" in df.columns:
        if not pd.api.types.is_integer_dtype(df["customer_id"]):
            invalid_types["customer_id"] = str(df["customer_id"].dtype)

    if "age" in df.columns:
        non_missing_age = df["age"].dropna()

        if not pd.api.types.is_integer_dtype(non_missing_age):
            invalid_types["age"] = str(df["age"].dtype)

    if "purchase_amount" in df.columns:
        if not pd.api.types.is_numeric_dtype(df["purchase_amount"]):
            invalid_types["purchase_amount"] = str(
                df["purchase_amount"].dtype
            )

    return invalid_types

def validate_emails(df):

    invalid_emails = []

    email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    for index, email in df["email"].items():

        if pd.isna(email):
            continue

        if not re.match(email_pattern, str(email)):
            invalid_emails.append(index)

    return invalid_emails

def validate_data(df):

    missing_columns = validate_required_columns(df)

    missing_values = validate_missing_values(df)

    duplicate_count = validate_duplicates(df)

    invalid_types = validate_data_types(df)

    invalid_emails = validate_emails(df)

    return {
        "missing_columns": missing_columns,
        "missing_values": missing_values,
        "duplicate_count": duplicate_count,
        "invalid_types": invalid_types,
        "invalid_emails": invalid_emails
    }

def print_validation_report(results, df):

    print("\n========================================")
    print("         DATA VALIDATION REPORT")
    print("========================================")

    print(f"\nRows checked: {len(df)}")

    print("\nCHECK                         STATUS")
    print("----------------------------------------")

    if results["missing_columns"]:
        print("Required columns              FAIL")
    else:
        print("Required columns              PASS")

    if results["missing_values"].sum() > 0:
        print("Missing values                WARNING")
    else:
        print("Missing values                PASS")

    if results["duplicate_count"] > 0:
        print("Duplicate records             WARNING")
    else:
        print("Duplicate records             PASS")

    if results["invalid_types"]:
        print("Data types                    WARNING")
    else:
        print("Data types                    PASS")

    if results["invalid_emails"]:
        print("Email format                  WARNING")
    else:
        print("Email format                  PASS")

    print("\n----------------------------------------")
    print("ISSUES")
    print("----------------------------------------")

    if results["missing_columns"]:
        print("\nMissing columns:")
        for column in results["missing_columns"]:
            print(f"    {column}")

    if results["missing_values"].sum() > 0:
        print("\nMissing values:")
        for column, count in results["missing_values"].items():
            if count > 0:
                print(f"    {column}: {count}")

    if results["duplicate_count"] > 0:
        print(f"\nDuplicate rows: {results['duplicate_count']}")

    if results["invalid_types"]:
        print("\nInvalid data types:")
        for column, data_type in results["invalid_types"].items():
            print(f"    {column}: {data_type}")

    if results["invalid_emails"]:
        print("\nInvalid email rows:")
        for row in results["invalid_emails"]:
            print(f"    Row {row}")