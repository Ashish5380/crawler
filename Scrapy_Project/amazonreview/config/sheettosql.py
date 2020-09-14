from Scrapy_Project.amazonreview.config.spreadsheet import AmazonLinks
from Scrapy_Project.amazonreview.models.amazon_data import AmazonData
from Scrapy_Project.amazonreview.utils.mysqlutils import MysqlUtil
from Scrapy_Project.amazonreview.utils.logger import logger

from sqlalchemy.orm import sessionmaker


class SheetToSql(MysqlUtil, AmazonLinks):

    def __init__(self, mysql_util, data):
        super().__init__()
        self.db_engine = mysql_util.db_engine
        self.spreadsheet_data = data
        self.update_product_data_mysql(spreadsheet_data=self.spreadsheet_data)

    def update_product_data_mysql(self, spreadsheet_data):
        session = sessionmaker(bind=self.db_engine)()
        for row in spreadsheet_data:
            try:
                data = AmazonData(row)
                session.add(data)
                session.commit()
            except Exception as ex:
                logger.info("Exception Occurred while saving sheet data: {0} to DB with stack trace {1}".format(row, ex))

        sessionmaker.close_all()
