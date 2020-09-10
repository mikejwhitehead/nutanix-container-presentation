# build environment
FROM node:alpine as builder

ENV PATH /app/node_modules/.bin:$PATH
WORKDIR /app
COPY package.json .
RUN npm install --silent
COPY . .
RUN npm run-script build

# production environment
FROM nginx:1.15.2-alpine
RUN rm -rf /etc/nginx/conf.d
COPY conf /etc/nginx

COPY --from=builder /app/build /usr/share/nginx/html/

EXPOSE 80

# Copy .env file and shell script to container
WORKDIR /usr/share/nginx/html
COPY ./env.sh .
COPY .env .

# Add bash
RUN apk add --no-cache bash

# Make our shell script executable
RUN chmod +x env.sh

# Start Nginx server
CMD ["/bin/bash", "-c", "/usr/share/nginx/html/env.sh && nginx -g \"daemon off;\""]