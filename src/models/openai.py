from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from src.stores.mysql import db
from pydantic import SecretStr
load_dotenv()
api_key_env = SecretStr(os.getenv("OPEN_API_KEY", ""))



llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=api_key_env)
generate_query = create_sql_query_chain(llm, db)
query = generate_query.invoke({"question": "what is price of `1968 Ford Mustang`"})
# "what is price of `1968 Ford Mustang`"
print(query)
