"""The module reserved for the decorators available by the Herodotus package"""

from typing import Callable
from sqlalchemy.orm import Session, registry
from scrapy.http.response import Response
from _collections_abc import list_iterator  # type: ignore


def parse_for_db(
    parse_method: Callable[[Response], list_iterator],  # type: ignore
    response: Response,
    session: Session,
):
    """Decorator for Scrapy Spider parsing method for automatically storing data into
    the database

    Args:
        parse_method (Callable[[Response], list_iterator]): the method that parses the
        response to the wanted data
        response (Response): response to parse
        session (Session): the SQLAlchemy session to save the data into the database
    """
    result: registry

    for result in parse_method(response):
        session.add(result)  # type: ignore

        yield vars(result)
