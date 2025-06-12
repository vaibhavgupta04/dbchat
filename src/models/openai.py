import os
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from dotenv import load_dotenv

from src.stores.mysql import db
from pydantic import SecretStr
load_dotenv()
api_key_env = SecretStr(os.getenv("OPEN_API_KEY", ""))




llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=api_key_env)
generate_query = create_sql_query_chain(llm, db)
query = generate_query.invoke({"question": ""})
print(query)



execute_query = QuerySQLDataBaseTool(db=db)
execute_query.invoke(query)