from Scrapy_Project.amazonreview.models.amazon_data import AmazonData
from Scrapy_Project.amazonreview.utils.logger import logger

from sqlalchemy.orm import sessionmaker


class ReviewUrls:

    def read_all_urls(self):
        urls = []
        session = sessionmaker(bind=self.db_engine)
        try:
            records = session().query(AmazonData).all()
        except Exception as ex:
            logger.error("Error reading Amazon data records from DB")
        for row in records:
            urls.append(row.product_link)
        return urls
