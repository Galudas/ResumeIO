FROM python:3.8
ENV PYTHONUNBUFFERED=1
COPY model.py model.py
COPY util.py util.py
COPY gensim-develop.zip gensim-develop.zip
COPY server.py server.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python3", "server.py"]
