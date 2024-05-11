FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ワークディレクトリの作成
WORKDIR /src

# プロジェクトのファイルをコピー
COPY ./service-order/src /src
COPY ./service-order/docs/oas.yaml /src

RUN pip install poetry && poetry config virtualenvs.create false
RUN poetry install