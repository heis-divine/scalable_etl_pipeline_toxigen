import pandas as pd # type: ignore
def extract_data(file_path):
    # Extracting the dataset
    if file_path.endswith('.json'):
        data = pd.read_json(file_path)
    elif file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format. Use JSON or CSV.")
    return data