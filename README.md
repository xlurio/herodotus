# Herodotus

<p align="center">
<a href="https://github.com/xlurio/herodotus/actions/workflows/test.yml" target="_blank">
    <img src="https://github.com/xlurio/herodotus/actions/workflows/test.yml/badge.svg?branch=main" alt="Test">
</a>
<a href="https://codecov.io/gh/xlurio/herodotus" target="_blank">
    <img src="https://img.shields.io/codecov/c/github/xlurio/herodotus?color=%2334D058" alt="Coverage">
</a>
<a href="https://pypi.org/project/herodotus" target="_blank">
    <img src="https://img.shields.io/pypi/v/herodotus?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
</p>

## Overview

Herodotus is a simple package for fastening the integration between Scrapy spiders and SQLAlchemy. With a few lines, it easily allows the data to be stored as soon as it gets scraped, providing a faster development for scraping tools.


## Requirements

- Python 3.8+
- [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)
- [Scrapy](https://github.com/scrapy/scrapy)


## Installation

```
$ pip install herodotus

---> 100%
```


## Usage

For using the herodotus, you need to wrap the `parse` method of your spider with the `herodotus.parse_for_db` decorator and pass a sqlalchemy.orm.Session object to it:

```
import herodotus

class MySpider(Spider):

    @herodotus.parse_for_db(session=session)
    def parse(response, **kwargs):
        // code
```

You will also need to yield a object mapped with a database table by using SQLAlchemy ORM:

```
import herodotus

Base = declarative_base()


class MappedModel(Base):
    
    __tablename__ == mappedmodel
    object_id = Column(Integer, primary_key=True)
    some_field = Column(String(50))


class MySpider(Spider):

    @herodotus.parse_for_db(session=session)
    def parse(response, **kwargs):
        // Scrape data
        yield MappedModel(object_id=object_id, some_field=some_field)
```


## License

This project is licensed under the terms of the MIT license.
