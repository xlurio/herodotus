"""The module reserved for the decorators available by the Herodotus package"""

from typing import Any, Callable, Dict, Iterator, Optional
from sqlalchemy.orm import Session, registry
from scrapy.http.response import Response


def parse_for_db(
    parse_method: Callable[[Response, Optional[Any]], Iterator[registry]],
    response: Response,
    session: Session,
    *args: Optional[Any]
) -> Iterator[Dict[str, Any]]:
    """Decorator for Scrapy Spider parsing method for automatically storing data into
    the database

    Args:
        parse_method (Callable[[Response], Iterator[registry]]): the method to parse the
        HTTP response into data to store
        response (Response): the HTTP response to be parsed
        session (Session): the SQLAlchemy session to store the data into the database

    Yields:
        Iterator[Dict[str, Any]]: the stored objects iterator
    """
    result: registry

    for result in parse_method(response, *args):
        session.add(result)  # type: ignore

        yield vars(result)
