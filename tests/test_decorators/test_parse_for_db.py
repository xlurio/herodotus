"""Tests for the parse_for_db decorator"""
import os
import pytest
from scrapy.selector.unified import Selector
from sqlalchemy.orm import Session
from tests.helpers import FakeSpider, FakeModel
from tests.db import make_session, engine
from herodotus.decorators import parse_for_db


class TestParseForDB:
    """Tests for the parse_for_db decorimport warningsator"""

    @pytest.fixture
    def _fake_response(self) -> Selector:
        current_directory = os.path.dirname(__file__)
        directory_path = os.path.abspath(current_directory)
        fake_page_path = os.path.join(directory_path, "../resources/fake_page.html")

        content: str

        with open(fake_page_path, "r", encoding="utf8") as page:
            content = page.read()

        return Selector(text=content)

    def test_parse(self, _fake_response: Selector) -> None:
        """Test parsing data"""
        self._create_table()

        with make_session() as session:
            self._when_parsed(_fake_response, session)
            self._then_should_store_data(session)

    def _create_table(self) -> None:
        with engine.connect() as connection:
            connection.execute(  # type: ignore
                "CREATE TABLE fakemodel( "
                "   unique_id INT AUTO_INCREMENT, "
                "   data1 VARCHAR(10), "
                "   data2 VARCHAR(10), "
                "   data3 VARCHAR(10), "
                "   PRIMARY KEY (unique_id)"
                ");"
            )

    def _when_parsed(self, response: Selector, session: Session) -> None:
        spider = FakeSpider()

        for _ in parse_for_db(spider.parse, session=session, response=response):  # type: ignore
            print(_)

        session.commit()

    def _then_should_store_data(self, session: Session) -> None:
        stored_objects = session.query(FakeModel).all()
        number_of_objects = len(stored_objects)

        assert number_of_objects == 3
