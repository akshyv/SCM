# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# WORKDIR /backend
 
# COPY ./requirements.txt /code/requirements.txt

# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
# COPY . .

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "81"]


# FROM python:3.9

# RUN mkdir build

# WORKDIR /build

# COPY . .

# RUN pip install --no-cache-dir -r requirements.txt

# WORKDIR /build/app

# CMD python -m uvicorn main:app --host 127.0.0.1 --port 8081


# FROM python:3.9.0-alpine

# WORKDIR /code

# COPY ./requirements.txt /code/requirements.txt

# RUN pip install --no-cache-dir --upgrade -r requirements.txt

# COPY ./app /code/app

# EXPOSE 8000

# CMD ["uvicorn","app.main:app","--proxy-headers", "--host","0.0.0.0", "--port","8000"]


FROM python



WORKDIR /main



COPY ./requirements.txt /main/requirements.txt  



RUN pip install --no-cache-dir --upgrade -r /main/requirements.txt



COPY ./app /main/app



EXPOSE 8000



CMD ["uvicorn","app.main:app","--proxy-headers", "--host","0.0.0.0", "--port","8000"]