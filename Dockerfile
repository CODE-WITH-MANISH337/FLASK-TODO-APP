#base image
FROM python:3.9-slim

#working directory 
WORKDIR /app


#copy the requiremensts
COPY requirements.txt requirements.txt

#run
RUN pip install -r requirements.txt

#ports
EXPOSE 5000


CMD ["python", "./run.py"]
