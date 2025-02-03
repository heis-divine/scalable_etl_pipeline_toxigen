def transform_data(data):
    # Cleaning the data remove duplicates and handle missing values
    data = data.drop_duplicates()
    data.dropna(inplace=True)
    
    # Normalize text columns
    data['prompt'] = data['prompt'].str.lower().str.strip()
    data['generation'] = data['generation'].str.lower().str.strip()
    
    # Categorize prompt toxicity using prompt_label
    data['prompt_toxicity'] = data['prompt_label'].apply(lambda x: 'toxic' if x == 1 else 'benign')
    
    # Ensure 'generation method' is consistent with other values
    data['generation_method'] = data['generation_method'].str.lower().str.strip()

    return data