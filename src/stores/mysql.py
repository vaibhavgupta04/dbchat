import os
os.environ["OPENAI_API_KEY"] = ""

db_user = ""
db_password = ""
db_host = ""
db_name = "testdb"
from langchain_community.utilities.sql_database import SQLDatabase
# db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=1,include_tables=['customers','orders'],custom_table_info={'customers':"customer"})
db = SQLDatabase.from_uri(f"mysql+pymysql://root:admin@localhost:3306/testdb")
print(db.dialect)
print(db.get_usable_table_names())
print(db.table_info)
