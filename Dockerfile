FROM python:3.8
LABEL maintainer "Meinhard Ploner <dummy@host.com>"
WORKDIR /code
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY ./ ./
EXPOSE 5001
CMD ["flask","run", "-p", "5001","--host=0.0.0.0"]
