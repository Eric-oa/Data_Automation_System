import pandas as pd 
def clean_column_names(df):

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df
def clean_text_columns(df):

    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    return df
def clean_names(df):

    if "name" in df.columns:
        df["name"] = df["name"].str.strip().str.title()

    return df
def clean_emails(df):

    if "email" in df.columns:
        df["email"] = df["email"].str.strip().str.lower()

    return df
def clean_numeric_columns(df):

    if "age" in df.columns:
        df["age"] = pd.to_numeric(df["age"], errors="coerce")

    if "purchase_amount" in df.columns:
        df["purchase_amount"] = pd.to_numeric(
            df["purchase_amount"],
            errors="coerce"
        )

    return df
def transform_data(df):

    df = clean_column_names(df)

    df = clean_text_columns(df)

    df = clean_names(df)

    df = clean_emails(df)

    df = clean_numeric_columns(df)

    return df
 