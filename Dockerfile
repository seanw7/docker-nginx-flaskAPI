FROM tiangolo/uwsgi-nginx:python3.5

MAINTAINER Sean Wilkie <seanw@protonmail.ch>


COPY ./app /app
ADD  requirements.txt /app
#RUN pip install flask
RUN apt-get update
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install -r requirements.txt

# Add app configuration to Nginx
COPY nginx.conf /etc/nginx/conf.d/

# Copy sample app
EXPOSE 80
WORKDIR /app
#RUN pip3 install -r requirements.txt

#ENTRYPOINT ["python", "run.py"]
