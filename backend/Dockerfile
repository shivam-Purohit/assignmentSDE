FROM python:3.10.12

WORKDIR /backend

COPY requirements.txt /backend/requirements.txt

RUN pip3 install --no-cache-dir -r /backend/requirements.txt

COPY add_data.py /backend/add_data.py

# copy the backend app
COPY /app /backend/app

# inject the database with values
RUN python /backend/add_data.py

# run the backend server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

