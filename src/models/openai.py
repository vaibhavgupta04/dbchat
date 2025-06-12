import os
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from src.stores.mysql import db



# Generate SQL query from user question
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
generate_query = create_sql_query_chain(llm, db=db, dialect="mysql", verbose=True)
query = generate_query.invoke({"question": ""})
print(query)
execute_query = QuerySQLDataBaseTool(db=db)
execute_query.invoke(query)


# Create a prompt to rephrase the answer based on the SQL result
answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, and SQL result, answer the user question.
        Question: {question}
        SQL Query: {query}
        SQL Result: {result}
        Answer: 
    """
 )

rephrase_answer = answer_prompt | llm | StrOutputParser()

chain = (
     RunnablePassthrough.assign(query=generate_query).assign(
         result=itemgetter("query") | execute_query
     )
     | rephrase_answer
 )

chain.invoke({"question": "How many customers have an order count greater than 5"})
