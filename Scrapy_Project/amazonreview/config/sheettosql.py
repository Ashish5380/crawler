from sqlalchemy.orm import sessionmaker
from Scrapy_Project.amazonreview.utils.mysqlutils import MysqlUtil
from Scrapy_Project.amazonreview.config import AmazonLinks
from Scrapy_Project.amazonreview.models.amazon_data import AmazonData
from datetime import datetime

class SheetToSql(MysqlUtil, AmazonLinks):

    def __init__(self, mysql_util, data):
        super().__init__()
        self.read_connection = mysql_util.od_read_db_engine
        self.write_connection = mysql_util.od_write_db_engine
        self.spreadsheet_data = data
        self.update_product_data_mysql(spreadsheet_data=self.spreadsheet_data)

    def update_product_data_mysql(self, spreadsheet_data):
        session = sessionmaker(bind=self.read_connection)()
        for row in spreadsheet_data:
            data = AmazonData(row)
            data.created_at = datetime.now()
            data.created_by = 93271
            data.updated_at = datetime.now()
            data.updated_by = 93271
            session.add(data)
            session.commit()
        sessionmaker.close_all()


if __name__ == '__main__':
    amazon_data = AmazonLinks().data
    mysqlUtils = MysqlUtil()
    SheetToSql(mysqlUtils, amazon_data)
