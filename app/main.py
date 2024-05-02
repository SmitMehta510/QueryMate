import sqlalchemy
from langchain_dbchain import get_few_shot_db_chain
from langchain_dbchain import get_llm, get_db


import streamlit as st

def parse_answer(result_string):
  if "Question" in result_string and "SQLQuery" in result_string:
    lines = result_string.splitlines()

    question = lines[0].split(':')[1].strip()  

    sql_query = lines[1]

    return question, sql_query
  else:
    return None


llm = get_llm()
db = get_db()

st.title("Solecraft shoes")

table_info = db.get_table_info()

markdown_output = ""

for create_table_statement in table_info.split('\n\n'):
    lines = create_table_statement.strip().split('\n')
    

    table_name = lines[0].split(' ')[2].strip()
    markdown_output += f"\n Attributes in table '**{table_name}**':\n"
    
    for line in lines[1:-1]:
        if 'PRIMARY' not in line and 'CONSTRAINT' not in line:
            parts = line.strip().split(' ')
            column_name = parts[0].strip(',')
            column_type = ' '.join(parts[1:])
        else:
            break
        
        markdown_output += f"\n*  **{column_name}**"
    

    markdown_output += "\n"

st.sidebar.markdown(markdown_output)


question = st.text_input("Question:")

parsed_result ="result"

chain = get_few_shot_db_chain(llm, db)
if question:
    with st.spinner("Finding the answer..."):
        try:
            answer = chain.invoke(question)
        except sqlalchemy.exc.ProgrammingError as e:
           st.error("The database is related to Shoes store and has shoes and discounts information. Kindly recheck the input")
        else:
            parsed_result = parse_answer(answer['result'])
            st.header("Answer")
            if parsed_result:
                st.write("No result found. Kindly recheck the input")
            else:
                st.write(answer['result'])


