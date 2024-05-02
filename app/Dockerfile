FROM python:3 

WORKDIR /nlp

COPY requirements.txt .

RUN python3 -m venv nlp_env

RUN /bin/bash -c "source nlp_env/bin/activate && pip install -r requirements.txt"

COPY few_shots.py .
COPY langchain_dbchain.py .
COPY main.py .

EXPOSE 8501

# ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501"]
ENTRYPOINT ["/nlp/nlp_env/bin/python", "-m", "streamlit", "run", "main.py", "--server.port=8501"]