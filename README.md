TOXIGEN ETL Pipeline
This project is an ETL (Extract, Transform, Load) pipeline designed to process the TOXIGEN dataset for toxic language detection. The pipeline extracts data from a JSON/CSV file, cleans and transforms it, and loads it into a PostgreSQL database.

PROJECT REQUIREMENTS 

This project adheres to the following requirements:
Extract data from the TOXIGEN dataset.
Transform and clean the data, including categorizing it for easier analysis.
Load the cleaned data into a PostgreSQL or MongoDB database.
Optimize the pipeline for handling large-scale data.
Use GitHub for version control
Provide a README with setup instructions and optimization suggestions.

PROJECT STRUCTURE
scalable-etl-pipeline/
 |── dataset/             # Raw dataset (excluded from GitHub due to size)
 |── scripts/             # ETL scripts
 |   ├── extract.py       # Extract data from CSV/JSON
 |   ├── transform.py     # Clean and categorize data
 |   ├── load.py          # Load data into database
 |── db/                  # Database setup
 |   ├── config.py        # Database connection settings
 |── .gitignore           # Ignore large files & virtual environments
 |── etl_pipeline.py      # main python file
 |── requirements.txt     # Dependencies
 |── README.md            # Documentation

SETUP INSTRUCTIONS

1) Clone Repository:
   gh repo clone heis-divine/scalable_etl_pipeline_toxigen
   cd scalable-etl-pipeline
2) Set Up Virtual Environment:
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
3) Install Dependencies:
   pip install -r requirements.txt
4) Database Configuration:
   Create a PostgreSQL database.
   Update database_url in the main(etl_pipeline.py) with your credentials(Deatils from your PostgreSQL database).
5) Run the ETL Pipeline:
   run the main file etl_pipeline.py("python etl_pipeline.py")

   
HANDLING LARGE FILES

Due to GitHub's file size limitations, the dataset and other large files have been removed from version control. To run this project, manually download the dataset from the TOXIGEN repository and place it in the dataset/ folder. Alternatively I have compressed the entire pipeline and datsets which can be sent on request.

OPTIMIZATION SUGGESTIONS
1) Integrate AWS Glue Data Quality to detect data anomalies before ingestion.
2) Batch Processing by loading data in chunks instead of as a whole or by row.
3) Store large datasets in the cloud e.g Amazon S3, Google Cloud Storage, or Firebase Storage instead of locally.
4) Real-Time Processing with Apache Kafka or AWS Lambda.
5) Training and using a different model for better classification.


