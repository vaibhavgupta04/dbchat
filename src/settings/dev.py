from dotenv import load_dotenv
load_dotenv()
import os

MYSQL_USER = os.getenv('MYSQL_USER', 'username')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'password')
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_PORT = os.getenv('MYSQL_PORT', '3306')
MYSQL_DB = os.getenv('MYSQL_DB', 'dbname')

DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)


class Settings:
    MYSQL_USER = MYSQL_USER
    MYSQL_PASSWORD = MYSQL_PASSWORD
    MYSQL_HOST = MYSQL_HOST
    MYSQL_PORT = MYSQL_PORT
    MYSQL_DB = MYSQL_DB
    DATABASE_URL = DATABASE_URL

settings = Settings()

print("MYSQL_USER:", settings.MYSQL_USER)
print("MYSQL_PASSWORD:", settings.MYSQL_PASSWORD)
print("MYSQL_HOST:", settings.MYSQL_HOST)
print("MYSQL_PORT:", settings.MYSQL_PORT)
print("MYSQL_DB:", settings.MYSQL_DB)
print("DATABASE_URL:", settings.DATABASE_URL)