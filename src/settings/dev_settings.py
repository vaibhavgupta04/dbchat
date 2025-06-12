from dotenv import load_dotenv
load_dotenv()
import os

MYSQL_USER = os.getenv('MYSQL_USER', 'username')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'password')
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_PORT = os.getenv('MYSQL_PORT', '3306')
MYSQL_DB = os.getenv('MYSQL_DB', 'dbname')
DATABASE_URL = (f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}")


# AI Model Configuration

# OpenAI API keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
# LangChain API keys
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY', '')
LANGSMITH_ENDPOINT = os.getenv('LANGSMITH_ENDPOINT', 'https://api.smith.langchain.com')
LANGCHAIN_TRACING_V2 = os.getenv('LANGCHAIN_TRACING_V2', 'true')
LANGSMITH_TRACING = os.getenv('LANGSMITH_TRACING', 'true')
LANGSMITH_PROJECT = os.getenv('LANGSMITH_PROJECT', 'DB_Tracing')

# Anthropic API keys
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')

class Settings:
    # MySQL settings
    MYSQL_USER = MYSQL_USER
    MYSQL_PASSWORD = MYSQL_PASSWORD
    MYSQL_HOST = MYSQL_HOST
    MYSQL_PORT = MYSQL_PORT
    MYSQL_DB = MYSQL_DB
    DATABASE_URL = DATABASE_URL

    # OpenAI settings
    OPENAI_API_KEY = OPENAI_API_KEY

    # LangChain settings
    LANGCHAIN_API_KEY = LANGCHAIN_API_KEY
    LANGSMITH_ENDPOINT = LANGSMITH_ENDPOINT
    LANGCHAIN_TRACING_V2 = LANGCHAIN_TRACING_V2
    LANGSMITH_TRACING = LANGSMITH_TRACING
    LANGSMITH_PROJECT = LANGSMITH_PROJECT

    # Anthropic settings
    ANTHROPIC_API_KEY = ANTHROPIC_API_KEY

settings = Settings()
