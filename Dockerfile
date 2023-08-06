FROM python/python:3.8
WORKDIR /app
COPY ./app
USER root
COPY ./defect/app/defect
CMD ["python","app.py"]