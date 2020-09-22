# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class EcommerceCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AmazonReviewItem(Item):
    star_rating = Field()
    rating_text = Field()
    author = Field()
    posted_dates = Field()
    review_header = Field()
    review_link = Field()
    user_profile = Field()
    verified_user = Field()
    brand_id = Field()
    product_id = Field()
