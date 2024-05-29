FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ワークディレクトリの作成
WORKDIR /src

# プロジェクトのファイルをコピー
COPY ./service-products/src /src

#RUN mkdir /docs
#COPY ./service-products/docs/oas.yaml /docs

RUN pip install poetry && poetry config virtualenvs.create false
RUN poetry install