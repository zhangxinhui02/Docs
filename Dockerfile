FROM nginx:latest

WORKDIR /app

COPY . /app

RUN rm -rf /usr/share/nginx/html && \
    cp /app/index.html /app/Docs/ && \
    touch /app/Docs/.nojekyll && \
    ln -s /app/Docs /usr/share/nginx/html
