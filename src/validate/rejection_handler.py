import pandas as pd

def find_invalid_rows(df, validation_results):

    invalid_rows = set()

    # Invalid emails
    for row in validation_results["invalid_emails"]:
        invalid_rows.add(row)

    # Invalid ages
    for row in validation_results["invalid_ages"]:
        invalid_rows.add(row)

    # Invalid purchase amounts
    for row in validation_results["invalid_purchase_amounts"]:
        invalid_rows.add(row)

    # Duplicate customer IDs
    for row in validation_results["invalid_customer_ids"]:
        invalid_rows.add(row)

    return sorted(invalid_rows)


def separate_valid_invalid_rows(df, invalid_rows):

    invalid_data = df.loc[invalid_rows]

    valid_data = df.drop(index=invalid_rows)

    return valid_data, invalid_data



def add_rejection_reasons(df, validation_results):

    df = df.copy()

    df["rejection_reason"] = ""

    for row in validation_results["invalid_emails"]:
        df.loc[row, "rejection_reason"] = "invalid_email"

    for row in validation_results["invalid_ages"]:
        df.loc[row, "rejection_reason"] = "invalid_age"

    for row in validation_results["invalid_purchase_amounts"]:
        df.loc[row, "rejection_reason"] = "invalid_purchase_amount"

    for row in validation_results["invalid_customer_ids"]:
        df.loc[row, "rejection_reason"] = "duplicate_customer_id"

    return df