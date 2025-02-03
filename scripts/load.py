from sqlalchemy import create_engine # type: ignore
def load_data(data, database_url, table_name):

    engine = create_engine(database_url)
    
    # Load the data into the database
    data.to_sql(table_name, engine, if_exists='replace', index=False)
    # data.to_sql(table_name, engine, if_exists='append', index=False, method='multi')