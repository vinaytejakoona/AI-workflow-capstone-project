FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python ./model.py
EXPOSE 5000
ENV FLASK_APP flask.py
ENTRYPOINT ["python -m flask run"]
