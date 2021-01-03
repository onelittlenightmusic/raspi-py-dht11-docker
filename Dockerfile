FROM balenalib/raspberrypi3-debian-python:latest

WORKDIR /usr/src/app
RUN sudo apt update && sudo apt install -y gcc libc6-dev
RUN pip install dht11
COPY app/ /usr/src/app/
CMD ["python", "app.py"]