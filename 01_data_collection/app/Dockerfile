# syntax=docker/dockerfile:1


FROM balenalib/raspberry-pi-debian:bullseye
#FROM debian:bullseye
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get -y install wget gnupg
#RUN echo "deb http://archive.raspberrypi.org/debian/ bullseye main" > /etc/apt/sources.list.d/raspberrypi.list
#RUN wget http://archive.raspberrypi.org/debian/raspberrypi.gpg.key -O - | apt-key add -

RUN apt-get update -y
WORKDIR /files


RUN apt-get install -y libcamera-dev libcamera-apps-lite v4l-utils libcamera-tools
RUN apt-get install -y python3 python3-pip python3-opencv python3-picamera2 udev
#RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

COPY requirements.txt requirements.txt


#RUN pip install ./torch-2.0.0-1-cp39-cp39-manylinux2014_aarch64.whl
RUN pip install -r requirements.txt

COPY start.sh ./

RUN chmod +x start.sh

RUN usermod -a -G video root

ENV UDEV=on

CMD ["sh","./start.sh"]
