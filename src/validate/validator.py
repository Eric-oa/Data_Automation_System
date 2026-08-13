import re
import pandas as pd

REQUIRED_COLUMNS = ["customer_id", "name", "email", "age", "country", "purchase_amount"]

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
        non_missing_ids = df["customer_id"].dropna()

        if not pd.api.types.is_integer_dtype(non_missing_ids):
            invalid_types["customer_id"] = str(
                df["customer_id"].dtype
            )

    if "purchase_amount" in df.columns:
        non_missing_amount = df["purchase_amount"].dropna()

        if not pd.api.types.is_numeric_dtype(non_missing_amount):
            invalid_types["purchase_amount"] = str(
                df["purchase_amount"].dtype
            )

    return invalid_types

def validate_emails(df):

    invalid_rows = []

    if "email" not in df.columns:
        return invalid_rows

    for index, email in df["email"].items():

        if pd.isna(email):
            invalid_rows.append(index)

        elif not re.match(
            r"^[\w\.-]+@[\w\.-]+\.\w+$",
            str(email)
        ):
            invalid_rows.append(index)

    return invalid_rows

def validate_age(df):

    invalid_rows = []

    if "age" not in df.columns:
        return invalid_rows

    for index, age in df["age"].items():

        if pd.isna(age):
            continue

        if not float(age).is_integer():
            invalid_rows.append(index)
            continue

        if age < 18 or age > 100:
            invalid_rows.append(index)

    return invalid_rows



def validate_purchase_amount(df):

    invalid_rows = []

    if "purchase_amount" not in df.columns:
        return invalid_rows

    for index, amount in df["purchase_amount"].items():

        if pd.isna(amount):
            invalid_rows.append(index)
            continue

        if not isinstance(amount, (int, float)):
            invalid_rows.append(index)
            continue

        if amount < 0:
            invalid_rows.append(index)

    return invalid_rows



def validate_required_values(df):

    required_columns = [
        "customer_id",
        "name",
        "email",
        "country",
        "purchase_amount"
    ]

    missing_values = {}

    for column in required_columns:

        if column in df.columns:

            count = df[column].isna().sum()

            if count > 0:
                missing_values[column] = count

    return missing_values


def validate_customer_ids(df):

    invalid_rows = []

    if "customer_id" not in df.columns:
        return invalid_rows

    duplicate_mask = df["customer_id"].duplicated(
        keep=False
    )

    invalid_rows = df[
        duplicate_mask
    ].index.tolist()

    return invalid_rows




def validate_data(df):

    missing_columns = validate_required_columns(df)

    missing_values = validate_missing_values(df)

    duplicate_count = validate_duplicates(df)

    invalid_types = validate_data_types(df)

    invalid_emails = validate_emails(df)

    invalid_ages = validate_age(df)

    invalid_purchase_amounts = validate_purchase_amount(df)

    invalid_customer_ids = validate_customer_ids(df)

    required_value_errors = validate_required_values(df)

    return {
        "missing_columns": missing_columns,
        "missing_values": missing_values,
        "duplicate_count": duplicate_count,
        "invalid_types": invalid_types,
        "invalid_emails": invalid_emails,
        "invalid_ages": invalid_ages,
        "invalid_purchase_amounts": invalid_purchase_amounts,
        "invalid_customer_ids": invalid_customer_ids,
        "required_value_errors": required_value_errors
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
        print("Email format                  ERROR")
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