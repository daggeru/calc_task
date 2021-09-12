FROM python:3.8-slim-buster

ENV APP_HOST=0.0.0.0
ENV APP_PORT=81

EXPOSE ${APP_PORT}

WORKDIR /calculations_service
COPY calculations_service /calculations_service
RUN pip3 install -r requirements.txt

ENV PYTHONPATH="/calculations_service"
CMD [ "python3", "app.py"]