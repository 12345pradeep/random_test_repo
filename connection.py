import pandas as pd


def mysql_connection():
    default_config_filepath = f"./cred.json"
    config = open(default_config_filepath)
    config_data = json.load(config)
    user = config_data['user']
    password = config_data['password']
    host = config_data['host']
    database= config_data['database']
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = conn.cursor(dictionary=True)
    return conn, cursor