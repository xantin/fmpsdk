from .general import __quotes

from .url_methods import (
    __return_json_v3,
    __validate_exchange,
)

import typing


def quote_short(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quote-short/ API.

    :param apikey: Your API key
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"quote-short/{symbol}"
    query_vars = {
        "apikey": apikey,
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def exchange_realtime(apikey: str, exchange: str) -> typing.List[typing.Dict]:
    """
    Query FMP /quotes/ API.

    :param apikey: Your API key
    :param exchange: Exchange symbol.
    :return: A list of dictionaries.
    """
    return __quotes(apikey=apikey, value=__validate_exchange(exchange))


def historical_stock_dividend(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /historical-price-full/stock_divident/ API

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"historical-price-full/stock_dividend/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)


def historical_stock_split(apikey: str, symbol: str) -> typing.List[typing.Dict]:
    """
    Query FMP /historical-price-full/stock_divident/ API

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :return: A list of dictionaries.
    """
    path = f"historical-price-full/stock_split/{symbol}"
    query_vars = {"apikey": apikey}
    return __return_json_v3(path=path, query_vars=query_vars)