from Scrapy_Project.amazonreview.config.sheettosql import SheetToSql
from Scrapy_Project.amazonreview.config.spreadsheet import AmazonLinks
from Scrapy_Project.amazonreview.utils.mysqlutils import MysqlUtil

if __name__ == '__main__':
    SheetToSql(MysqlUtil(), AmazonLinks())
