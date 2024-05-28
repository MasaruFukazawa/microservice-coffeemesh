# -*- coding: utf-8 -*-


class OrderNotFoundError(Exception):
    """
    注文が存在しないことを通知する例外
    """

    pass


class APIIntegrationError(Exception):
    """
    API 統合エラーが発生していることを通知する例外
    """

    pass


class InvalidActionError(Exception):
    """
    実行しようとしているアクションが無効であることを通知する例外
    """

    pass
