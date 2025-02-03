from scripts.load import load_data
from scripts.extract import extract_data
from scripts.transform import transform_data

# Main function
def main():
    # File path to the dataset
    file_path = 'dataset/toxigen.csv'
    
    # Extracting the data
    data = extract_data(file_path)
    print(data.head())
    
    # Transforming the data
    transformed_data = transform_data(data)
    print(transformed_data)
    
    # Loading the data into PostgreSQL
    database_url = 'postgresql://myuser:mypassword@localhost:5432/mydatabase'
    load_data(transformed_data, database_url, 'toxigen_data')

if __name__ == "__main__":
    main()
    