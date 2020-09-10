from sqlalchemy.orm import sessionmaker
from Scrapy_Project.amazonreview.utils.mysqlutils import MysqlUtil
from Scrapy_Project.amazonreview.config.spreadsheet import AmazonLinks
from Scrapy_Project.amazonreview.models.amazon_data import AmazonData


class SheetToSql(MysqlUtil, AmazonLinks):

    def __init__(self, mysql_util, data):
        super().__init__()
        self.db_engine = mysql_util.db_engine
        self.spreadsheet_data = data
        self.update_product_data_mysql(spreadsheet_data=self.spreadsheet_data)

    def update_product_data_mysql(self, spreadsheet_data):
        session = sessionmaker(bind=self.db_engine)()
        for row in spreadsheet_data:
            data = AmazonData(row)
            session.add(data)
            session.commit()

        sessionmaker.close_all()
