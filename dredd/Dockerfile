FROM node:21

WORKDIR /src

# プロジェクトのファイルをコピー
COPY ./dredd/src /src

RUN mkdir /docs
COPY ./service-order/docs/oas.yaml /docs

#RUN npm install -g npm@latest && npm install