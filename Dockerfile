FROM python:3.10.1 AS base
WORKDIR /app
ENV PYTHONPATH=/app/src
EXPOSE 5000
RUN mkdir -p src/services/base

COPY src/ src/
COPY templates/ templates/
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "-u", "-m", "src"]

