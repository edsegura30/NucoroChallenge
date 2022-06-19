from python:alpine3.15

ARG APP_DIR=/app
WORKDIR $APP_DIR

# Install server dependencies
RUN apk add --update gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev


# Install project dependencies
COPY requirements.txt $APP_DIR
RUN pip3 install -r requirements.txt

COPY . $APP_DIR
RUN ["chmod", "+x", "init-web.sh"]

EXPOSE 8000
CMD ["sh", "init-web.sh"]
