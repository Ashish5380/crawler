from Scrapy_Project.amazonreview.models.amazon_data import AmazonData
from Scrapy_Project.amazonreview.utils.logger import logger
from Scrapy_Project.amazonreview.utils.mysqlutils import MysqlUtil

from sqlalchemy.orm import sessionmaker


class ReviewUrls:

    def __init__(self):
        super().__init__()
        self.db_engine = MysqlUtil().db_engine

    def read_all_urls(self):
        urls = []
        session = sessionmaker(bind=self.db_engine)
        try:
            records = session().query(AmazonData).all()
            for row in records:
                urls.append(row.product_link)
        except Exception as ex:
            logger.error("Error reading Amazon data records from DB")

        return urls
