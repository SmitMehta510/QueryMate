from langchain_community.utilities.sql_database import SQLDatabase
from langchain_experimental.sql.base import SQLDatabaseChain
from langchain_core.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from few_shots import few_shots

def get_llm():
    llm = GoogleGenerativeAI(model="gemini-pro",google_api_key="-----ENTER API KEY HERE-----")
    return llm


def get_db():
    # db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=0)
    db = SQLDatabase.from_uri("mysql+pymysql://root:password@database:3306/solecraft?charset=utf8mb4",sample_rows_in_table_info=0)
    return db


def get_few_shot_db_chain(llm,db):
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    to_vectorize = [" ".join(example.values()) for example in few_shots]

    vectorstore = Chroma.from_texts(texts = to_vectorize, embedding = embeddings, collection_name = "Demo", metadatas = few_shots)

    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2,
    )

    example_selector.select_examples({"Question": "How many Adidas shoes I have left in my store?"})

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    PREFIX = """You are an agent designed to interact with a SQL database.
    Given an input question, create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
    Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
    You can order the results by a relevant column to return the most interesting examples in the database.
    You have access to tools for interacting with the database.
    Only use the information returned by the tools to construct your final answer.
    You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

    Dont include ```, ```sql and \n in the output.
    Always consider table name to be in lowercase only.
    If the query turns out to be INSERT/UPDATE/DELETE query, run the query and return success as answer.
    If the question does not seem related to the database,DO NOT RUN THAT QUERY, just return "Recheck the query" as the answer.
    Always make a proper statement using the answer received from running the query and return that statement as answer
    Never return direct database object , always convert the object to natural language string response and then add to answer.

    You must DOUBLE check all the constraints mentioned earlier and adhere to them strictly.
    
    Here are some examples of user inputs and their corresponding SQL queries:"""

    FORMAT_INSTRUCTIONS = """Use the following format:

    Question: Question here
    SQLQuery: SQL Query to run
    SQLResult: Result of the SQLQuery
    Answer: Final answer here
    """
    SUFFIX = """Only use the following tables:
    {table_info}

    Question: {input}"""


    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=PREFIX,
        suffix=FORMAT_INSTRUCTIONS + SUFFIX,
        input_variables=["input", "table_info", "top_k"], 
    )

    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)

    return chain