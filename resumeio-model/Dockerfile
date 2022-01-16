FROM python:3.8
ENV PYTHONUNBUFFERED=1
COPY /processing /processing
COPY config.py config.py
COPY request_parser.py request_parser.py
COPY server.py server.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python3", "server.py"]
