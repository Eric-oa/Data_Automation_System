import pandas as pd
import os


def save_processed_data(df, file_path):

    os.makedirs(
        os.path.dirname(file_path),
        exist_ok=True
    )

    df.to_csv(file_path, index=False)

    print(f"\nProcessed data saved to: {file_path}")


def save_rejected_data(df, file_path):

    os.makedirs(
        os.path.dirname(file_path),
        exist_ok=True
    )

    df.to_csv(file_path, index=False)

    print(f"Rejected data saved to: {file_path}")