FROM python:3.10
COPY . ./home
WORKDIR /home
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
ENV SECRET_KEY ''
ENV HP_HOST 0.0.0.0
ENV HP_PORT 5000
ENV TG_API_KEY ''
ENV TG_ADMIN ''
ENV TG_REPORTS True
ENV DEBUG False
ENTRYPOINT ["python"]
CMD ["honeypot.py"]