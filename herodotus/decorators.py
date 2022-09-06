"""The module reserved for the decorators available by the Herodutus package"""

from typing import Callable
from sqlalchemy.orm import Session
from scrapy.http.response import Response
from _collections_abc import list_iterator  # type: ignore


def parse_for_db(
    parse_method: Callable[[Response], list_iterator],
    response: Response,
    session: Session,
):
    """Decorator for scrapy spider for automatically storing data to database

    Args:
        spider_class (type): the class of the spider
        session (Session): the SQLAlchemy session to save the data
    """
    for result in parse_method(response):
        session.add(result)  # type: ignore
