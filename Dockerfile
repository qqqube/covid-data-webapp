FROM python:3

# set a directory for the app
WORKDIR /usr/src

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8111

CMD ["python3", "server.py"]