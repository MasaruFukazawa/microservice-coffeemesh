FROM node:21

WORKDIR /src

# プロジェクトのファイルをコピー
COPY ./mock-service-kitchen/src /src

RUN mkdir /docs
COPY ./mock-service-kitchen/docs/kitchen.yaml /docs

RUN npm install -g npm@latest && npm install