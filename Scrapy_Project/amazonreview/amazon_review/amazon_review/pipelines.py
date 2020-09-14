pipe

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from Scrapy_Project.amazonreview.models.amazon_review import AmazonReview
from Scrapy_Project.amazonreview.utils.mysqlutils import MysqlUtil

from sqlalchemy.orm import sessionmaker
import hashlib


class AmazonReviewPipeline(MysqlUtil):

    def __init__(self, mysql_util):
        self.db_engine = mysql_util.db_engine

    def process_item(self, data, spider):
        print("Pipeline processing started.")
        amazon_review_data = self.generate_amazon_review_data(data)
        self.store_db(data=amazon_review_data)

    @classmethod
    def generate_amazon_review_data(cls, scrapped_data):
        review_dict = {}
        review_dict.__setitem__("brand_id", scrapped_data['brand_id'])
        review_dict.__setitem__("star_rating", scrapped_data['star_rating'][0])
        review_dict.__setitem__("rating_text", scrapped_data['rating_text'])
        review_dict.__setitem__("author", scrapped_data['author'][0])
        review_dict.__setitem__("posted_date", scrapped_data['posted_dates'])
        review_dict.__setitem__("review_header", scrapped_data['review_header'][0])
        review_dict.__setitem__("review_link", scrapped_data['review_link'])
        review_dict.__setitem__("user_profile", scrapped_data['user_profile'])
        review_dict.__setitem__("verified_user", scrapped_data['verified_user'][0] if len(
            scrapped_data['verified_user']) != 0 else "")
        review_dict.__setitem__("review_text_hash", cls.generate_review_hash(review_dict))
        review_dict.__setitem__("product_id", scrapped_data['product_id'])
        amazon_review_data = AmazonReview(review_data=review_dict)
        return amazon_review_data

    @classmethod
    def generate_review_hash(cls, review_dict):
        hash_string = review_dict.get("review_header") + review_dict.get("rating_text") + review_dict.get("author")
        try:
            review_hash = hashlib.sha256(hash_string.encode(encoding='UTF-8', errors='strict'))
        except Exception as ex:
            print("Exception thrown while hashing string {0} with stacktrace {1}".format(hash_string, ex))
        return review_hash

    def store_db(self, data):
        session = sessionmaker(bind=self.db_engine)()
        print("Going to store data to DB from pipeline")
        try:
            session.add(data)
            session.commit()
        except Exception as ex:
            print("Exception Occurred while saving review data: {0} to DB with stack trace {1}".format(item, ex))
