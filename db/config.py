def database_config():
    db_name = 'mydatabase'
    db_user = 'myuser'
    db_host = 'localhost'
    db_password = 'mypassword'
    db_port = 5432
    # database_url = f'postgresql://myuser:mypassword@localhost:5432/mydatabase'
    database_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    print(database_url)


