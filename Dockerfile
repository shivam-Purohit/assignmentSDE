FROM python:3.10.12

WORKDIR /test

COPY requirements.txt /test/requirements.txt

RUN pip3 install --no-cache-dir -r /test/requirements.txt

COPY add_data.py /test/add_data.py

COPY /app /test/app

RUN python /test/add_data.py

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
