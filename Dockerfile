FROM python:slim

COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app /app

WORKDIR /app

EXPOSE 8000

ENTRYPOINT [ "python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000" ]
