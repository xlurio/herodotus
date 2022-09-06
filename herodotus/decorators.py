"""The module reserved for the decorators available by the Herodutus package"""

from sqlalchemy.orm import Session


def parse_for_db(spider_class: type, session: Session):
    """Decorator for scrapy spider for automatically storing data to database

    Args:
        spider_class (type): the class of the spider
        session (Session): the SQLAlchemy session to save the data
    """
    spider = spider_class()

    for result in spider.parse():
        session.add(result)  # type: ignore
