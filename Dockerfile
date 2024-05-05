FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

COPY Public /usr/share/nginx/html
