# QueryMate : Simplifying database interactions
Welcome to the QueryMate project repository! This project aims to leverage natural language processing (NLP) techniques to convert natural language queries into SQL queries. It provides a seamless interface for users to interact with SQL databases using everyday language

## Overview

The NLP2SQL project consists of several components:
    
  + **Language Model**: We utilize advanced language models, such as Google Gemini, to understand and interpret natural language queries.
      
  +  **Semantic Similarity**: To improve the accuracy of our system, we employ semantic similarity techniques to match user queries with predefined SQL templates and examples.
    
  +  **SQL Database Interaction**: The project integrates with SQL databases, allowing users to query databases using natural language.
    
  +  **Few-Shot Learning**: We incorporate few-shot learning techniques to enhance the system's ability to understand new types of queries by learning from a small number of examples.

## Getting Started
Requirement: An API key for using Google GEMINI model. Head to [Makersuite](https://aistudio.google.com/app/apikey) for getting an API key.
```python
#Enter that API key as value
llm = GoogleGenerativeAI(model="gemini-pro",google_api_key="-----ENTER API KEY HERE-----")
```

### To get started with the QueryMate manually, follow these steps:

  1. **Clone the Repository**: Clone this repository to your local machine using `git clone`.

       ```sh
       git clone https://github.com/SmitMehta510/QueryMate.git
       ```

  2. **Install Dependencies**: Install the required dependencies.
      ```sh
      pip install -r requirements.txt
      ```

  3. **Set Up Databases**: Set up your SQL databases and configure the project to connect to them.
      ```sh
      # After login into the mysql user
      cd /db/init.scripts
      source solecraft.sql
      ```
      This will create a new database "Solecraft" which will have 2 tables Shoes and Discounts.
      Code currently has docker configuration for db. Make following change when running locally.
      ```python
      # app/langchain_dbchain.py  . Replace the get_db() function with this code
      db_user = "YOUR-USERNAME"
      db_password = "YOUR-PASSWORD"
      db_host = "localhost"
      db_name = "solecraft"
      
      db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)
      ```
  5. **Run the Project**: Run the main script to start the steamlit server. 
      ```sh
      streamlit run main.py
      ```
      This command will start the project on locallhost on port 8501
  6. **Interact with the System**: Once the system is running, you can interact with it by providing natural language queries.


### To setup QueryMate using docker 
> [!IMPORTANT]
> Docker should be already installed on the system

  1. **Clone the Repository**: Clone this repository to your local machine using `git clone`.

       ```sh
       git clone https://github.com/SmitMehta510/QueryMate.git
       ```
  2. **Docker compose**: You can find a `docker-compose.yml` file on the home folder of this project.
       ```sh
       docker compose up
       ```
       This command will take time, because it builds 2 docker image from their respective docker file.  
       This will start 2 containers:
       + QueryMate application on port 8501  
       + MySQL database on port 3306  
  4. **Interact with the System**: Once the system is running, you can interact with it by providing natural language queries.
  5. **Stop and Remove container**: After interacting with the system, stop and remove the container using  
      ```sh
      docker compose down
      ```
## Examples

Here are some examples of natural language queries that the QueryMate system can handle:

    "How many shoes do we have left for Nike in size 6 and white color?"
    "How much is the total price of the inventory for all size 7 shoes?"
    "If we have to sell all the Adidas shoes today with discounts applied, how much revenue will our store generate?"
