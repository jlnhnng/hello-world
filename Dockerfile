FROM python:3.10.0-alpine3.14
WORKDIR /usr/src/app
RUN mkdir -p /usr/src/app/templates
RUN pip install --upgrade pip
RUN pip install --no-cache-dir flask
COPY . .
CMD [ "python", "-u", "flask-api.py"]