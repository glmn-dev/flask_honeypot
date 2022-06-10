FROM python:3.10
WORKDIR /honeypot
COPY requirements.txt /honeypot
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /honeypot
ENV HP_HOST="0.0.0.0"
ENV HP_PORT=5000
ENV TG_API_KEY=""
ENV TG_ADMIN=""

EXPOSE 5000