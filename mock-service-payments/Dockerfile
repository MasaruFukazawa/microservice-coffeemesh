FROM node:21

WORKDIR /src

# プロジェクトのファイルをコピー
COPY ./mock-service-payments/src /src

RUN mkdir /docs
COPY ./mock-service-payments/docs/payments.yaml /docs

RUN npm install -g npm@latest && npm install