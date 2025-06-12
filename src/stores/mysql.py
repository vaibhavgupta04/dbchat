from settings.dev_settings import settings
from langchain_community.utilities.sql_database import SQLDatabase
import threading

class MySQLConfig:
    def __init__(self, user, password, host, port, db_name):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name

    @property
    def url(self):
        return f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"

class SQLDatabaseSingleton:
    _instance = None
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls, config: MySQLConfig):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-checked locking
                    cls._instance = SQLDatabase.from_uri(config.url)
        return cls._instance

# Initialize config from settings
config = MySQLConfig(
    user=settings.MYSQL_USER,
    password=settings.MYSQL_PASSWORD,
    host=settings.MYSQL_HOST,
    port=settings.MYSQL_PORT,
    db_name=settings.MYSQL_DB
)

# Get singleton database instance
db = SQLDatabaseSingleton.get_instance(config)