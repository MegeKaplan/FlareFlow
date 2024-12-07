from dotenv import load_dotenv
import os
import pymysql

load_dotenv()

flare_db_host = os.getenv("FLARE_DB_HOST")
flare_db_user = os.getenv("FLARE_DB_USER")
flare_db_password = os.getenv("FLARE_DB_PASSWORD")
flare_db_name = os.getenv("FLARE_DB_NAME")
flare_db_port = os.getenv("FLARE_DB_PORT")


def get_db_connection():
    return pymysql.connect(
        host=flare_db_host,
        user=flare_db_user,
        password=flare_db_password,
        database=flare_db_name,
        port=int(flare_db_port),
    )
