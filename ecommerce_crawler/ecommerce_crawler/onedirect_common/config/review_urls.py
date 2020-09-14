from ecommerce_crawler.onedirect_common.models.amazon_data import AmazonData
from ecommerce_crawler.onedirect_common.utils.logger import logger
from sqlalchemy.orm import sessionmaker
from ecommerce_crawler.onedirect_common.utils.mysqlutils import MysqlUtil


class ReviewUrls:

    def __init__(self):
        self.urls = self.read_all_urls()

    def read_all_urls(self):
        urls = []
        session = sessionmaker(bind=MysqlUtil.db_engine)
        try:
            records = session().query(AmazonData).all()
            for row in records:
                urls.append(row.product_link)
        except Exception as ex:
            logger.error("Error reading Amazon data records from DB {0}".format(str(ex)))

        return urls