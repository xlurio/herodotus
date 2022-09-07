"""Utilities for making easy to make tests on the package"""
# pylint: disable=E0213
# pyright: reportUnknownMemberType=false

from typing import Any, Generator, Optional
from scrapy import Spider
from scrapy.selector.unified import Selector
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declared_attr
from tests.db import Base


class FakeModel(Base):
    """Model for storing fake data"""

    @declared_attr
    def __tablename__(cls) -> str:
        table_name: str = cls.__name__
        return table_name.lower()

    unique_id = Column(Integer, primary_key=True, autoincrement=True)
    data1 = Column(String(10))
    data2 = Column(String(10))
    data3 = Column(String(10))


class FakeSpider(Spider):
    """Scrapy spider for testing the Herodotus package"""

    name = "generic_spider"
    allowed_domains = ["fakewebsite.com"]
    start_urls = ["http://fakewebsite.com/"]

    box_xpath = '//div[@class="information-box"]'
    data1_xpath = './/p[@class="fake-information-1"]/text()'
    data2_xpath = './/p[@class="fake-information-2"]/text()'
    data3_xpath = './/p[@class="fake-information-3"]/text()'

    def parse(
        self, response: Selector, **kwargs: Optional[Any]
    ) -> Generator[Any, None, None]:
        box_elements = response.xpath(self.box_xpath)
        unique_id = 0

        box: Selector
        for box in box_elements:
            data1 = box.xpath(self.data1_xpath).get()
            data2 = box.xpath(self.data2_xpath).get()
            data3 = box.xpath(self.data3_xpath).get()

            yield FakeModel(unique_id=unique_id, data1=data1, data2=data2, data3=data3)

            unique_id += 1
