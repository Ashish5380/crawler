# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class AmazonreviewItem(Item):
    star_rating = Field()
    rating_text = Field()
    author = Field()
    posted_dates = Field()
    review_header = Field()
    review_link = Field()
    user_profile = Field()
    verified_user = Field()
