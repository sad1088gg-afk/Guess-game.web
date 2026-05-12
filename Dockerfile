FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install flask gunicorn

EXPOSE 10000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:10000"]
