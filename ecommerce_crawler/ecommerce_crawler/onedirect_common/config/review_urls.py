from ecommerce_crawler.onedirect_common.models.amazon_data import AmazonData
from ecommerce_crawler.onedirect_common.utils.logger import logger
from ecommerce_crawler.onedirect_common.utils.mysqlutils import MysqlUtil

from sqlalchemy.orm import sessionmaker


class ReviewUrls:

    db_engine = None

    def __init__(self):
        self.db_engine = MysqlUtil().db_engine
        self.urls = self.read_all_urls()

    def read_all_urls(self):
        urls = []
        session = sessionmaker(bind=self.db_engine)
        try:
            records = session().query(AmazonData).all()
            for row in records:
                urls.append(row.review_links)
        except Exception as ex:
            logger.error("Error reading Amazon data records from DB {0}".format(ex))
        return urls
