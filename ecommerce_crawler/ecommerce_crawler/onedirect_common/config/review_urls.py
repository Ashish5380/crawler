from ecommerce_crawler.onedirect_common.models.amazon_data import AmazonData
from ecommerce_crawler.onedirect_common.utils.logger import logger
from sqlalchemy.orm import sessionmaker
from ecommerce_crawler.onedirect_common.utils.mysqlutils import MysqlUtil


class ReviewUrls:

    def __init__(self):
        self.db_engine = MysqlUtil().db_engine
        self.urls = self.read_all_urls()

    def read_all_urls(self):
        request_data = []
        try:
            session = sessionmaker(bind=self.db_engine)
            records = session().query(AmazonData).all()
            for row in records:
                data = {}
                data.__setitem__("brand_id", row.brand_id)
                data.__setitem__("product_id", row.id)
                data.__setitem__("review_link", row.review_links)
                request_data.append(data)
        except Exception as ex:
            logger.error("Error reading Amazon data records from DB :: {0}".format(str(ex)))

        return request_data


if __name__ == "__main__":
    url = ReviewUrls()
    print(url.read_all_urls())
