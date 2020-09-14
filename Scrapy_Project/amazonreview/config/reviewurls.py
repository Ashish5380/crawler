from Scrapy_Project.amazonreview.models.amazon_data import AmazonData

from sqlalchemy.orm import sessionmaker


class ReviewUrls:

    def read_all_urls(self):
        urls = []
        session = sessionmaker(bind=self.db_engine)
        records = session().query(AmazonData).all()
        for row in records:
            urls.append(row.product_link)
        return urls
