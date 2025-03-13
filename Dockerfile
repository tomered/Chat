FROM python:3.12.3-slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY app/ /app/

EXPOSE 5000
CMD ["flask", "run"]

