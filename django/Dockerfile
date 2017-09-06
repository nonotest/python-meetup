FROM python:alpine3.6

# Setup our app
COPY app /usr/src/app
WORKDIR /usr/src/app
RUN cat immutableisgood/views.py

RUN pip install -r requirements.txt



# Start the server
EXPOSE 8000

