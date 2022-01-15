FROM python:3.8
ENV PYTHONUNBUFFERED=1
COPY infrastructure app
COPY server.py serv.py
COPY config.py config.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python3", "serv.py"]
