import pandas as pd

def extract_json(file_path): 
    df = pd.read_json(file_path)

    return df
