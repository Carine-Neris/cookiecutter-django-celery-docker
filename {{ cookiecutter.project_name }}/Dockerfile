FROM python:3.8

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code/media
RUN touch /code/.env
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip -r requirements.txt 
ADD . /code/


RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    xvfb \
    && rm -rf /var/lib/apt/lists/*


# set display port to avoid crash
ENV DISPLAY=:99
