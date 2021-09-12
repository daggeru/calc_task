FROM python:3.8-slim-buster

ARG CALC_SERVICE_URL
ARG DYNAMODB_REGION
ARG DYNAMODB_TABLE_NAME
ARG AWS_DYNAMO_DB_URL

ENV APP_HOST=0.0.0.0
ENV APP_PORT=80

EXPOSE ${APP_PORT}

WORKDIR /api_service
COPY api_service /api_service
RUN pip3 install -r requirements.txt

ENV PYTHONPATH="/api_service"
CMD [ "python3", "app.py"]
