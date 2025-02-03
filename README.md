TOXIGEN ETL Pipeline
This project is an ETL (Extract, Transform, Load) pipeline designed to process the TOXIGEN dataset for toxic language detection. The pipeline extracts data from a JSON/CSV file, cleans and transforms it, and loads it into a PostgreSQL 

Project Requirements

This project was completed as part of a technical test and adheres to the following requirements:

Extract data from the TOXIGEN dataset.

Transform and clean the data, including categorizing it for easier analysis.

Load the cleaned data into a PostgreSQL or MongoDB database.

Optimize the pipeline for handling large-scale data.

Use GitHub for version control

Provide a README with setup instructions and optimization suggestions.

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
   run the main file etl_pipeline.py
