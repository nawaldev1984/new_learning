FROM node
ENV MONGO_DB_USERNAME=admin \
    MONGO_DB-PWD=qwerty

RUN mkdir -p Docker_test

COPY . /Docker_test
CMD ["node", "/Docker_test/server.js" ]
