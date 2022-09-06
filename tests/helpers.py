from scrapy import Spider


class FakeSpider(Spider):
    """Scrapy spider for testing the Herodotus package"""

    name = "generic_spider"
    allowed_domains = ["fakewebsite.com"]
