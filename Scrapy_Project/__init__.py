from Scrapy_Project.amazonreview.amazon_review.amazon_review.onedirect_config import SheetToSql
from Scrapy_Project.amazonreview.amazon_review.amazon_review.onedirect_config import AmazonLinks
from Scrapy_Project.amazonreview.amazon_review.amazon_review.onedirect_config import MysqlUtil

if __name__ == '__main__':
    SheetToSql(MysqlUtil(), AmazonLinks().data)
