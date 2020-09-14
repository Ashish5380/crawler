import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.in']
    start_urls = ['http://amazon.in/']

    def parse(self, response):
        pass
