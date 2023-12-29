FROM python:3.11.0-slim
WORKDIR /code
EXPOSE 8000
COPY ./api/requirements.txt /code/requirements.txt
COPY ./api /code
RUN mkdir sqlitedb
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN python3 database.py
RUN python3 fillDb.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
