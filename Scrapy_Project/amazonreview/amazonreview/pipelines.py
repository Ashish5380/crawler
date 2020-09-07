# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from mysqlutils import MysqlUtil

import ast


class AmazonreviewPipeline(MysqlUtil):

    def __init__(self, mysql_util):
        self.connection = mysql_util.od_read_db_engine

    def store_db(self, item):
        print("Going to store data to db")
        try:
            self.connection.execute('insert into onedirect.amazon_review(brand_id, star_rating, rating_text, author,'
                                'posted_date, review_header, review_link, user_profile, verified_user, status) '
                                'values(6221, %s,'
                                '%s, %s, %s, %s, %s, %s, %s, 1)', (
                                    str(item['star_rating'][0]),
                                    str(item['rating_text']),
                                    str(item['author'][0]),
                                    str(item['posted_dates']),
                                    str(item['review_header'][0]),
                                    str(item['review_link']),
                                    str(item['user_profile']),
                                    item['verified_user'][0] if len(item['verified_user']) is not 0 else ""
                                ))
        except Exception as e:
            print("Exception occured while saving data")

    def process_item(self, item, spider):
        self.store_db(item)
