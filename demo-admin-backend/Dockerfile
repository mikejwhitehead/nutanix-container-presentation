FROM python:3.8.3

# set default variables
ENV DB_HOST demo-admin-app-db
ENV DB_PORT 27017
ENV API_SERVER_HOST 0.0.0.0
ENV API_SERVER_PORT 5000

# install netcat
RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

# copy backend app
COPY . /demo-admin-backend
WORKDIR /demo-admin-backend

# install requirements
RUN pip install -r requirements.txt

# chmod entrypoint
RUN chmod +x entrypoint.sh

# run server
CMD ["/demo-admin-backend/entrypoint.sh"]